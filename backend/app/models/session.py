"""
Requirement gathering session model
"""

from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Enum, JSON, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.core.database import Base

class SessionStatus(str, enum.Enum):
    """Session status enumeration"""
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class RequirementSession(Base):
    """Requirement gathering session model"""
    
    __tablename__ = "requirement_sessions"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.ACTIVE)
    context = Column(JSON, default=dict)  # Store conversation context
    dialogue_history = Column(JSON, default=list)  # Store conversation history
    completeness_score = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    project = relationship("Project", back_populates="sessions")
    user = relationship("User", back_populates="sessions")
    
    def __repr__(self):
        return f"<RequirementSession(id={self.id}, project_id={self.project_id}, status={self.status})>"

# Add relationships to other models
from app.models.project import Project
from app.models.user import User

Project.sessions = relationship("RequirementSession", back_populates="project")
User.sessions = relationship("RequirementSession", back_populates="user")