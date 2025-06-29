"""
AI Service using LiteLLM for scalable AI integration
"""

import litellm
from typing import Dict, List, Any, Optional
import json
import asyncio
from app.core.config import settings

class AIService:
    """AI service for intelligent requirement gathering and processing"""
    
    def __init__(self):
        # Configure LiteLLM with DeepSeek (OpenAI-compatible)
        import os
        os.environ["OPENAI_API_KEY"] = settings.DEEPSEEK_API_KEY
        os.environ["OPENAI_API_BASE"] = settings.LITELLM_API_BASE
        
        self.model = settings.LITELLM_MODEL
        
    async def generate_response(
        self, 
        messages: List[Dict[str, str]], 
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """Generate AI response using LiteLLM"""
        try:
            # Prepare messages
            formatted_messages = []
            
            if system_prompt:
                formatted_messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            formatted_messages.extend(messages)
            
            # Generate response using LiteLLM
            response = await litellm.acompletion(
                model=self.model,
                messages=formatted_messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"AI Service Error: {e}")
            return "I apologize, but I'm experiencing technical difficulties. Please try again."
    
    async def analyze_intent(self, user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze user intent for requirement gathering"""
        
        system_prompt = """You are an expert AI Product Manager for the 一键升级-uplus platform. 
        Your role is to analyze user input and extract structured information for requirement gathering.
        
        Analyze the user's input and return a JSON response with:
        1. intent_type: The type of requirement (functional, non-functional, constraint, etc.)
        2. confidence: Confidence score (0.0-1.0)
        3. extracted_info: Key information extracted
        4. missing_info: What additional information is needed
        5. follow_up_questions: Intelligent questions to ask next
        
        Be conversational, intelligent, and help users articulate their vision clearly."""
        
        messages = [
            {
                "role": "user", 
                "content": f"Context: {json.dumps(context)}\n\nUser Input: {user_input}\n\nPlease analyze this input and provide structured analysis."
            }
        ]
        
        try:
            response = await self.generate_response(
                messages=messages,
                system_prompt=system_prompt,
                temperature=0.3
            )
            
            # Try to parse JSON response
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                # Fallback if JSON parsing fails
                return {
                    "intent_type": "general",
                    "confidence": 0.5,
                    "extracted_info": {"raw_input": user_input},
                    "missing_info": ["More specific details needed"],
                    "follow_up_questions": ["Could you provide more details about your requirements?"]
                }
                
        except Exception as e:
            print(f"Intent analysis error: {e}")
            return {
                "intent_type": "error",
                "confidence": 0.0,
                "extracted_info": {},
                "missing_info": ["System error occurred"],
                "follow_up_questions": ["Let's try again. What would you like to build?"]
            }
    
    async def generate_socratic_questions(
        self, 
        context: Dict[str, Any], 
        conversation_history: List[Dict[str, Any]]
    ) -> List[str]:
        """Generate intelligent Socratic questions for requirement discovery"""
        
        system_prompt = """You are a master AI Product Manager using the Socratic method to discover requirements.
        
        Your goal is to help users articulate their complete vision through intelligent questioning.
        Generate 2-3 thoughtful questions that:
        1. Uncover hidden requirements
        2. Clarify ambiguous statements
        3. Explore edge cases and constraints
        4. Guide toward completeness
        
        Be conversational, insightful, and help users think deeper about their needs.
        Return only a JSON array of questions."""
        
        messages = [
            {
                "role": "user",
                "content": f"Context: {json.dumps(context)}\n\nConversation History: {json.dumps(conversation_history)}\n\nGenerate intelligent follow-up questions."
            }
        ]
        
        try:
            response = await self.generate_response(
                messages=messages,
                system_prompt=system_prompt,
                temperature=0.6
            )
            
            # Try to parse JSON response
            try:
                questions = json.loads(response)
                return questions if isinstance(questions, list) else [response]
            except json.JSONDecodeError:
                # Fallback questions
                return [
                    "What specific features are most important to your users?",
                    "Are there any constraints or limitations we should consider?",
                    "How do you envision users interacting with this system?"
                ]
                
        except Exception as e:
            print(f"Question generation error: {e}")
            return ["What would you like to focus on next?"]
    
    async def generate_rsd(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate Requirements Specification Document from conversation"""
        
        system_prompt = """You are an expert AI Product Manager creating a comprehensive Requirements Specification Document (RSD).
        
        Based on the conversation context and history, generate a complete RSD with:
        1. functional_requirements: User stories, use cases, business rules
        2. non_functional_requirements: Performance, security, usability, reliability
        3. constraints: Technical, business, regulatory constraints
        4. success_criteria: Metrics and acceptance tests
        
        Return a well-structured JSON document that captures all requirements comprehensively."""
        
        messages = [
            {
                "role": "user",
                "content": f"Context: {json.dumps(context)}\n\nConversation History: {json.dumps(conversation_history)}\n\nGenerate a comprehensive RSD document."
            }
        ]
        
        try:
            response = await self.generate_response(
                messages=messages,
                system_prompt=system_prompt,
                temperature=0.2,
                max_tokens=2000
            )
            
            # Try to parse JSON response
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                # Fallback RSD structure
                return {
                    "functional_requirements": {
                        "user_stories": ["As a user, I want to use the system"],
                        "use_cases": ["Basic system usage"],
                        "business_rules": ["Standard business logic"]
                    },
                    "non_functional_requirements": {
                        "performance": {"response_time": "< 2 seconds"},
                        "security": {"authentication": "Required"},
                        "usability": {"user_friendly": "High priority"}
                    },
                    "constraints": {
                        "technical": ["Web-based application"],
                        "business": ["Budget constraints"],
                        "regulatory": ["Data protection compliance"]
                    },
                    "success_criteria": {
                        "metrics": ["User satisfaction > 4.0/5"],
                        "acceptance_tests": ["All features functional"]
                    }
                }
                
        except Exception as e:
            print(f"RSD generation error: {e}")
            return {"error": "Failed to generate RSD"}

# Global AI service instance
ai_service = AIService()