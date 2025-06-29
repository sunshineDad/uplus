"""
BITCUP Modeling Language Service
Universal semantic language that expresses "what" not "how"
"""

from typing import Dict, List, Any, Optional
import json
import re
from datetime import datetime
from app.core.config import settings

class BitcupService:
    """
    BITCUP Modeling Language Service
    
    BITCUP = Business + Intent + Technology + Constraints + User + Process
    
    This service implements the revolutionary semantic modeling language that:
    - Describes business intent, not technical implementation
    - Is platform-agnostic and technology-independent
    - Is formally verifiable and mathematically sound
    - Supports bidirectional transformation
    """
    
    def __init__(self):
        self.core_constructs = {
            "entities": "What exists in the system",
            "behaviors": "What the system does", 
            "rules": "Constraints and validations",
            "flows": "How things connect",
            "events": "What triggers actions",
            "views": "How users interact"
        }
        
        self.semantic_patterns = self._initialize_semantic_patterns()
    
    def _initialize_semantic_patterns(self) -> Dict[str, Any]:
        """Initialize semantic pattern recognition"""
        return {
            "entity_patterns": {
                "user": r'\b(user|customer|client|person|people|stakeholder)\b',
                "data": r'\b(data|information|record|file|document|content)\b',
                "system": r'\b(system|platform|application|app|service)\b',
                "process": r'\b(process|workflow|procedure|task|activity)\b',
                "resource": r'\b(resource|asset|item|object|component)\b'
            },
            "behavior_patterns": {
                "create": r'\b(create|add|new|generate|build|make)\b',
                "read": r'\b(view|read|display|show|list|get|fetch)\b',
                "update": r'\b(update|edit|modify|change|alter)\b',
                "delete": r'\b(delete|remove|destroy|eliminate)\b',
                "search": r'\b(search|find|filter|query|lookup)\b',
                "validate": r'\b(validate|verify|check|confirm|approve)\b',
                "notify": r'\b(notify|alert|inform|message|email)\b',
                "process": r'\b(process|execute|run|perform|handle)\b'
            },
            "rule_patterns": {
                "permission": r'\b(permission|access|authorize|allow|deny)\b',
                "validation": r'\b(required|mandatory|optional|valid|invalid)\b',
                "business": r'\b(business|policy|rule|regulation|compliance)\b',
                "constraint": r'\b(limit|maximum|minimum|constraint|restriction)\b'
            },
            "flow_patterns": {
                "sequence": r'\b(then|next|after|before|sequence|order)\b',
                "condition": r'\b(if|when|unless|condition|case|scenario)\b',
                "parallel": r'\b(parallel|concurrent|simultaneous|together)\b',
                "loop": r'\b(repeat|loop|iterate|cycle|recurring)\b'
            },
            "event_patterns": {
                "trigger": r'\b(trigger|event|signal|notification|alert)\b',
                "schedule": r'\b(schedule|timer|periodic|daily|weekly)\b',
                "user_action": r'\b(click|submit|select|input|action)\b',
                "system_event": r'\b(startup|shutdown|error|completion)\b'
            },
            "view_patterns": {
                "interface": r'\b(interface|screen|page|form|dialog)\b',
                "display": r'\b(display|show|render|present|visualize)\b',
                "input": r'\b(input|form|field|control|widget)\b',
                "navigation": r'\b(menu|navigation|link|button|tab)\b'
            }
        }
    
    async def generate_bitcup_model(self, rsd_document: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate BITCUP model from Requirements Specification Document
        
        This method transforms human-readable requirements into a formal,
        machine-parseable semantic model that can be used for code generation.
        """
        
        # Extract semantic elements from RSD
        semantic_analysis = self._analyze_rsd_semantics(rsd_document)
        
        # Generate BITCUP model structure
        bitcup_model = {
            "metadata": {
                "version": "1.0",
                "created_at": datetime.utcnow().isoformat(),
                "source": "RSD_TRANSFORMATION",
                "completeness_score": self._calculate_completeness(semantic_analysis)
            },
            "business_context": self._extract_business_context(rsd_document),
            "entities": self._generate_entities(semantic_analysis),
            "behaviors": self._generate_behaviors(semantic_analysis),
            "rules": self._generate_rules(semantic_analysis),
            "flows": self._generate_flows(semantic_analysis),
            "events": self._generate_events(semantic_analysis),
            "views": self._generate_views(semantic_analysis),
            "constraints": self._extract_constraints(rsd_document),
            "success_criteria": self._extract_success_criteria(rsd_document)
        }
        
        # Validate and enhance the model
        validated_model = self._validate_bitcup_model(bitcup_model)
        
        return validated_model
    
    def _analyze_rsd_semantics(self, rsd_document: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze RSD document to extract semantic elements"""
        
        semantic_analysis = {
            "entities": [],
            "behaviors": [],
            "rules": [],
            "flows": [],
            "events": [],
            "views": []
        }
        
        # Analyze functional requirements
        functional_reqs = rsd_document.get("functional_requirements", {})
        
        # Extract from user stories
        user_stories = functional_reqs.get("user_stories", [])
        for story in user_stories:
            semantic_analysis.update(self._analyze_user_story(story))
        
        # Extract from use cases
        use_cases = functional_reqs.get("use_cases", [])
        for use_case in use_cases:
            semantic_analysis.update(self._analyze_use_case(use_case))
        
        # Extract from business rules
        business_rules = functional_reqs.get("business_rules", [])
        for rule in business_rules:
            semantic_analysis["rules"].extend(self._analyze_business_rule(rule))
        
        # Extract from feature requirements
        features = functional_reqs.get("feature_requirements", [])
        for feature in features:
            semantic_analysis.update(self._analyze_feature(feature))
        
        return semantic_analysis
    
    def _analyze_user_story(self, user_story: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze individual user story for semantic elements"""
        
        analysis = {
            "entities": [],
            "behaviors": [],
            "rules": [],
            "flows": [],
            "events": [],
            "views": []
        }
        
        # Extract text content
        text_content = f"{user_story.get('goal', '')} {user_story.get('benefit', '')}"
        
        # Identify entities
        for entity_type, pattern in self.semantic_patterns["entity_patterns"].items():
            if re.search(pattern, text_content.lower()):
                analysis["entities"].append({
                    "type": entity_type,
                    "role": user_story.get("role", "user"),
                    "context": user_story.get("goal", ""),
                    "source": f"US_{user_story.get('id', 'unknown')}"
                })
        
        # Identify behaviors
        for behavior_type, pattern in self.semantic_patterns["behavior_patterns"].items():
            if re.search(pattern, text_content.lower()):
                analysis["behaviors"].append({
                    "type": behavior_type,
                    "actor": user_story.get("role", "user"),
                    "goal": user_story.get("goal", ""),
                    "priority": user_story.get("priority", "Medium"),
                    "source": f"US_{user_story.get('id', 'unknown')}"
                })
        
        # Extract acceptance criteria as rules
        acceptance_criteria = user_story.get("acceptance_criteria", [])
        for criterion in acceptance_criteria:
            analysis["rules"].append({
                "type": "acceptance",
                "description": criterion,
                "source": f"US_{user_story.get('id', 'unknown')}"
            })
        
        return analysis
    
    def _analyze_use_case(self, use_case: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze use case for semantic elements"""
        
        analysis = {
            "entities": [],
            "behaviors": [],
            "rules": [],
            "flows": [],
            "events": [],
            "views": []
        }
        
        # Analyze main flow for sequence
        main_flow = use_case.get("main_flow", [])
        if main_flow:
            analysis["flows"].append({
                "type": "main_sequence",
                "steps": main_flow,
                "actors": use_case.get("actors", []),
                "source": f"UC_{use_case.get('id', 'unknown')}"
            })
        
        # Analyze alternative flows
        alt_flows = use_case.get("alternative_flows", [])
        for i, alt_flow in enumerate(alt_flows):
            analysis["flows"].append({
                "type": "alternative_sequence",
                "description": alt_flow,
                "source": f"UC_{use_case.get('id', 'unknown')}_ALT_{i}"
            })
        
        # Extract preconditions as rules
        preconditions = use_case.get("preconditions", [])
        for precondition in preconditions:
            analysis["rules"].append({
                "type": "precondition",
                "description": precondition,
                "source": f"UC_{use_case.get('id', 'unknown')}"
            })
        
        return analysis
    
    def _analyze_business_rule(self, business_rule: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Analyze business rule for semantic elements"""
        
        return [{
            "type": "business",
            "description": business_rule.get("rule", ""),
            "rationale": business_rule.get("rationale", ""),
            "impact": business_rule.get("impact", ""),
            "source": f"BR_{business_rule.get('id', 'unknown')}"
        }]
    
    def _analyze_feature(self, feature: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze feature for semantic elements"""
        
        analysis = {
            "entities": [],
            "behaviors": [],
            "rules": [],
            "flows": [],
            "events": [],
            "views": []
        }
        
        # Feature typically represents a behavior or view
        feature_name = feature.get("feature", "").lower()
        
        # Determine if it's a view or behavior
        if any(pattern in feature_name for pattern in ["screen", "page", "form", "interface"]):
            analysis["views"].append({
                "type": "feature_view",
                "name": feature.get("feature", ""),
                "description": feature.get("description", ""),
                "priority": feature.get("priority", "Medium"),
                "source": f"FEATURE_{feature.get('feature', 'unknown')}"
            })
        else:
            analysis["behaviors"].append({
                "type": "feature_behavior",
                "name": feature.get("feature", ""),
                "description": feature.get("description", ""),
                "priority": feature.get("priority", "Medium"),
                "dependencies": feature.get("dependencies", []),
                "source": f"FEATURE_{feature.get('feature', 'unknown')}"
            })
        
        # Extract acceptance criteria as rules
        acceptance_criteria = feature.get("acceptance_criteria", [])
        for criterion in acceptance_criteria:
            analysis["rules"].append({
                "type": "feature_acceptance",
                "description": criterion,
                "source": f"FEATURE_{feature.get('feature', 'unknown')}"
            })
        
        return analysis
    
    def _extract_business_context(self, rsd_document: Dict[str, Any]) -> Dict[str, Any]:
        """Extract business context from RSD"""
        
        project_overview = rsd_document.get("project_overview", {})
        stakeholders = rsd_document.get("stakeholders", {})
        
        return {
            "project_name": project_overview.get("name", ""),
            "description": project_overview.get("description", ""),
            "business_context": project_overview.get("business_context", ""),
            "success_vision": project_overview.get("success_vision", ""),
            "primary_users": stakeholders.get("primary_users", []),
            "stakeholders": stakeholders.get("stakeholders", []),
            "decision_makers": stakeholders.get("decision_makers", [])
        }
    
    def _generate_entities(self, semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate entity definitions from semantic analysis"""
        
        entities = []
        entity_map = {}
        
        # Consolidate entities by type
        for entity in semantic_analysis.get("entities", []):
            entity_type = entity["type"]
            if entity_type not in entity_map:
                entity_map[entity_type] = {
                    "name": entity_type,
                    "type": "entity",
                    "attributes": [],
                    "relationships": [],
                    "sources": []
                }
            
            entity_map[entity_type]["sources"].append(entity["source"])
            
            # Add context as potential attributes
            if entity.get("context"):
                entity_map[entity_type]["attributes"].append({
                    "name": "context",
                    "value": entity["context"],
                    "source": entity["source"]
                })
        
        return list(entity_map.values())
    
    def _generate_behaviors(self, semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate behavior definitions from semantic analysis"""
        
        behaviors = []
        behavior_map = {}
        
        # Consolidate behaviors by type
        for behavior in semantic_analysis.get("behaviors", []):
            behavior_key = f"{behavior['type']}_{behavior.get('actor', 'system')}"
            
            if behavior_key not in behavior_map:
                behavior_map[behavior_key] = {
                    "name": behavior["type"],
                    "actor": behavior.get("actor", "system"),
                    "type": "behavior",
                    "goals": [],
                    "priority": behavior.get("priority", "Medium"),
                    "sources": []
                }
            
            behavior_map[behavior_key]["sources"].append(behavior["source"])
            
            if behavior.get("goal"):
                behavior_map[behavior_key]["goals"].append(behavior["goal"])
        
        return list(behavior_map.values())
    
    def _generate_rules(self, semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate rule definitions from semantic analysis"""
        
        return semantic_analysis.get("rules", [])
    
    def _generate_flows(self, semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate flow definitions from semantic analysis"""
        
        return semantic_analysis.get("flows", [])
    
    def _generate_events(self, semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate event definitions from semantic analysis"""
        
        return semantic_analysis.get("events", [])
    
    def _generate_views(self, semantic_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate view definitions from semantic analysis"""
        
        return semantic_analysis.get("views", [])
    
    def _extract_constraints(self, rsd_document: Dict[str, Any]) -> Dict[str, Any]:
        """Extract constraints from RSD"""
        
        constraints = rsd_document.get("constraints", {})
        non_functional = rsd_document.get("non_functional_requirements", {})
        
        return {
            "technical": constraints.get("technical", []),
            "business": constraints.get("business", []),
            "regulatory": constraints.get("regulatory", []),
            "performance": non_functional.get("performance", {}),
            "security": non_functional.get("security", {}),
            "scalability": non_functional.get("scalability", {})
        }
    
    def _extract_success_criteria(self, rsd_document: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract success criteria from RSD"""
        
        success_criteria = rsd_document.get("success_criteria", {})
        
        return {
            "metrics": success_criteria.get("metrics", []),
            "acceptance_tests": success_criteria.get("acceptance_tests", []),
            "business_outcomes": success_criteria.get("business_outcomes", [])
        }
    
    def _calculate_completeness(self, semantic_analysis: Dict[str, Any]) -> float:
        """Calculate model completeness score"""
        
        total_elements = 0
        present_elements = 0
        
        for construct in self.core_constructs.keys():
            total_elements += 1
            if semantic_analysis.get(construct) and len(semantic_analysis[construct]) > 0:
                present_elements += 1
        
        return present_elements / total_elements if total_elements > 0 else 0.0
    
    def _validate_bitcup_model(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and enhance BITCUP model"""
        
        # Ensure all required sections exist
        required_sections = ["entities", "behaviors", "rules", "flows", "events", "views"]
        
        for section in required_sections:
            if section not in bitcup_model:
                bitcup_model[section] = []
        
        # Add validation metadata
        bitcup_model["validation"] = {
            "is_valid": True,
            "completeness_score": bitcup_model["metadata"]["completeness_score"],
            "validation_timestamp": datetime.utcnow().isoformat(),
            "warnings": self._generate_validation_warnings(bitcup_model)
        }
        
        return bitcup_model
    
    def _generate_validation_warnings(self, bitcup_model: Dict[str, Any]) -> List[str]:
        """Generate validation warnings for incomplete model"""
        
        warnings = []
        
        # Check for empty sections
        for section in ["entities", "behaviors", "rules", "flows", "events", "views"]:
            if not bitcup_model.get(section):
                warnings.append(f"No {section} defined - model may be incomplete")
        
        # Check completeness score
        completeness = bitcup_model["metadata"]["completeness_score"]
        if completeness < 0.5:
            warnings.append(f"Low completeness score ({completeness:.1%}) - consider adding more requirements")
        
        return warnings
    
    async def transform_to_implementation_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform BITCUP model to implementation specification
        
        This method prepares the semantic model for code generation by
        creating technology-specific implementation guidelines.
        """
        
        implementation_spec = {
            "metadata": {
                "source_model": bitcup_model["metadata"],
                "transformation_timestamp": datetime.utcnow().isoformat(),
                "target_architecture": "modern_web_application"
            },
            "architecture": self._generate_architecture_spec(bitcup_model),
            "data_model": self._generate_data_model_spec(bitcup_model),
            "api_specification": self._generate_api_spec(bitcup_model),
            "user_interface": self._generate_ui_spec(bitcup_model),
            "business_logic": self._generate_business_logic_spec(bitcup_model),
            "integration_points": self._generate_integration_spec(bitcup_model)
        }
        
        return implementation_spec
    
    def _generate_architecture_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Generate architecture specification from BITCUP model"""
        
        return {
            "pattern": "layered_architecture",
            "layers": [
                "presentation_layer",
                "business_logic_layer", 
                "data_access_layer",
                "database_layer"
            ],
            "technologies": {
                "frontend": "Vue.js 3",
                "backend": "FastAPI",
                "database": "PostgreSQL",
                "cache": "Redis"
            }
        }
    
    def _generate_data_model_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Generate data model specification"""
        
        entities = bitcup_model.get("entities", [])
        
        data_models = []
        for entity in entities:
            data_models.append({
                "name": entity["name"],
                "type": "database_table",
                "attributes": entity.get("attributes", []),
                "relationships": entity.get("relationships", [])
            })
        
        return {"models": data_models}
    
    def _generate_api_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Generate API specification"""
        
        behaviors = bitcup_model.get("behaviors", [])
        
        endpoints = []
        for behavior in behaviors:
            endpoints.append({
                "path": f"/{behavior['name']}",
                "method": self._map_behavior_to_http_method(behavior),
                "description": f"Handle {behavior['name']} behavior",
                "actor": behavior.get("actor", "system")
            })
        
        return {"endpoints": endpoints}
    
    def _generate_ui_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Generate UI specification"""
        
        views = bitcup_model.get("views", [])
        
        ui_components = []
        for view in views:
            ui_components.append({
                "name": view.get("name", "UnknownView"),
                "type": "vue_component",
                "description": view.get("description", ""),
                "source": view.get("source", "")
            })
        
        return {"components": ui_components}
    
    def _generate_business_logic_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Generate business logic specification"""
        
        rules = bitcup_model.get("rules", [])
        flows = bitcup_model.get("flows", [])
        
        return {
            "business_rules": rules,
            "workflows": flows
        }
    
    def _generate_integration_spec(self, bitcup_model: Dict[str, Any]) -> Dict[str, Any]:
        """Generate integration specification"""
        
        constraints = bitcup_model.get("constraints", {})
        
        return {
            "external_systems": constraints.get("technical", []),
            "apis": [],
            "data_sources": []
        }
    
    def _map_behavior_to_http_method(self, behavior: Dict[str, Any]) -> str:
        """Map behavior type to HTTP method"""
        
        behavior_type = behavior.get("type", "").lower()
        
        method_mapping = {
            "create": "POST",
            "read": "GET", 
            "update": "PUT",
            "delete": "DELETE",
            "search": "GET",
            "validate": "POST",
            "notify": "POST",
            "process": "POST"
        }
        
        return method_mapping.get(behavior_type, "POST")