"""
Configuration settings for 一键升级-uplus platform
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # Application
    APP_NAME: str = "一键升级-uplus"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "sqlite:///./uplus.db"  # Default to SQLite for development
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://localhost:8080"]
    
    # AI Configuration
    DEEPSEEK_API_KEY: str = "sk-46ac4ed1f2144dd4844876880e5c3eca"
    LITELLM_MODEL: str = "openai/deepseek-chat"
    LITELLM_API_BASE: str = "https://api.deepseek.com/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()