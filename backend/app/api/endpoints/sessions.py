"""
Requirement gathering session endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Dict, Any

from app.core.database import get_db
from app.models.session import RequirementSession, SessionStatus
from app.models.project import Project
from app.models.user import User
from pydantic import BaseModel

router = APIRouter()

# Pydantic models
class SessionCreate(BaseModel):
    project_id: str

class SessionResponse(BaseModel):
    id: str
    project_id: str
    user_id: str
    status: SessionStatus
    context: Dict[str, Any]
    dialogue_history: List[Dict[str, Any]]
    completeness_score: float
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

class SessionUpdate(BaseModel):
    status: SessionStatus = None
    context: Dict[str, Any] = None
    dialogue_history: List[Dict[str, Any]] = None
    completeness_score: float = None

@router.post("/", response_model=SessionResponse)
async def create_session(
    session_data: SessionCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new requirement gathering session"""
    
    # Verify project exists
    project_result = await db.execute(select(Project).where(Project.id == session_data.project_id))
    project = project_result.scalar_one_or_none()
    
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found"
        )
    
    # Create session
    session = RequirementSession(
        project_id=session_data.project_id,
        user_id=project.owner_id,
        status=SessionStatus.ACTIVE,
        context={
            "project_name": project.name,
            "project_description": project.description,
            "session_started": True
        },
        dialogue_history=[],
        completeness_score=0.0
    )
    
    db.add(session)
    await db.commit()
    await db.refresh(session)
    
    return SessionResponse(
        id=str(session.id),
        project_id=str(session.project_id),
        user_id=str(session.user_id),
        status=session.status,
        context=session.context,
        dialogue_history=session.dialogue_history,
        completeness_score=session.completeness_score,
        created_at=session.created_at.isoformat(),
        updated_at=session.updated_at.isoformat() if session.updated_at else session.created_at.isoformat()
    )

@router.get("/", response_model=List[SessionResponse])
async def list_sessions(
    project_id: str = None,
    db: AsyncSession = Depends(get_db)
):
    """List requirement gathering sessions"""
    
    query = select(RequirementSession)
    
    if project_id:
        query = query.where(RequirementSession.project_id == project_id)
    
    query = query.order_by(RequirementSession.created_at.desc())
    result = await db.execute(query)
    sessions = result.scalars().all()
    
    return [
        SessionResponse(
            id=session.id,
            project_id=session.project_id,
            user_id=session.user_id,
            status=session.status,
            context=session.context,
            dialogue_history=session.dialogue_history,
            completeness_score=session.completeness_score,
            created_at=session.created_at.isoformat(),
            updated_at=session.updated_at.isoformat() if session.updated_at else session.created_at.isoformat()
        )
        for session in sessions
    ]

@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific session"""
    
    result = await db.execute(select(RequirementSession).where(RequirementSession.id == session_id))
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    return SessionResponse(
        id=str(session.id),
        project_id=str(session.project_id),
        user_id=str(session.user_id),
        status=session.status,
        context=session.context,
        dialogue_history=session.dialogue_history,
        completeness_score=session.completeness_score,
        created_at=session.created_at.isoformat(),
        updated_at=session.updated_at.isoformat() if session.updated_at else session.created_at.isoformat()
    )

@router.put("/{session_id}", response_model=SessionResponse)
async def update_session(
    session_id: str,
    session_data: SessionUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Update a session"""
    
    result = await db.execute(select(RequirementSession).where(RequirementSession.id == session_id))
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Session not found"
        )
    
    # Update fields
    if session_data.status is not None:
        session.status = session_data.status
    if session_data.context is not None:
        session.context = session_data.context
    if session_data.dialogue_history is not None:
        session.dialogue_history = session_data.dialogue_history
    if session_data.completeness_score is not None:
        session.completeness_score = session_data.completeness_score
    
    await db.commit()
    await db.refresh(session)
    
    return SessionResponse(
        id=str(session.id),
        project_id=str(session.project_id),
        user_id=str(session.user_id),
        status=session.status,
        context=session.context,
        dialogue_history=session.dialogue_history,
        completeness_score=session.completeness_score,
        created_at=session.created_at.isoformat(),
        updated_at=session.updated_at.isoformat() if session.updated_at else session.created_at.isoformat()
    )