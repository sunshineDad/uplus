"""
Models for AI Low-Code Platform
"""

from sqlalchemy import Column, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.core.database import Base
import uuid

# Import models for relationships
from app.models.bitcup_model import BitcupModel

class GeneratedCode(Base):
    """
    Model for storing generated code from BITCUP models
    """
    
    __tablename__ = "generated_code"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    bitcup_id = Column(String, ForeignKey("bitcup_models.id"))
    tech_stack = Column(JSON, nullable=False)
    frontend_code = Column(JSON, nullable=False)
    backend_code = Column(JSON, nullable=False)
    database_code = Column(JSON, nullable=False)
    deployment_config = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    bitcup_model = relationship("BitcupModel", back_populates="generated_code")
    deployments = relationship("Deployment", back_populates="generated_code")

class Deployment(Base):
    """
    Model for storing deployment information
    """
    
    __tablename__ = "deployments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    code_id = Column(String, ForeignKey("generated_code.id"))
    environment = Column(String, nullable=False)
    status = Column(String, nullable=False)
    url = Column(String, nullable=True)
    deployed_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    generated_code = relationship("GeneratedCode", back_populates="deployments")