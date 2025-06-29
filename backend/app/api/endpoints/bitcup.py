"""
BITCUP Modeling Language endpoints for semantic modeling
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Dict, Any
from datetime import datetime

from app.core.database import get_db
from app.models.rsd import RSDDocument
from app.models.bitcup_model import BitcupModel
from app.services.bitcup_service import bitcup_service
from pydantic import BaseModel

router = APIRouter()

# Pydantic models
class BitcupGenerationRequest(BaseModel):
    rsd_id: str

class RSDGenerationRequest(BaseModel):
    bitcup_id: str

class BitcupResponse(BaseModel):
    id: str
    project_id: str
    business_model: Dict[str, Any]
    implementation_model: Dict[str, Any]
    created_at: str

class RSDResponse(BaseModel):
    id: str
    session_id: str
    project_id: str
    functional_requirements: Dict[str, Any]
    non_functional_requirements: Dict[str, Any]
    constraints: Dict[str, Any]
    success_criteria: Dict[str, Any]
    completeness_score: float
    created_at: str

@router.post("/generate-model", response_model=BitcupResponse)
async def generate_bitcup_model(
    request: BitcupGenerationRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate BITCUP model from RSD document"""
    
    # Get RSD document
    result = await db.execute(select(RSDDocument).where(RSDDocument.id == request.rsd_id))
    rsd_document = result.scalar_one_or_none()
    
    if not rsd_document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RSD document not found"
        )
    
    try:
        # Generate BITCUP model using service
        rsd_content = {
            "functional_requirements": rsd_document.functional_requirements,
            "non_functional_requirements": rsd_document.non_functional_requirements,
            "constraints": rsd_document.constraints,
            "success_criteria": rsd_document.success_criteria
        }
        
        bitcup_model_content = await bitcup_service.generate_bitcup_model(rsd_content)
        
        # Create BITCUP model in database
        bitcup_model = BitcupModel(
            project_id=rsd_document.project_id,
            business_model=bitcup_model_content,
            implementation_model=await bitcup_service.transform_to_implementation_spec(bitcup_model_content)
        )
        
        db.add(bitcup_model)
        await db.commit()
        await db.refresh(bitcup_model)
        
        return BitcupResponse(
            id=bitcup_model.id,
            project_id=bitcup_model.project_id,
            business_model=bitcup_model.business_model,
            implementation_model=bitcup_model.implementation_model,
            created_at=bitcup_model.created_at.isoformat()
        )
        
    except Exception as e:
        print(f"BITCUP model generation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate BITCUP model"
        )

@router.post("/generate-rsd", response_model=RSDResponse)
async def generate_rsd_from_bitcup(
    request: RSDGenerationRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate RSD document from BITCUP model (bidirectional transformation)"""
    
    # Get BITCUP model
    result = await db.execute(select(BitcupModel).where(BitcupModel.id == request.bitcup_id))
    bitcup_model = result.scalar_one_or_none()
    
    if not bitcup_model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="BITCUP model not found"
        )
    
    try:
        # Generate RSD document using service
        rsd_content = await bitcup_service.generate_rsd_from_bitcup(bitcup_model.business_model)
        
        # Create RSD document in database
        rsd_document = RSDDocument(
            project_id=bitcup_model.project_id,
            session_id="bitcup_generated",  # Special marker for BITCUP-generated RSDs
            functional_requirements=rsd_content.get("functional_requirements", {}),
            non_functional_requirements=rsd_content.get("non_functional_requirements", {}),
            constraints=rsd_content.get("constraints", {}),
            success_criteria=rsd_content.get("success_criteria", {}),
            completeness_score=rsd_content.get("metadata", {}).get("completeness_score", 0.8),
            validation_results={"generated_by": "bitcup", "timestamp": datetime.now().isoformat()}
        )
        
        db.add(rsd_document)
        await db.commit()
        await db.refresh(rsd_document)
        
        return RSDResponse(
            id=rsd_document.id,
            session_id=rsd_document.session_id,
            project_id=rsd_document.project_id,
            functional_requirements=rsd_document.functional_requirements,
            non_functional_requirements=rsd_document.non_functional_requirements,
            constraints=rsd_document.constraints,
            success_criteria=rsd_document.success_criteria,
            completeness_score=rsd_document.completeness_score,
            created_at=rsd_document.created_at.isoformat()
        )
        
    except Exception as e:
        print(f"RSD generation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate RSD document from BITCUP model"
        )

@router.get("/models/{project_id}", response_model=List[BitcupResponse])
async def get_project_models(
    project_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Get all BITCUP models for a project"""
    
    result = await db.execute(select(BitcupModel).where(BitcupModel.project_id == project_id))
    models = result.scalars().all()
    
    return [
        BitcupResponse(
            id=model.id,
            project_id=model.project_id,
            business_model=model.business_model,
            implementation_model=model.implementation_model,
            created_at=model.created_at.isoformat()
        )
        for model in models
    ]

@router.get("/model/{model_id}", response_model=BitcupResponse)
async def get_model(
    model_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific BITCUP model"""
    
    result = await db.execute(select(BitcupModel).where(BitcupModel.id == model_id))
    model = result.scalar_one_or_none()
    
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="BITCUP model not found"
        )
    
    return BitcupResponse(
        id=model.id,
        project_id=model.project_id,
        business_model=model.business_model,
        implementation_model=model.implementation_model,
        created_at=model.created_at.isoformat()
    )