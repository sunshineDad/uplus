"""
Advanced AI Service implementing the 一键升级-uplus vision
Revolutionary AI-native software engineering platform
"""

import litellm
from typing import Dict, List, Any, Optional
import json
import asyncio
import re
from datetime import datetime
from app.core.config import settings

class AIService:
    """
    Advanced AI service implementing the revolutionary 一键升级-uplus methodology
    
    This service embodies the platform's core thesis:
    "From human-written code to AI-materialized intent"
    """
    
    def __init__(self):
        # Configure LiteLLM with enhanced settings
        import os
        os.environ["OPENAI_API_KEY"] = settings.DEEPSEEK_API_KEY
        os.environ["OPENAI_API_BASE"] = settings.LITELLM_API_BASE
        
        self.model = settings.LITELLM_MODEL
        
        # Advanced AI-PM personality and capabilities
        self.ai_pm_persona = """
        You are the AI Product Manager for 一键升级-uplus, the revolutionary AI-native software engineering platform.
        
        Your mission: Transform vague human desires into precise, executable specifications using Socratic Intelligence.
        
        Core Capabilities:
        1. Multi-modal understanding (voice, sketches, examples, context)
        2. Progressive requirement discovery through intelligent questioning
        3. Mental model building of desired systems
        4. Generation of machine-parseable Requirements Specification Documents (RSD)
        
        Personality Traits:
        - Intellectually curious and deeply analytical
        - Patient but purposeful in questioning
        - Visionary yet practical
        - Empathetic to user needs while maintaining technical precision
        
        Communication Style:
        - Ask progressively deeper questions to uncover hidden requirements
        - Build on previous responses to create comprehensive understanding
        - Use business language, not technical jargon
        - Guide users toward completeness without overwhelming them
        
        Remember: You're not just gathering requirements - you're helping users discover what they truly need.
        """
        
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
        """
        Advanced intent analysis using the 一键升级-uplus methodology
        
        This method implements sophisticated requirement discovery that goes beyond
        simple text analysis to understand the deeper intent and business context.
        """
        
        # Enhanced system prompt with 一键升级-uplus methodology
        system_prompt = f"""
        {self.ai_pm_persona}
        
        TASK: Analyze user input for intelligent requirement discovery
        
        You must analyze the user's input and extract structured information using the 一键升级-uplus methodology:
        
        1. INTENT CLASSIFICATION:
           - functional_requirement: Core features and capabilities
           - non_functional_requirement: Performance, security, usability
           - business_constraint: Budget, timeline, regulatory requirements
           - user_story: User-centered feature descriptions
           - technical_constraint: Technology, platform, integration requirements
           - clarification_needed: User needs to provide more information
        
        2. SEMANTIC ANALYSIS:
           - Extract business entities (users, processes, data, systems)
           - Identify relationships and dependencies
           - Understand success criteria and metrics
           - Detect implicit requirements and assumptions
        
        3. COMPLETENESS ASSESSMENT:
           - Evaluate information completeness (0.0-1.0)
           - Identify critical missing information
           - Prioritize next discovery areas
        
        Return a JSON response with this exact structure:
        {{
            "intent_type": "one of the types above",
            "confidence": 0.0-1.0,
            "semantic_analysis": {{
                "entities": ["list of business entities mentioned"],
                "relationships": ["list of relationships between entities"],
                "success_criteria": ["list of success indicators"],
                "assumptions": ["list of implicit assumptions"]
            }},
            "extracted_info": {{
                "summary": "concise summary of what user wants",
                "key_features": ["list of mentioned features"],
                "user_types": ["list of user types/roles"],
                "business_value": "why this matters to the business",
                "constraints": ["any mentioned constraints"]
            }},
            "completeness_score": 0.0-1.0,
            "missing_info": ["specific information still needed"],
            "follow_up_questions": ["2-3 intelligent Socratic questions"],
            "next_discovery_areas": ["areas to explore next"]
        }}
        
        Be intelligent, insightful, and help users discover what they truly need.
        """
        
        # Prepare context-aware message
        context_summary = self._summarize_context(context)
        conversation_stage = self._determine_conversation_stage(context)
        
        messages = [
            {
                "role": "user", 
                "content": f"""
                CONTEXT SUMMARY: {context_summary}
                CONVERSATION STAGE: {conversation_stage}
                
                USER INPUT: "{user_input}"
                
                Please analyze this input using the 一键升级-uplus methodology and provide structured analysis.
                """
            }
        ]
        
        try:
            response = await self.generate_response(
                messages=messages,
                system_prompt=system_prompt,
                temperature=0.3,
                max_tokens=1500
            )
            
            # Try to parse JSON response
            try:
                analysis = json.loads(response)
                
                # Validate and enhance the analysis
                analysis = self._validate_and_enhance_analysis(analysis, user_input, context)
                
                return analysis
                
            except json.JSONDecodeError:
                # Intelligent fallback with pattern recognition
                return self._create_fallback_analysis(user_input, context)
                
        except Exception as e:
            print(f"Intent analysis error: {e}")
            return self._create_error_analysis(user_input, context)
    
    def _summarize_context(self, context: Dict[str, Any]) -> str:
        """Create intelligent context summary"""
        if not context:
            return "New conversation - no prior context"
        
        summary_parts = []
        
        if "project_type" in context:
            summary_parts.append(f"Project type: {context['project_type']}")
        
        if "key_features" in context:
            features = context["key_features"][:3]  # Top 3 features
            summary_parts.append(f"Key features discussed: {', '.join(features)}")
        
        if "user_types" in context:
            summary_parts.append(f"Target users: {', '.join(context['user_types'])}")
        
        if "constraints" in context:
            summary_parts.append(f"Known constraints: {', '.join(context['constraints'])}")
        
        return "; ".join(summary_parts) if summary_parts else "Basic project context established"
    
    def _determine_conversation_stage(self, context: Dict[str, Any]) -> str:
        """Determine what stage of requirement gathering we're in"""
        if not context:
            return "INITIAL_DISCOVERY"
        
        info_count = len([k for k in context.keys() if context[k]])
        
        if info_count < 3:
            return "INITIAL_DISCOVERY"
        elif info_count < 7:
            return "REQUIREMENT_ELABORATION"
        elif info_count < 12:
            return "DETAIL_REFINEMENT"
        else:
            return "COMPLETION_VALIDATION"
    
    def _validate_and_enhance_analysis(self, analysis: Dict[str, Any], user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and enhance AI analysis with business logic"""
        
        # Ensure required fields exist
        required_fields = ["intent_type", "confidence", "extracted_info", "follow_up_questions"]
        for field in required_fields:
            if field not in analysis:
                analysis[field] = self._get_default_value(field)
        
        # Enhance extracted_info with pattern recognition
        if "extracted_info" in analysis:
            analysis["extracted_info"] = self._enhance_extracted_info(
                analysis["extracted_info"], user_input, context
            )
        
        # Ensure confidence is reasonable
        if analysis.get("confidence", 0) > 0.95:
            analysis["confidence"] = 0.95  # Cap confidence to maintain humility
        
        return analysis
    
    def _enhance_extracted_info(self, extracted_info: Dict[str, Any], user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance extracted information with pattern recognition"""
        
        # Detect common patterns
        if re.search(r'\b(dashboard|analytics|reporting)\b', user_input.lower()):
            extracted_info.setdefault("features", []).append("data_visualization")
        
        if re.search(r'\b(user|customer|client)\b', user_input.lower()):
            extracted_info.setdefault("user_types", []).append("end_users")
        
        if re.search(r'\b(team|collaboration|sharing)\b', user_input.lower()):
            extracted_info.setdefault("features", []).append("collaboration")
        
        if re.search(r'\b(mobile|phone|app)\b', user_input.lower()):
            extracted_info.setdefault("constraints", []).append("mobile_compatibility")
        
        return extracted_info
    
    def _create_fallback_analysis(self, user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create intelligent fallback analysis when AI parsing fails"""
        
        # Basic pattern recognition
        intent_type = "functional_requirement"
        if re.search(r'\b(performance|speed|fast|slow)\b', user_input.lower()):
            intent_type = "non_functional_requirement"
        elif re.search(r'\b(budget|cost|timeline|deadline)\b', user_input.lower()):
            intent_type = "business_constraint"
        
        return {
            "intent_type": intent_type,
            "confidence": 0.6,
            "semantic_analysis": {
                "entities": self._extract_entities(user_input),
                "relationships": [],
                "success_criteria": [],
                "assumptions": []
            },
            "extracted_info": {
                "summary": f"User mentioned: {user_input[:100]}...",
                "key_features": self._extract_features(user_input),
                "user_types": [],
                "business_value": "To be determined",
                "constraints": []
            },
            "completeness_score": 0.4,
            "missing_info": ["More specific details needed", "Business context required"],
            "follow_up_questions": [
                "Could you tell me more about who will be using this system?",
                "What specific problem are you trying to solve?",
                "What would success look like for this project?"
            ],
            "next_discovery_areas": ["user_identification", "problem_definition", "success_criteria"]
        }
    
    def _create_error_analysis(self, user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create error analysis when system fails"""
        return {
            "intent_type": "system_error",
            "confidence": 0.0,
            "semantic_analysis": {"entities": [], "relationships": [], "success_criteria": [], "assumptions": []},
            "extracted_info": {"summary": "System error occurred", "key_features": [], "user_types": [], "business_value": "", "constraints": []},
            "completeness_score": 0.0,
            "missing_info": ["System recovery needed"],
            "follow_up_questions": ["I apologize for the technical difficulty. Could you please rephrase your request?"],
            "next_discovery_areas": ["error_recovery"]
        }
    
    def _extract_entities(self, text: str) -> List[str]:
        """Extract business entities from text using pattern recognition"""
        entities = []
        
        # Common business entities
        patterns = {
            "user": r'\b(user|customer|client|person|people)\b',
            "data": r'\b(data|information|record|file)\b',
            "system": r'\b(system|platform|application|app)\b',
            "process": r'\b(process|workflow|procedure|task)\b'
        }
        
        for entity_type, pattern in patterns.items():
            if re.search(pattern, text.lower()):
                entities.append(entity_type)
        
        return entities
    
    def _extract_features(self, text: str) -> List[str]:
        """Extract potential features from text"""
        features = []
        
        feature_patterns = {
            "authentication": r'\b(login|signin|auth|password)\b',
            "search": r'\b(search|find|filter|query)\b',
            "reporting": r'\b(report|analytics|dashboard|chart)\b',
            "messaging": r'\b(message|chat|notification|email)\b',
            "file_management": r'\b(upload|download|file|document)\b'
        }
        
        for feature, pattern in feature_patterns.items():
            if re.search(pattern, text.lower()):
                features.append(feature)
        
        return features
    
    def _get_default_value(self, field: str) -> Any:
        """Get default values for required fields"""
        defaults = {
            "intent_type": "general",
            "confidence": 0.5,
            "extracted_info": {},
            "follow_up_questions": ["Could you provide more details?"],
            "missing_info": ["More information needed"],
            "completeness_score": 0.3
        }
        return defaults.get(field, None)
    
    async def generate_socratic_questions(
        self, 
        context: Dict[str, Any], 
        conversation_history: List[Dict[str, Any]]
    ) -> List[str]:
        """
        Generate intelligent Socratic questions using the 一键升级-uplus methodology
        
        This method implements advanced requirement discovery through strategic questioning
        that guides users toward complete and actionable specifications.
        """
        
        # Analyze conversation stage and context
        conversation_stage = self._determine_conversation_stage(context)
        missing_areas = self._identify_missing_requirement_areas(context)
        
        # Enhanced system prompt for Socratic questioning
        system_prompt = f"""
        {self.ai_pm_persona}
        
        TASK: Generate intelligent Socratic questions for requirement discovery
        
        CURRENT CONTEXT:
        - Conversation Stage: {conversation_stage}
        - Missing Requirement Areas: {missing_areas}
        
        SOCRATIC QUESTIONING STRATEGY:
        
        1. PROGRESSIVE DISCOVERY:
           - Start with broad understanding, narrow to specifics
           - Build on previous responses to deepen insight
           - Uncover implicit assumptions and hidden requirements
        
        2. QUESTION TYPES BY STAGE:
           
           INITIAL_DISCOVERY:
           - Problem definition and business context
           - User identification and needs
           - Success criteria and value proposition
           
           REQUIREMENT_ELABORATION:
           - Feature prioritization and dependencies
           - User workflows and interactions
           - Technical and business constraints
           
           DETAIL_REFINEMENT:
           - Edge cases and error scenarios
           - Performance and scalability requirements
           - Integration and compatibility needs
           
           COMPLETION_VALIDATION:
           - Requirement completeness verification
           - Assumption validation
           - Implementation readiness assessment
        
        3. QUESTION QUALITY CRITERIA:
           - Open-ended to encourage elaboration
           - Specific enough to elicit actionable information
           - Business-focused, not technical
           - Progressive - each question builds understanding
        
        Generate 2-3 intelligent questions as a JSON array.
        Focus on the most critical missing information for the current stage.
        
        Example format: ["Question 1?", "Question 2?", "Question 3?"]
        """
        
        # Prepare context for AI
        context_analysis = {
            "stage": conversation_stage,
            "missing_areas": missing_areas,
            "context_summary": self._summarize_context(context),
            "interaction_count": len(conversation_history),
            "last_user_input": conversation_history[-1].get("user_message", "") if conversation_history else ""
        }
        
        messages = [
            {
                "role": "user",
                "content": f"""
                CONTEXT ANALYSIS: {json.dumps(context_analysis, indent=2)}
                
                CONVERSATION HISTORY SUMMARY:
                {self._summarize_conversation_history(conversation_history)}
                
                Generate intelligent Socratic questions for the next phase of requirement discovery.
                """
            }
        ]
        
        try:
            response = await self.generate_response(
                messages=messages,
                system_prompt=system_prompt,
                temperature=0.6,
                max_tokens=800
            )
            
            # Try to parse JSON response
            try:
                questions = json.loads(response)
                if isinstance(questions, list) and len(questions) > 0:
                    # Validate and enhance questions
                    return self._validate_and_enhance_questions(questions, conversation_stage, missing_areas)
                else:
                    return self._generate_fallback_questions(conversation_stage, missing_areas)
                    
            except json.JSONDecodeError:
                # Intelligent fallback based on stage
                return self._generate_fallback_questions(conversation_stage, missing_areas)
                
        except Exception as e:
            print(f"Question generation error: {e}")
            return self._generate_emergency_questions()
    
    def _identify_missing_requirement_areas(self, context: Dict[str, Any]) -> List[str]:
        """Identify which requirement areas are missing or incomplete"""
        
        required_areas = [
            "problem_definition",
            "user_identification", 
            "core_features",
            "success_criteria",
            "constraints",
            "user_workflows",
            "business_value",
            "technical_requirements",
            "performance_requirements",
            "security_requirements"
        ]
        
        missing_areas = []
        
        for area in required_areas:
            if not self._is_area_covered(area, context):
                missing_areas.append(area)
        
        return missing_areas
    
    def _is_area_covered(self, area: str, context: Dict[str, Any]) -> bool:
        """Check if a requirement area is adequately covered"""
        
        area_indicators = {
            "problem_definition": ["problem", "challenge", "issue", "need"],
            "user_identification": ["user_types", "users", "customers", "stakeholders"],
            "core_features": ["key_features", "features", "functionality"],
            "success_criteria": ["success_criteria", "metrics", "goals"],
            "constraints": ["constraints", "limitations", "budget", "timeline"],
            "user_workflows": ["workflow", "process", "journey", "interaction"],
            "business_value": ["business_value", "value", "benefit", "roi"],
            "technical_requirements": ["technology", "platform", "integration"],
            "performance_requirements": ["performance", "speed", "scalability"],
            "security_requirements": ["security", "privacy", "compliance"]
        }
        
        indicators = area_indicators.get(area, [])
        
        # Check if any indicators are present in context
        for key, value in context.items():
            if any(indicator in key.lower() for indicator in indicators):
                if value and (isinstance(value, list) and len(value) > 0 or 
                            isinstance(value, str) and len(value) > 0):
                    return True
        
        return False
    
    def _summarize_conversation_history(self, conversation_history: List[Dict[str, Any]]) -> str:
        """Create a concise summary of the conversation history"""
        
        if not conversation_history:
            return "No previous conversation"
        
        summary_parts = []
        
        for i, entry in enumerate(conversation_history[-3:], 1):  # Last 3 interactions
            user_msg = entry.get("user_message", "")[:100]
            intent = entry.get("intent_analysis", {}).get("intent_type", "unknown")
            summary_parts.append(f"{i}. User: {user_msg}... (Intent: {intent})")
        
        return "\n".join(summary_parts)
    
    def _validate_and_enhance_questions(self, questions: List[str], stage: str, missing_areas: List[str]) -> List[str]:
        """Validate and enhance generated questions"""
        
        enhanced_questions = []
        
        for question in questions[:3]:  # Limit to 3 questions
            # Ensure question ends with question mark
            if not question.strip().endswith('?'):
                question = question.strip() + '?'
            
            # Ensure question is not too short or too long
            if 10 <= len(question) <= 200:
                enhanced_questions.append(question)
        
        # If we don't have enough good questions, add fallbacks
        while len(enhanced_questions) < 2:
            fallback = self._get_stage_specific_question(stage, missing_areas, len(enhanced_questions))
            if fallback not in enhanced_questions:
                enhanced_questions.append(fallback)
        
        return enhanced_questions
    
    def _generate_fallback_questions(self, stage: str, missing_areas: List[str]) -> List[str]:
        """Generate intelligent fallback questions based on stage and missing areas"""
        
        questions = []
        
        # Add stage-specific questions
        for i in range(3):
            question = self._get_stage_specific_question(stage, missing_areas, i)
            if question not in questions:
                questions.append(question)
        
        return questions[:3]
    
    def _get_stage_specific_question(self, stage: str, missing_areas: List[str], index: int) -> str:
        """Get stage-specific questions based on missing areas"""
        
        stage_questions = {
            "INITIAL_DISCOVERY": [
                "What specific problem or challenge are you trying to solve with this system?",
                "Who are the main users or stakeholders who will benefit from this solution?",
                "What would success look like for this project from a business perspective?"
            ],
            "REQUIREMENT_ELABORATION": [
                "Which features would be most critical for your users' daily workflows?",
                "Are there any existing systems or processes this solution needs to integrate with?",
                "What constraints should we consider - budget, timeline, or technical limitations?"
            ],
            "DETAIL_REFINEMENT": [
                "How do you envision users navigating through the main workflows?",
                "What performance expectations do you have for response times and system load?",
                "Are there any compliance or security requirements we need to address?"
            ],
            "COMPLETION_VALIDATION": [
                "Looking at everything we've discussed, what feels most important to validate or clarify?",
                "Are there any edge cases or unusual scenarios we should plan for?",
                "What would make you confident this solution will meet your needs?"
            ]
        }
        
        questions = stage_questions.get(stage, stage_questions["INITIAL_DISCOVERY"])
        return questions[index % len(questions)]
    
    def _generate_emergency_questions(self) -> List[str]:
        """Generate emergency fallback questions when all else fails"""
        return [
            "Could you tell me more about what you're trying to achieve?",
            "What's the most important aspect of this project for you?",
            "How can I help you move forward with your requirements?"
        ]
    
    async def generate_rsd(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate comprehensive Requirements Specification Document using 一键升级-uplus methodology
        
        This method creates a complete, machine-parseable RSD that captures 100% of user intent
        and serves as the foundation for BITCUP model generation.
        """
        
        # Analyze conversation completeness and extract key insights
        conversation_analysis = self._analyze_conversation_completeness(context, conversation_history)
        
        # Enhanced system prompt for RSD generation
        system_prompt = f"""
        {self.ai_pm_persona}
        
        TASK: Generate a comprehensive Requirements Specification Document (RSD)
        
        You are creating the definitive specification that will be used to generate BITCUP models
        and ultimately materialize the user's vision into a working system.
        
        CRITICAL SUCCESS FACTOR: The RSD must capture 100% of user intent. This is non-negotiable.
        
        RSD STRUCTURE (JSON format):
        {{
            "project_overview": {{
                "name": "Project name",
                "description": "Comprehensive project description",
                "business_context": "Why this project matters",
                "success_vision": "What success looks like"
            }},
            "stakeholders": {{
                "primary_users": ["List of primary user types"],
                "secondary_users": ["List of secondary user types"],
                "stakeholders": ["List of business stakeholders"],
                "decision_makers": ["List of decision makers"]
            }},
            "functional_requirements": {{
                "user_stories": [
                    {{
                        "id": "US001",
                        "role": "user role",
                        "goal": "what they want to do",
                        "benefit": "why they want it",
                        "acceptance_criteria": ["list of criteria"],
                        "priority": "High/Medium/Low"
                    }}
                ],
                "use_cases": [
                    {{
                        "id": "UC001",
                        "name": "Use case name",
                        "description": "Detailed description",
                        "actors": ["List of actors"],
                        "preconditions": ["List of preconditions"],
                        "main_flow": ["Step-by-step main flow"],
                        "alternative_flows": ["Alternative scenarios"],
                        "postconditions": ["Expected outcomes"]
                    }}
                ],
                "business_rules": [
                    {{
                        "id": "BR001",
                        "rule": "Business rule description",
                        "rationale": "Why this rule exists",
                        "impact": "What happens if violated"
                    }}
                ],
                "feature_requirements": [
                    {{
                        "feature": "Feature name",
                        "description": "Detailed description",
                        "priority": "High/Medium/Low",
                        "dependencies": ["List of dependencies"],
                        "acceptance_criteria": ["List of criteria"]
                    }}
                ]
            }},
            "non_functional_requirements": {{
                "performance": {{
                    "response_time": "Maximum acceptable response time",
                    "throughput": "Expected transaction volume",
                    "concurrent_users": "Number of simultaneous users",
                    "availability": "Uptime requirements"
                }},
                "security": {{
                    "authentication": "Authentication requirements",
                    "authorization": "Access control requirements",
                    "data_protection": "Data security requirements",
                    "compliance": "Regulatory compliance needs"
                }},
                "usability": {{
                    "user_experience": "UX requirements",
                    "accessibility": "Accessibility standards",
                    "learning_curve": "Training requirements",
                    "error_handling": "Error management approach"
                }},
                "reliability": {{
                    "error_rate": "Acceptable error rate",
                    "recovery_time": "Disaster recovery requirements",
                    "data_integrity": "Data consistency requirements",
                    "backup_requirements": "Backup and restore needs"
                }},
                "scalability": {{
                    "user_growth": "Expected user growth",
                    "data_growth": "Expected data volume growth",
                    "geographic_expansion": "Multi-region requirements",
                    "feature_expansion": "Future feature considerations"
                }}
            }},
            "constraints": {{
                "technical": [
                    {{
                        "constraint": "Technical limitation",
                        "description": "Detailed explanation",
                        "impact": "How it affects the solution",
                        "mitigation": "How to work around it"
                    }}
                ],
                "business": [
                    {{
                        "constraint": "Business limitation",
                        "description": "Detailed explanation",
                        "impact": "How it affects the project",
                        "mitigation": "How to manage it"
                    }}
                ],
                "regulatory": [
                    {{
                        "regulation": "Regulatory requirement",
                        "description": "What must be complied with",
                        "impact": "How it affects the solution",
                        "compliance_approach": "How to ensure compliance"
                    }}
                ],
                "timeline": {{
                    "project_deadline": "Overall project deadline",
                    "milestone_deadlines": ["Key milestone dates"],
                    "critical_path": "Most time-sensitive requirements"
                }},
                "budget": {{
                    "total_budget": "Overall budget constraint",
                    "budget_breakdown": "How budget is allocated",
                    "cost_priorities": "What to prioritize if budget is tight"
                }}
            }},
            "success_criteria": {{
                "business_metrics": [
                    {{
                        "metric": "Business metric name",
                        "target": "Target value",
                        "measurement": "How to measure",
                        "timeline": "When to achieve"
                    }}
                ],
                "user_metrics": [
                    {{
                        "metric": "User satisfaction metric",
                        "target": "Target value",
                        "measurement": "How to measure",
                        "timeline": "When to achieve"
                    }}
                ],
                "technical_metrics": [
                    {{
                        "metric": "Technical metric name",
                        "target": "Target value",
                        "measurement": "How to measure",
                        "timeline": "When to achieve"
                    }}
                ],
                "acceptance_tests": [
                    {{
                        "test": "Acceptance test description",
                        "criteria": "Pass/fail criteria",
                        "priority": "High/Medium/Low"
                    }}
                ]
            }},
            "assumptions": [
                {{
                    "assumption": "What we're assuming",
                    "rationale": "Why we're making this assumption",
                    "risk": "What happens if assumption is wrong",
                    "validation": "How to validate this assumption"
                }}
            ],
            "risks": [
                {{
                    "risk": "Risk description",
                    "probability": "High/Medium/Low",
                    "impact": "High/Medium/Low",
                    "mitigation": "How to mitigate",
                    "contingency": "Backup plan"
                }}
            ],
            "integration_requirements": [
                {{
                    "system": "External system name",
                    "type": "Type of integration",
                    "data_exchange": "What data is exchanged",
                    "frequency": "How often",
                    "requirements": "Specific integration requirements"
                }}
            ]
        }}
        
        ANALYSIS CONTEXT:
        - Conversation Completeness: {conversation_analysis['completeness_score']:.1%}
        - Missing Areas: {conversation_analysis['missing_areas']}
        - Key Insights: {conversation_analysis['key_insights']}
        
        Generate a comprehensive RSD that captures all discussed requirements and fills in reasonable
        defaults for any missing areas based on industry best practices.
        """
        
        # Prepare comprehensive context for AI
        rsd_context = {
            "conversation_analysis": conversation_analysis,
            "context_summary": self._create_detailed_context_summary(context),
            "conversation_insights": self._extract_conversation_insights(conversation_history),
            "requirement_coverage": self._assess_requirement_coverage(context, conversation_history)
        }
        
        messages = [
            {
                "role": "user",
                "content": f"""
                RSD GENERATION CONTEXT:
                {json.dumps(rsd_context, indent=2)}
                
                CONVERSATION HISTORY ANALYSIS:
                {self._create_detailed_conversation_analysis(conversation_history)}
                
                Generate a comprehensive Requirements Specification Document that captures
                100% of the user's intent and provides a complete foundation for system development.
                """
            }
        ]
        
        try:
            response = await self.generate_response(
                messages=messages,
                system_prompt=system_prompt,
                temperature=0.2,
                max_tokens=4000
            )
            
            # Try to parse JSON response
            try:
                rsd = json.loads(response)
                
                # Validate and enhance the RSD
                rsd = self._validate_and_enhance_rsd(rsd, context, conversation_history)
                
                return rsd
                
            except json.JSONDecodeError:
                # Create intelligent fallback RSD
                return self._create_comprehensive_fallback_rsd(context, conversation_history)
                
        except Exception as e:
            print(f"RSD generation error: {e}")
            return self._create_error_rsd(context, conversation_history)
    
    def _analyze_conversation_completeness(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze how complete the conversation is for RSD generation"""
        
        required_areas = [
            "problem_definition", "user_identification", "core_features", "success_criteria",
            "constraints", "user_workflows", "business_value", "technical_requirements"
        ]
        
        covered_areas = []
        missing_areas = []
        
        for area in required_areas:
            if self._is_area_covered(area, context):
                covered_areas.append(area)
            else:
                missing_areas.append(area)
        
        completeness_score = len(covered_areas) / len(required_areas)
        
        # Extract key insights from conversation
        key_insights = self._extract_key_insights(context, conversation_history)
        
        return {
            "completeness_score": completeness_score,
            "covered_areas": covered_areas,
            "missing_areas": missing_areas,
            "key_insights": key_insights,
            "conversation_depth": len(conversation_history),
            "readiness_for_rsd": completeness_score >= 0.7
        }
    
    def _extract_key_insights(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> List[str]:
        """Extract key insights from the conversation"""
        
        insights = []
        
        # Analyze context for insights
        if context.get("key_features"):
            insights.append(f"Core features identified: {', '.join(context['key_features'][:3])}")
        
        if context.get("user_types"):
            insights.append(f"Target users: {', '.join(context['user_types'])}")
        
        if context.get("business_value"):
            insights.append(f"Business value: {context['business_value']}")
        
        # Analyze conversation patterns
        if len(conversation_history) > 5:
            insights.append("Detailed requirements discussion conducted")
        
        # Look for specific patterns in conversation
        for entry in conversation_history:
            intent = entry.get("intent_analysis", {}).get("intent_type", "")
            if intent == "business_constraint":
                insights.append("Business constraints identified")
            elif intent == "technical_constraint":
                insights.append("Technical constraints discussed")
        
        return insights
    
    def _create_detailed_context_summary(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Create a detailed summary of the context for RSD generation"""
        
        return {
            "project_type": context.get("project_type", "Not specified"),
            "key_features": context.get("key_features", []),
            "user_types": context.get("user_types", []),
            "constraints": context.get("constraints", []),
            "business_value": context.get("business_value", "Not specified"),
            "success_criteria": context.get("success_criteria", []),
            "technical_requirements": context.get("technical_requirements", []),
            "context_richness": len([v for v in context.values() if v])
        }
    
    def _extract_conversation_insights(self, conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract insights from conversation history"""
        
        insights = {
            "total_interactions": len(conversation_history),
            "intent_distribution": {},
            "key_topics": [],
            "user_engagement": "high" if len(conversation_history) > 5 else "medium"
        }
        
        # Analyze intent distribution
        for entry in conversation_history:
            intent = entry.get("intent_analysis", {}).get("intent_type", "unknown")
            insights["intent_distribution"][intent] = insights["intent_distribution"].get(intent, 0) + 1
        
        return insights
    
    def _assess_requirement_coverage(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, float]:
        """Assess how well different requirement areas are covered"""
        
        coverage = {}
        
        requirement_areas = [
            "functional_requirements", "non_functional_requirements", 
            "constraints", "success_criteria", "stakeholders"
        ]
        
        for area in requirement_areas:
            coverage[area] = self._calculate_area_coverage(area, context, conversation_history)
        
        return coverage
    
    def _calculate_area_coverage(self, area: str, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> float:
        """Calculate coverage score for a specific requirement area"""
        
        # This is a simplified calculation - in a real implementation,
        # this would be more sophisticated
        
        area_keywords = {
            "functional_requirements": ["feature", "function", "capability", "user story"],
            "non_functional_requirements": ["performance", "security", "usability", "reliability"],
            "constraints": ["constraint", "limitation", "budget", "timeline"],
            "success_criteria": ["success", "metric", "goal", "measure"],
            "stakeholders": ["user", "stakeholder", "customer", "admin"]
        }
        
        keywords = area_keywords.get(area, [])
        coverage_score = 0.0
        
        # Check context
        for key, value in context.items():
            if any(keyword in key.lower() for keyword in keywords):
                if value:
                    coverage_score += 0.3
        
        # Check conversation history
        for entry in conversation_history:
            user_msg = entry.get("user_message", "").lower()
            if any(keyword in user_msg for keyword in keywords):
                coverage_score += 0.1
        
        return min(coverage_score, 1.0)
    
    def _create_detailed_conversation_analysis(self, conversation_history: List[Dict[str, Any]]) -> str:
        """Create detailed analysis of conversation history"""
        
        if not conversation_history:
            return "No conversation history available"
        
        analysis_parts = []
        
        analysis_parts.append(f"Total Interactions: {len(conversation_history)}")
        
        # Analyze intent patterns
        intents = [entry.get("intent_analysis", {}).get("intent_type", "unknown") 
                  for entry in conversation_history]
        intent_counts = {}
        for intent in intents:
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        analysis_parts.append(f"Intent Distribution: {intent_counts}")
        
        # Extract key user statements
        key_statements = []
        for entry in conversation_history[-3:]:  # Last 3 interactions
            user_msg = entry.get("user_message", "")
            if len(user_msg) > 20:  # Only meaningful statements
                key_statements.append(user_msg[:150] + "..." if len(user_msg) > 150 else user_msg)
        
        if key_statements:
            analysis_parts.append("Recent Key Statements:")
            for i, statement in enumerate(key_statements, 1):
                analysis_parts.append(f"  {i}. {statement}")
        
        return "\n".join(analysis_parts)
    
    def _validate_and_enhance_rsd(self, rsd: Dict[str, Any], context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate and enhance the generated RSD"""
        
        # Ensure all required sections exist
        required_sections = [
            "project_overview", "stakeholders", "functional_requirements",
            "non_functional_requirements", "constraints", "success_criteria"
        ]
        
        for section in required_sections:
            if section not in rsd:
                rsd[section] = self._get_default_rsd_section(section)
        
        # Add metadata
        rsd["metadata"] = {
            "generated_at": datetime.now().isoformat(),
            "conversation_interactions": len(conversation_history),
            "context_richness": len([v for v in context.values() if v]),
            "generation_method": "一键升级-uplus AI-PM",
            "version": "1.0"
        }
        
        return rsd
    
    def _create_comprehensive_fallback_rsd(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create a comprehensive fallback RSD when AI generation fails"""
        
        # Extract what we can from context and conversation
        project_name = context.get("project_type", "Software Project")
        features = context.get("key_features", ["Core functionality"])
        users = context.get("user_types", ["End users"])
        
        return {
            "project_overview": {
                "name": project_name,
                "description": f"A {project_name.lower()} designed to meet user needs",
                "business_context": "Addresses identified business requirements",
                "success_vision": "Delivers value to users and stakeholders"
            },
            "stakeholders": {
                "primary_users": users,
                "secondary_users": ["System administrators"],
                "stakeholders": ["Business stakeholders"],
                "decision_makers": ["Project sponsors"]
            },
            "functional_requirements": {
                "user_stories": [
                    {
                        "id": "US001",
                        "role": "user",
                        "goal": f"use {feature}",
                        "benefit": "accomplish my tasks efficiently",
                        "acceptance_criteria": ["Feature works as expected"],
                        "priority": "High"
                    } for feature in features[:5]
                ],
                "use_cases": [
                    {
                        "id": "UC001",
                        "name": "Basic System Usage",
                        "description": "User interacts with the system",
                        "actors": users,
                        "preconditions": ["User is authenticated"],
                        "main_flow": ["User accesses system", "User performs actions", "System responds"],
                        "alternative_flows": ["Error handling"],
                        "postconditions": ["Task completed successfully"]
                    }
                ],
                "business_rules": [
                    {
                        "id": "BR001",
                        "rule": "System must maintain data integrity",
                        "rationale": "Ensure reliable operations",
                        "impact": "System failure if violated"
                    }
                ],
                "feature_requirements": [
                    {
                        "feature": feature,
                        "description": f"Implementation of {feature}",
                        "priority": "High",
                        "dependencies": [],
                        "acceptance_criteria": ["Feature functions correctly"]
                    } for feature in features
                ]
            },
            "non_functional_requirements": {
                "performance": {
                    "response_time": "< 2 seconds",
                    "throughput": "100 concurrent users",
                    "concurrent_users": "100",
                    "availability": "99.9%"
                },
                "security": {
                    "authentication": "Required for all users",
                    "authorization": "Role-based access control",
                    "data_protection": "Encryption at rest and in transit",
                    "compliance": "Industry standard compliance"
                },
                "usability": {
                    "user_experience": "Intuitive and user-friendly",
                    "accessibility": "WCAG 2.1 AA compliance",
                    "learning_curve": "Minimal training required",
                    "error_handling": "Clear error messages and recovery"
                },
                "reliability": {
                    "error_rate": "< 0.1%",
                    "recovery_time": "< 1 hour",
                    "data_integrity": "100% data consistency",
                    "backup_requirements": "Daily automated backups"
                },
                "scalability": {
                    "user_growth": "Support 10x user growth",
                    "data_growth": "Handle increasing data volumes",
                    "geographic_expansion": "Multi-region support",
                    "feature_expansion": "Modular architecture for new features"
                }
            },
            "constraints": {
                "technical": [
                    {
                        "constraint": "Web-based application",
                        "description": "Must run in web browsers",
                        "impact": "Limits to web technologies",
                        "mitigation": "Use modern web standards"
                    }
                ],
                "business": [
                    {
                        "constraint": "Budget limitations",
                        "description": "Project has budget constraints",
                        "impact": "May limit scope or timeline",
                        "mitigation": "Prioritize core features"
                    }
                ],
                "regulatory": [
                    {
                        "regulation": "Data protection",
                        "description": "Must comply with data protection laws",
                        "impact": "Affects data handling",
                        "compliance_approach": "Implement privacy by design"
                    }
                ],
                "timeline": {
                    "project_deadline": "To be determined",
                    "milestone_deadlines": ["Phase 1: Core features", "Phase 2: Advanced features"],
                    "critical_path": "Core functionality development"
                },
                "budget": {
                    "total_budget": "To be determined",
                    "budget_breakdown": "Development, testing, deployment",
                    "cost_priorities": "Core features first"
                }
            },
            "success_criteria": {
                "business_metrics": [
                    {
                        "metric": "User adoption rate",
                        "target": "> 80%",
                        "measurement": "Active users / Total users",
                        "timeline": "3 months post-launch"
                    }
                ],
                "user_metrics": [
                    {
                        "metric": "User satisfaction",
                        "target": "> 4.0/5.0",
                        "measurement": "User surveys",
                        "timeline": "Ongoing"
                    }
                ],
                "technical_metrics": [
                    {
                        "metric": "System uptime",
                        "target": "> 99.9%",
                        "measurement": "Monitoring tools",
                        "timeline": "Ongoing"
                    }
                ],
                "acceptance_tests": [
                    {
                        "test": "All core features functional",
                        "criteria": "100% of core features pass testing",
                        "priority": "High"
                    }
                ]
            },
            "assumptions": [
                {
                    "assumption": "Users have basic computer skills",
                    "rationale": "Standard assumption for software projects",
                    "risk": "May need additional training",
                    "validation": "User research and testing"
                }
            ],
            "risks": [
                {
                    "risk": "Technical complexity",
                    "probability": "Medium",
                    "impact": "Medium",
                    "mitigation": "Iterative development approach",
                    "contingency": "Simplify features if needed"
                }
            ],
            "integration_requirements": [
                {
                    "system": "To be determined",
                    "type": "API integration",
                    "data_exchange": "Standard data formats",
                    "frequency": "Real-time",
                    "requirements": "RESTful API support"
                }
            ],
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "conversation_interactions": len(conversation_history),
                "context_richness": len([v for v in context.values() if v]),
                "generation_method": "一键升级-uplus AI-PM Fallback",
                "version": "1.0"
            }
        }
    
    def _create_error_rsd(self, context: Dict[str, Any], conversation_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create error RSD when generation fails"""
        return {
            "error": "Failed to generate RSD",
            "message": "System encountered an error during RSD generation",
            "context_available": bool(context),
            "conversation_length": len(conversation_history),
            "timestamp": datetime.now().isoformat()
        }
    
    def _get_default_rsd_section(self, section: str) -> Dict[str, Any]:
        """Get default content for RSD sections"""
        
        defaults = {
            "project_overview": {
                "name": "Software Project",
                "description": "Project description to be defined",
                "business_context": "Business context to be defined",
                "success_vision": "Success vision to be defined"
            },
            "stakeholders": {
                "primary_users": ["End users"],
                "secondary_users": ["System administrators"],
                "stakeholders": ["Business stakeholders"],
                "decision_makers": ["Project sponsors"]
            },
            "functional_requirements": {
                "user_stories": [],
                "use_cases": [],
                "business_rules": [],
                "feature_requirements": []
            },
            "non_functional_requirements": {
                "performance": {},
                "security": {},
                "usability": {},
                "reliability": {},
                "scalability": {}
            },
            "constraints": {
                "technical": [],
                "business": [],
                "regulatory": [],
                "timeline": {},
                "budget": {}
            },
            "success_criteria": {
                "business_metrics": [],
                "user_metrics": [],
                "technical_metrics": [],
                "acceptance_tests": []
            }
        }
        
        return defaults.get(section, {})

# Global AI service instance
ai_service = AIService()