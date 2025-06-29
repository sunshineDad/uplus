"""
AI Product Manager endpoints for intelligent requirement gathering
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Dict, Any
from datetime import datetime

from app.core.database import get_db
from app.models.session import RequirementSession, SessionStatus
from app.models.rsd import RSDDocument
from app.services.ai_service import ai_service
from pydantic import BaseModel

router = APIRouter()

# Pydantic models
class InteractionRequest(BaseModel):
    session_id: str
    message: str
    metadata: Dict[str, Any] = {}

class InteractionResponse(BaseModel):
    response: str
    questions: List[str]
    completeness_score: float
    next_steps: List[str]
    session_updated: bool

class RSDGenerationRequest(BaseModel):
    session_id: str

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

@router.post("/interact", response_model=InteractionResponse)
async def interact_with_ai_pm(
    request: InteractionRequest,
    db: AsyncSession = Depends(get_db)
):
    """Interact with AI Product Manager for requirement gathering"""
    
    # Get session
    result = await db.execute(select(RequirementSession).where(RequirementSession.id == request.session_id))
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    if session.status != SessionStatus.ACTIVE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Session is not active"
        )
    
    try:
        # Analyze user intent
        intent_analysis = await ai_service.analyze_intent(request.message, session.context)
        
        # Update context with new information
        updated_context = session.context.copy()
        if "extracted_info" in intent_analysis:
            updated_context.update(intent_analysis["extracted_info"])
        
        # Add interaction to dialogue history
        dialogue_entry = {
            "timestamp": datetime.now().isoformat(),
            "user_message": request.message,
            "intent_analysis": intent_analysis,
            "metadata": request.metadata
        }
        
        updated_dialogue_history = session.dialogue_history.copy()
        updated_dialogue_history.append(dialogue_entry)
        
        # Generate follow-up questions
        questions = await ai_service.generate_socratic_questions(updated_context, updated_dialogue_history)
        
        # Calculate completeness score (simple heuristic for MVP)
        completeness_score = min(len(updated_dialogue_history) * 0.1, 1.0)
        
        # Generate AI response
        if completeness_score >= 0.8:
            ai_response = "Great! I think we have enough information to create your requirements specification. Would you like me to generate the RSD document?"
            next_steps = ["Generate RSD Document", "Review Requirements", "Continue Gathering"]
        else:
            ai_response = f"Thank you for that information! I understand you want to {intent_analysis.get('extracted_info', {}).get('summary', 'build something great')}. Let me ask a few more questions to ensure we capture all your requirements."
            next_steps = ["Continue Dialogue", "Review Progress"]
        
        # Update session in database
        session.context = updated_context
        session.dialogue_history = updated_dialogue_history
        session.completeness_score = completeness_score
        
        await db.commit()
        
        return InteractionResponse(
            response=ai_response,
            questions=questions,
            completeness_score=completeness_score,
            next_steps=next_steps,
            session_updated=True
        )
        
    except Exception as e:
        print(f"AI-PM interaction error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process interaction"
        )

@router.post("/generate-rsd", response_model=RSDResponse)
async def generate_rsd(
    request: RSDGenerationRequest,
    db: AsyncSession = Depends(get_db)
):
    """Generate Requirements Specification Document from session"""
    
    # Get session
    result = await db.execute(select(RequirementSession).where(RequirementSession.id == request.session_id))
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    if session.completeness_score < 0.7:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Session not complete enough for RSD generation. Continue gathering requirements."
        )
    
    try:
        # Generate RSD using AI
        rsd_content = await ai_service.generate_rsd(session.context, session.dialogue_history)
        
        # Create RSD document
        rsd_document = RSDDocument(
            session_id=session.id,
            project_id=session.project_id,
            functional_requirements=rsd_content.get("functional_requirements", {}),
            non_functional_requirements=rsd_content.get("non_functional_requirements", {}),
            constraints=rsd_content.get("constraints", {}),
            success_criteria=rsd_content.get("success_criteria", {}),
            completeness_score=session.completeness_score,
            validation_results={"generated_by": "ai_pm", "timestamp": datetime.now().isoformat()}
        )
        
        db.add(rsd_document)
        
        # Update session status
        session.status = SessionStatus.COMPLETED
        session.completed_at = datetime.now()
        
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
            detail="Failed to generate RSD document"
        )

@router.get("/session/{session_id}/status")
async def get_session_status(
    session_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Get session status and progress"""
    
    result = await db.execute(select(RequirementSession).where(RequirementSession.id == session_id))
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    return {
        "session_id": session.id,
        "status": session.status,
        "completeness_score": session.completeness_score,
        "interaction_count": len(session.dialogue_history),
        "ready_for_rsd": session.completeness_score >= 0.7,
        "last_updated": session.updated_at.isoformat() if session.updated_at else session.created_at.isoformat()
    }