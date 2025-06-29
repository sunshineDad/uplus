"""
Main API router for 一键升级-uplus platform
"""

from fastapi import APIRouter
from app.api.endpoints import projects, sessions, ai_pm

# Create main API router
api_router = APIRouter()

# Include endpoint routers
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
api_router.include_router(ai_pm.router, prefix="/ai-pm", tags=["ai-pm"])