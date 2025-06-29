"""
Requirements Specification Document (RSD) model
"""

from sqlalchemy import Column, String, DateTime, Text, ForeignKey, JSON, Float, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class RSDDocument(Base):
    """Requirements Specification Document model"""
    
    __tablename__ = "rsd_documents"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    session_id = Column(String(36), ForeignKey("requirement_sessions.id"), nullable=False)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)
    
    # RSD Content
    functional_requirements = Column(JSON, default=dict)
    non_functional_requirements = Column(JSON, default=dict)
    constraints = Column(JSON, default=dict)
    success_criteria = Column(JSON, default=dict)
    
    # Metadata
    version = Column(Integer, default=1)
    completeness_score = Column(Float, default=0.0)
    validation_results = Column(JSON, default=dict)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    session = relationship("RequirementSession", back_populates="rsd_document")
    project = relationship("Project", back_populates="rsd_documents")
    
    def __repr__(self):
        return f"<RSDDocument(id={self.id}, project_id={self.project_id}, version={self.version})>"

# Add relationships to other models
from app.models.session import RequirementSession
from app.models.project import Project

RequirementSession.rsd_document = relationship("RSDDocument", back_populates="session", uselist=False)
Project.rsd_documents = relationship("RSDDocument", back_populates="project")