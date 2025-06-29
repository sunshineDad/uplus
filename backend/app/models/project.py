"""
Project model for managing user projects
"""

from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.core.database import Base

class ProjectStatus(str, enum.Enum):
    """Project status enumeration"""
    DRAFT = "draft"
    ACTIVE = "active"
    REQUIREMENTS_GATHERING = "requirements_gathering"
    MODELING = "modeling"
    GENERATING = "generating"
    DEPLOYED = "deployed"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class Project(Base):
    """Project model for user projects"""
    
    __tablename__ = "projects"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.DRAFT)
    owner_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    owner = relationship("User", back_populates="projects")
    
    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, status={self.status})>"

# Add relationship to User model
from app.models.user import User
User.projects = relationship("Project", back_populates="owner")