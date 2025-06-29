"""
AI Low-Code Platform endpoints for code generation and deployment
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Dict, Any, Optional
from datetime import datetime

from app.core.database import get_db
from app.models.bitcup_model import BitcupModel
from app.models.lowcode import GeneratedCode, Deployment
from app.services.lowcode_service import lowcode_service
from pydantic import BaseModel

router = APIRouter()

# Pydantic models
class CodeGenerationRequest(BaseModel):
    bitcup_id: str
    tech_stack: Optional[Dict[str, str]] = None

class PreviewRequest(BaseModel):
    code_id: str

class DeploymentRequest(BaseModel):
    code_id: str
    environment: str = "development"

class CodeResponse(BaseModel):
    id: str
    bitcup_id: str
    tech_stack: Dict[str, str]
    frontend: Dict[str, Any]
    backend: Dict[str, Any]
    database: Dict[str, Any]
    deployment: Dict[str, Any]
    created_at: str

class PreviewResponse(BaseModel):
    preview_url: str
    screenshots: List[Dict[str, str]]
    expiration: float

class DeploymentResponse(BaseModel):
    deployment_id: str
    environment: str
    status: str
    url: str
    deployed_at: str

@router.post("/generate-code", response_model=CodeResponse)
async def generate_code(
    request: CodeGenerationRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate code from BITCUP model"""
    
    # Get BITCUP model
    result = await db.execute(select(BitcupModel).where(BitcupModel.id == request.bitcup_id))
    bitcup_model = result.scalar_one_or_none()
    
    if not bitcup_model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="BITCUP model not found"
        )
    
    try:
        # Generate code using service
        implementation_model = bitcup_model.implementation_model
        tech_stack = request.tech_stack or {
            "frontend": "vue",
            "backend": "fastapi",
            "database": "postgresql"
        }
        
        generated_code_content = await lowcode_service.generate_code_from_model(
            implementation_model,
            tech_stack
        )
        
        # Store the generated code in the database
        code_record = GeneratedCode(
            bitcup_id=bitcup_model.id,
            tech_stack=tech_stack,
            frontend_code=generated_code_content["frontend"],
            backend_code=generated_code_content["backend"],
            database_code=generated_code_content["database"],
            deployment_config=generated_code_content["deployment"]
        )
        
        db.add(code_record)
        await db.commit()
        await db.refresh(code_record)
        
        return {
            "id": code_record.id,
            "bitcup_id": code_record.bitcup_id,
            "tech_stack": code_record.tech_stack,
            "frontend": code_record.frontend_code,
            "backend": code_record.backend_code,
            "database": code_record.database_code,
            "deployment": code_record.deployment_config,
            "created_at": code_record.created_at.isoformat()
        }
        
    except Exception as e:
        print(f"Code generation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate code from BITCUP model"
        )

@router.post("/preview", response_model=PreviewResponse)
async def generate_preview(
    request: PreviewRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate a preview of the application"""
    
    try:
        # Get the generated code from the database
        result = await db.execute(select(GeneratedCode).where(GeneratedCode.id == request.code_id))
        code_record = result.scalar_one_or_none()
        
        if not code_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Generated code not found"
            )
        
        # Generate preview
        code_content = {
            "frontend": code_record.frontend_code,
            "backend": code_record.backend_code,
            "database": code_record.database_code,
            "deployment": code_record.deployment_config
        }
        
        preview = await lowcode_service.generate_preview(code_content)
        
        return preview
        
    except Exception as e:
        print(f"Preview generation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate preview"
        )

@router.post("/deploy", response_model=DeploymentResponse)
async def deploy_application(
    request: DeploymentRequest,
    db: AsyncSession = Depends(get_db)
):
    """Deploy the application to the specified environment"""
    
    try:
        # Get the generated code from the database
        result = await db.execute(select(GeneratedCode).where(GeneratedCode.id == request.code_id))
        code_record = result.scalar_one_or_none()
        
        if not code_record:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Generated code not found"
            )
        
        # Deploy the application
        code_content = {
            "frontend": code_record.frontend_code,
            "backend": code_record.backend_code,
            "database": code_record.database_code,
            "deployment": code_record.deployment_config
        }
        
        deployment_result = await lowcode_service.deploy_application(code_content, request.environment)
        
        # Store the deployment in the database
        deployment_record = Deployment(
            code_id=code_record.id,
            environment=request.environment,
            status=deployment_result["status"],
            url=deployment_result["url"]
        )
        
        db.add(deployment_record)
        await db.commit()
        await db.refresh(deployment_record)
        
        return {
            "deployment_id": deployment_record.id,
            "environment": deployment_record.environment,
            "status": deployment_record.status,
            "url": deployment_record.url,
            "deployed_at": deployment_record.deployed_at.isoformat()
        }
        
    except Exception as e:
        print(f"Deployment error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to deploy application"
        )

@router.get("/tech-stacks", response_model=Dict[str, List[str]])
async def get_tech_stacks():
    """Get available technology stacks"""
    
    return lowcode_service.supported_frameworks

@router.get("/code/{code_id}", response_model=CodeResponse)
async def get_generated_code(
    code_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Get generated code by ID"""
    
    result = await db.execute(select(GeneratedCode).where(GeneratedCode.id == code_id))
    code_record = result.scalar_one_or_none()
    
    if not code_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Generated code not found"
        )
    
    return {
        "id": code_record.id,
        "bitcup_id": code_record.bitcup_id,
        "tech_stack": code_record.tech_stack,
        "frontend": code_record.frontend_code,
        "backend": code_record.backend_code,
        "database": code_record.database_code,
        "deployment": code_record.deployment_config,
        "created_at": code_record.created_at.isoformat()
    }

@router.get("/codes/{bitcup_id}", response_model=List[CodeResponse])
async def get_codes_by_bitcup(
    bitcup_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Get all generated code for a BITCUP model"""
    
    result = await db.execute(select(GeneratedCode).where(GeneratedCode.bitcup_id == bitcup_id))
    code_records = result.scalars().all()
    
    return [
        {
            "id": record.id,
            "bitcup_id": record.bitcup_id,
            "tech_stack": record.tech_stack,
            "frontend": record.frontend_code,
            "backend": record.backend_code,
            "database": record.database_code,
            "deployment": record.deployment_config,
            "created_at": record.created_at.isoformat()
        }
        for record in code_records
    ]