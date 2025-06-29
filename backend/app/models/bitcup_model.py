"""
BITCUP Model for semantic modeling
"""

from sqlalchemy import Column, String, DateTime, Text, ForeignKey, JSON, Float, Integer, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
import enum
from app.core.database import Base

class ModelStatus(str, enum.Enum):
    """BITCUP model status enumeration"""
    GENERATING = "generating"
    VALIDATING = "validating"
    VALID = "valid"
    INVALID = "invalid"
    OPTIMIZING = "optimizing"
    READY = "ready"

class BitcupModel(Base):
    """BITCUP semantic model"""
    
    __tablename__ = "bitcup_models"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    rsd_id = Column(String(36), ForeignKey("rsd_documents.id"), nullable=False)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)
    
    # Model Content
    entities = Column(JSON, default=list)
    behaviors = Column(JSON, default=list)
    flows = Column(JSON, default=list)
    views = Column(JSON, default=list)
    events = Column(JSON, default=list)
    rules = Column(JSON, default=list)
    
    # Model Metadata
    status = Column(Enum(ModelStatus), default=ModelStatus.GENERATING)
    version = Column(Integer, default=1)
    validation_results = Column(JSON, default=dict)
    optimization_results = Column(JSON, default=dict)
    quality_score = Column(Float, default=0.0)
    
    # Generation Metadata
    generation_metadata = Column(JSON, default=dict)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    rsd_document = relationship("RSDDocument", back_populates="bitcup_model")
    project = relationship("Project", back_populates="bitcup_models")
    
    def __repr__(self):
        return f"<BitcupModel(id={self.id}, project_id={self.project_id}, status={self.status})>"

# Add relationships to other models
from app.models.rsd import RSDDocument
from app.models.project import Project

RSDDocument.bitcup_model = relationship("BitcupModel", back_populates="rsd_document", uselist=False)
Project.bitcup_models = relationship("BitcupModel", back_populates="project")