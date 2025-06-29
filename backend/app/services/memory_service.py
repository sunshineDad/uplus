"""
Document Memory Intelligence Service
Create an immortal, ever-learning organizational brain
"""

from typing import Dict, List, Any, Optional, Tuple
import json
import hashlib
from datetime import datetime, timedelta
from collections import defaultdict
import re
from app.core.config import settings

class MemoryService:
    """
    Document Memory Intelligence Service
    
    This service implements the revolutionary memory system that:
    - Creates an immortal, ever-learning organizational brain
    - Tracks every decision linked to its context and outcomes
    - Identifies causal relationships over time
    - Recognizes patterns across projects
    - Provides predictive insights from historical data
    """
    
    def __init__(self):
        # In-memory knowledge graph (would be replaced with proper graph database in production)
        self.knowledge_graph = {
            "nodes": {},  # id -> node data
            "edges": {},  # id -> edge data
            "patterns": {},  # pattern_id -> pattern data
            "insights": {},  # insight_id -> insight data
            "temporal_data": {}  # timestamp -> events
        }
        
        self.pattern_recognition = PatternRecognition()
        self.insight_engine = InsightEngine()
        
    async def store_interaction(self, interaction_data: Dict[str, Any]) -> str:
        """
        Store interaction in the temporal knowledge graph
        
        Every interaction becomes a node in the knowledge graph with
        temporal relationships to other interactions.
        """
        
        interaction_id = self._generate_interaction_id(interaction_data)
        timestamp = datetime.utcnow()
        
        # Create interaction node
        interaction_node = {
            "id": interaction_id,
            "type": "interaction",
            "timestamp": timestamp.isoformat(),
            "data": interaction_data,
            "context": self._extract_context(interaction_data),
            "semantic_fingerprint": self._generate_semantic_fingerprint(interaction_data),
            "relationships": []
        }
        
        # Store in knowledge graph
        self.knowledge_graph["nodes"][interaction_id] = interaction_node
        self.knowledge_graph["temporal_data"][timestamp.isoformat()] = interaction_id
        
        # Identify and create relationships
        await self._identify_relationships(interaction_id, interaction_node)
        
        # Update pattern recognition
        await self._update_patterns(interaction_id, interaction_node)
        
        # Generate insights
        await self._generate_insights(interaction_id, interaction_node)
        
        return interaction_id
    
    async def store_decision(self, decision_data: Dict[str, Any]) -> str:
        """
        Store decision with full context and rationale
        
        Decisions are special nodes that track:
        - The decision made
        - The context and reasoning
        - The expected outcomes
        - The actual outcomes (updated later)
        """
        
        decision_id = self._generate_decision_id(decision_data)
        timestamp = datetime.utcnow()
        
        decision_node = {
            "id": decision_id,
            "type": "decision",
            "timestamp": timestamp.isoformat(),
            "decision": decision_data.get("decision", ""),
            "rationale": decision_data.get("rationale", ""),
            "context": decision_data.get("context", {}),
            "expected_outcomes": decision_data.get("expected_outcomes", []),
            "actual_outcomes": [],  # Updated later
            "decision_maker": decision_data.get("decision_maker", "unknown"),
            "project_id": decision_data.get("project_id", ""),
            "session_id": decision_data.get("session_id", ""),
            "impact_score": 0.0,  # Calculated based on outcomes
            "relationships": []
        }
        
        self.knowledge_graph["nodes"][decision_id] = decision_node
        self.knowledge_graph["temporal_data"][timestamp.isoformat()] = decision_id
        
        # Link to related interactions and decisions
        await self._link_decision_to_context(decision_id, decision_node)
        
        return decision_id
    
    async def store_outcome(self, outcome_data: Dict[str, Any]) -> str:
        """
        Store outcome and link to related decisions
        
        Outcomes complete the learning loop by providing feedback
        on the effectiveness of decisions and approaches.
        """
        
        outcome_id = self._generate_outcome_id(outcome_data)
        timestamp = datetime.utcnow()
        
        outcome_node = {
            "id": outcome_id,
            "type": "outcome",
            "timestamp": timestamp.isoformat(),
            "outcome": outcome_data.get("outcome", ""),
            "success_level": outcome_data.get("success_level", 0.5),  # 0.0 to 1.0
            "metrics": outcome_data.get("metrics", {}),
            "lessons_learned": outcome_data.get("lessons_learned", []),
            "project_id": outcome_data.get("project_id", ""),
            "related_decisions": outcome_data.get("related_decisions", []),
            "relationships": []
        }
        
        self.knowledge_graph["nodes"][outcome_id] = outcome_node
        
        # Update related decisions with actual outcomes
        await self._update_decision_outcomes(outcome_id, outcome_node)
        
        # Learn from the outcome
        await self._learn_from_outcome(outcome_id, outcome_node)
        
        return outcome_id
    
    async def query_memory(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Query the memory system for relevant information
        
        Supports various query types:
        - Temporal: "What happened 6 months ago?"
        - Causal: "Why did we make this decision?"
        - Pattern: "Have we seen this before?"
        - Predictive: "What's likely to happen if we do X?"
        """
        
        query_type = query.get("type", "general")
        
        if query_type == "temporal":
            return await self._temporal_query(query)
        elif query_type == "causal":
            return await self._causal_query(query)
        elif query_type == "pattern":
            return await self._pattern_query(query)
        elif query_type == "predictive":
            return await self._predictive_query(query)
        else:
            return await self._general_query(query)
    
    async def get_insights(self, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Get relevant insights for current context
        
        Returns proactive insights that might be helpful
        for the current situation.
        """
        
        relevant_insights = []
        
        # Find insights related to current context
        for insight_id, insight in self.knowledge_graph["insights"].items():
            relevance_score = self._calculate_insight_relevance(insight, context)
            
            if relevance_score > 0.5:
                relevant_insights.append({
                    "insight": insight,
                    "relevance_score": relevance_score
                })
        
        # Sort by relevance
        relevant_insights.sort(key=lambda x: x["relevance_score"], reverse=True)
        
        return relevant_insights[:10]  # Top 10 insights
    
    async def predict_outcomes(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """
        Predict likely outcomes based on historical patterns
        
        Uses pattern matching and causal analysis to predict
        what might happen in similar scenarios.
        """
        
        # Find similar historical scenarios
        similar_scenarios = await self._find_similar_scenarios(scenario)
        
        # Analyze outcomes of similar scenarios
        outcome_analysis = self._analyze_historical_outcomes(similar_scenarios)
        
        # Generate predictions
        predictions = {
            "predicted_success_probability": outcome_analysis.get("average_success", 0.5),
            "likely_challenges": outcome_analysis.get("common_challenges", []),
            "recommended_approaches": outcome_analysis.get("successful_approaches", []),
            "risk_factors": outcome_analysis.get("risk_factors", []),
            "confidence_level": outcome_analysis.get("confidence", 0.5),
            "similar_cases_count": len(similar_scenarios),
            "historical_evidence": similar_scenarios[:5]  # Top 5 similar cases
        }
        
        return predictions
    
    def _generate_interaction_id(self, interaction_data: Dict[str, Any]) -> str:
        """Generate unique ID for interaction"""
        content = json.dumps(interaction_data, sort_keys=True)
        timestamp = datetime.utcnow().isoformat()
        return hashlib.md5(f"{content}_{timestamp}".encode()).hexdigest()
    
    def _generate_decision_id(self, decision_data: Dict[str, Any]) -> str:
        """Generate unique ID for decision"""
        content = f"{decision_data.get('decision', '')}_{decision_data.get('project_id', '')}"
        timestamp = datetime.utcnow().isoformat()
        return hashlib.md5(f"{content}_{timestamp}".encode()).hexdigest()
    
    def _generate_outcome_id(self, outcome_data: Dict[str, Any]) -> str:
        """Generate unique ID for outcome"""
        content = f"{outcome_data.get('outcome', '')}_{outcome_data.get('project_id', '')}"
        timestamp = datetime.utcnow().isoformat()
        return hashlib.md5(f"{content}_{timestamp}".encode()).hexdigest()
    
    def _extract_context(self, interaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract contextual information from interaction"""
        return {
            "project_id": interaction_data.get("project_id", ""),
            "session_id": interaction_data.get("session_id", ""),
            "user_id": interaction_data.get("user_id", ""),
            "interaction_type": interaction_data.get("type", ""),
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def _generate_semantic_fingerprint(self, interaction_data: Dict[str, Any]) -> str:
        """Generate semantic fingerprint for pattern matching"""
        
        # Extract key semantic elements
        text_content = ""
        if "user_message" in interaction_data:
            text_content += interaction_data["user_message"]
        if "ai_response" in interaction_data:
            text_content += " " + interaction_data["ai_response"]
        
        # Simple semantic fingerprint (would use embeddings in production)
        words = re.findall(r'\w+', text_content.lower())
        key_words = [word for word in words if len(word) > 3]
        
        return "_".join(sorted(set(key_words))[:10])  # Top 10 unique words
    
    async def _identify_relationships(self, interaction_id: str, interaction_node: Dict[str, Any]):
        """Identify relationships with existing nodes"""
        
        semantic_fingerprint = interaction_node["semantic_fingerprint"]
        context = interaction_node["context"]
        
        # Find related interactions
        for node_id, node in self.knowledge_graph["nodes"].items():
            if node_id == interaction_id:
                continue
            
            # Check semantic similarity
            if node.get("semantic_fingerprint"):
                similarity = self._calculate_semantic_similarity(
                    semantic_fingerprint, 
                    node["semantic_fingerprint"]
                )
                
                if similarity > 0.3:  # Threshold for relationship
                    self._create_relationship(interaction_id, node_id, "semantic_similarity", similarity)
            
            # Check temporal proximity
            if node.get("timestamp"):
                time_diff = self._calculate_time_difference(
                    interaction_node["timestamp"],
                    node["timestamp"]
                )
                
                if time_diff < timedelta(hours=24):  # Within 24 hours
                    self._create_relationship(interaction_id, node_id, "temporal_proximity", 1.0 - (time_diff.total_seconds() / 86400))
            
            # Check context similarity
            if node.get("context"):
                context_similarity = self._calculate_context_similarity(context, node["context"])
                
                if context_similarity > 0.5:
                    self._create_relationship(interaction_id, node_id, "context_similarity", context_similarity)
    
    def _create_relationship(self, from_id: str, to_id: str, relationship_type: str, strength: float):
        """Create relationship between nodes"""
        
        relationship_id = f"{from_id}_{to_id}_{relationship_type}"
        
        relationship = {
            "id": relationship_id,
            "from": from_id,
            "to": to_id,
            "type": relationship_type,
            "strength": strength,
            "created_at": datetime.utcnow().isoformat()
        }
        
        self.knowledge_graph["edges"][relationship_id] = relationship
        
        # Add to node relationships
        if from_id in self.knowledge_graph["nodes"]:
            self.knowledge_graph["nodes"][from_id]["relationships"].append(relationship_id)
        
        if to_id in self.knowledge_graph["nodes"]:
            self.knowledge_graph["nodes"][to_id]["relationships"].append(relationship_id)
    
    async def _update_patterns(self, interaction_id: str, interaction_node: Dict[str, Any]):
        """Update pattern recognition with new interaction"""
        
        patterns = self.pattern_recognition.identify_patterns(interaction_node, self.knowledge_graph)
        
        for pattern in patterns:
            pattern_id = pattern["id"]
            
            if pattern_id in self.knowledge_graph["patterns"]:
                # Update existing pattern
                self.knowledge_graph["patterns"][pattern_id]["occurrences"] += 1
                self.knowledge_graph["patterns"][pattern_id]["last_seen"] = datetime.utcnow().isoformat()
                self.knowledge_graph["patterns"][pattern_id]["examples"].append(interaction_id)
            else:
                # Create new pattern
                self.knowledge_graph["patterns"][pattern_id] = {
                    "id": pattern_id,
                    "type": pattern["type"],
                    "description": pattern["description"],
                    "occurrences": 1,
                    "first_seen": datetime.utcnow().isoformat(),
                    "last_seen": datetime.utcnow().isoformat(),
                    "examples": [interaction_id],
                    "confidence": pattern.get("confidence", 0.5)
                }
    
    async def _generate_insights(self, interaction_id: str, interaction_node: Dict[str, Any]):
        """Generate insights from new interaction"""
        
        insights = self.insight_engine.generate_insights(interaction_node, self.knowledge_graph)
        
        for insight in insights:
            insight_id = insight["id"]
            
            self.knowledge_graph["insights"][insight_id] = {
                "id": insight_id,
                "type": insight["type"],
                "description": insight["description"],
                "evidence": insight.get("evidence", []),
                "confidence": insight.get("confidence", 0.5),
                "actionable": insight.get("actionable", False),
                "created_at": datetime.utcnow().isoformat(),
                "source_interaction": interaction_id
            }
    
    def _calculate_semantic_similarity(self, fingerprint1: str, fingerprint2: str) -> float:
        """Calculate semantic similarity between fingerprints"""
        
        words1 = set(fingerprint1.split("_"))
        words2 = set(fingerprint2.split("_"))
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def _calculate_time_difference(self, timestamp1: str, timestamp2: str) -> timedelta:
        """Calculate time difference between timestamps"""
        
        dt1 = datetime.fromisoformat(timestamp1.replace('Z', '+00:00'))
        dt2 = datetime.fromisoformat(timestamp2.replace('Z', '+00:00'))
        
        return abs(dt1 - dt2)
    
    def _calculate_context_similarity(self, context1: Dict[str, Any], context2: Dict[str, Any]) -> float:
        """Calculate context similarity"""
        
        similarity_score = 0.0
        total_factors = 0
        
        # Check project similarity
        if context1.get("project_id") and context2.get("project_id"):
            total_factors += 1
            if context1["project_id"] == context2["project_id"]:
                similarity_score += 1.0
        
        # Check session similarity
        if context1.get("session_id") and context2.get("session_id"):
            total_factors += 1
            if context1["session_id"] == context2["session_id"]:
                similarity_score += 1.0
        
        # Check user similarity
        if context1.get("user_id") and context2.get("user_id"):
            total_factors += 1
            if context1["user_id"] == context2["user_id"]:
                similarity_score += 1.0
        
        return similarity_score / total_factors if total_factors > 0 else 0.0
    
    async def _temporal_query(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Handle temporal queries"""
        
        timeframe = query.get("timeframe", "1 month")
        target_date = self._parse_timeframe(timeframe)
        
        relevant_nodes = []
        
        for node_id, node in self.knowledge_graph["nodes"].items():
            node_date = datetime.fromisoformat(node["timestamp"].replace('Z', '+00:00'))
            
            if node_date >= target_date:
                relevant_nodes.append(node)
        
        return {
            "query_type": "temporal",
            "timeframe": timeframe,
            "results_count": len(relevant_nodes),
            "results": relevant_nodes[:20]  # Limit results
        }
    
    async def _causal_query(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Handle causal queries"""
        
        decision_id = query.get("decision_id", "")
        
        if decision_id in self.knowledge_graph["nodes"]:
            decision_node = self.knowledge_graph["nodes"][decision_id]
            
            # Find related interactions and outcomes
            related_nodes = self._find_related_nodes(decision_id)
            
            return {
                "query_type": "causal",
                "decision": decision_node,
                "related_interactions": related_nodes["interactions"],
                "outcomes": related_nodes["outcomes"],
                "context": decision_node.get("context", {})
            }
        
        return {"query_type": "causal", "error": "Decision not found"}
    
    def _parse_timeframe(self, timeframe: str) -> datetime:
        """Parse timeframe string to datetime"""
        
        now = datetime.utcnow()
        
        if "month" in timeframe:
            months = int(re.search(r'\d+', timeframe).group()) if re.search(r'\d+', timeframe) else 1
            return now - timedelta(days=months * 30)
        elif "week" in timeframe:
            weeks = int(re.search(r'\d+', timeframe).group()) if re.search(r'\d+', timeframe) else 1
            return now - timedelta(weeks=weeks)
        elif "day" in timeframe:
            days = int(re.search(r'\d+', timeframe).group()) if re.search(r'\d+', timeframe) else 1
            return now - timedelta(days=days)
        else:
            return now - timedelta(days=30)  # Default to 1 month


class PatternRecognition:
    """Pattern recognition engine for identifying recurring patterns"""
    
    def identify_patterns(self, interaction_node: Dict[str, Any], knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify patterns in the interaction"""
        
        patterns = []
        
        # Identify conversation patterns
        conversation_pattern = self._identify_conversation_pattern(interaction_node)
        if conversation_pattern:
            patterns.append(conversation_pattern)
        
        # Identify requirement patterns
        requirement_pattern = self._identify_requirement_pattern(interaction_node)
        if requirement_pattern:
            patterns.append(requirement_pattern)
        
        # Identify temporal patterns
        temporal_pattern = self._identify_temporal_pattern(interaction_node, knowledge_graph)
        if temporal_pattern:
            patterns.append(temporal_pattern)
        
        return patterns
    
    def _identify_conversation_pattern(self, interaction_node: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Identify conversation patterns"""
        
        data = interaction_node.get("data", {})
        
        if "user_message" in data and "ai_response" in data:
            user_msg = data["user_message"].lower()
            
            # Identify question-answer patterns
            if "?" in user_msg:
                return {
                    "id": "question_answer_pattern",
                    "type": "conversation",
                    "description": "User asking questions, AI providing answers",
                    "confidence": 0.8
                }
        
        return None
    
    def _identify_requirement_pattern(self, interaction_node: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Identify requirement gathering patterns"""
        
        data = interaction_node.get("data", {})
        
        if "intent_analysis" in data:
            intent_type = data["intent_analysis"].get("intent_type", "")
            
            if intent_type in ["functional_requirement", "non_functional_requirement"]:
                return {
                    "id": f"requirement_pattern_{intent_type}",
                    "type": "requirement",
                    "description": f"Pattern of {intent_type} gathering",
                    "confidence": 0.7
                }
        
        return None
    
    def _identify_temporal_pattern(self, interaction_node: Dict[str, Any], knowledge_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Identify temporal patterns"""
        
        # Simple temporal pattern: interactions within same session
        context = interaction_node.get("context", {})
        session_id = context.get("session_id", "")
        
        if session_id:
            session_interactions = 0
            for node in knowledge_graph["nodes"].values():
                if node.get("context", {}).get("session_id") == session_id:
                    session_interactions += 1
            
            if session_interactions > 3:
                return {
                    "id": f"session_pattern_{session_id}",
                    "type": "temporal",
                    "description": "Extended conversation session",
                    "confidence": 0.6
                }
        
        return None


class InsightEngine:
    """Insight generation engine for creating actionable insights"""
    
    def generate_insights(self, interaction_node: Dict[str, Any], knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate insights from interaction and knowledge graph"""
        
        insights = []
        
        # Generate conversation insights
        conversation_insight = self._generate_conversation_insight(interaction_node, knowledge_graph)
        if conversation_insight:
            insights.append(conversation_insight)
        
        # Generate requirement insights
        requirement_insight = self._generate_requirement_insight(interaction_node, knowledge_graph)
        if requirement_insight:
            insights.append(requirement_insight)
        
        # Generate pattern insights
        pattern_insight = self._generate_pattern_insight(interaction_node, knowledge_graph)
        if pattern_insight:
            insights.append(pattern_insight)
        
        return insights
    
    def _generate_conversation_insight(self, interaction_node: Dict[str, Any], knowledge_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate insights about conversation quality"""
        
        data = interaction_node.get("data", {})
        
        if "intent_analysis" in data:
            completeness_score = data["intent_analysis"].get("completeness_score", 0.0)
            
            if completeness_score < 0.3:
                return {
                    "id": f"low_completeness_{interaction_node['id']}",
                    "type": "conversation_quality",
                    "description": "Low completeness score indicates need for more detailed requirements gathering",
                    "confidence": 0.8,
                    "actionable": True,
                    "evidence": [f"Completeness score: {completeness_score:.1%}"]
                }
        
        return None
    
    def _generate_requirement_insight(self, interaction_node: Dict[str, Any], knowledge_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate insights about requirement patterns"""
        
        # Count requirement types in current session
        context = interaction_node.get("context", {})
        session_id = context.get("session_id", "")
        
        if session_id:
            requirement_types = defaultdict(int)
            
            for node in knowledge_graph["nodes"].values():
                if node.get("context", {}).get("session_id") == session_id:
                    node_data = node.get("data", {})
                    if "intent_analysis" in node_data:
                        intent_type = node_data["intent_analysis"].get("intent_type", "")
                        requirement_types[intent_type] += 1
            
            # Check for missing requirement types
            expected_types = ["functional_requirement", "non_functional_requirement", "business_constraint"]
            missing_types = [t for t in expected_types if requirement_types[t] == 0]
            
            if missing_types:
                return {
                    "id": f"missing_requirements_{session_id}",
                    "type": "requirement_completeness",
                    "description": f"Missing requirement types: {', '.join(missing_types)}",
                    "confidence": 0.7,
                    "actionable": True,
                    "evidence": [f"Current types: {dict(requirement_types)}"]
                }
        
        return None
    
    def _generate_pattern_insight(self, interaction_node: Dict[str, Any], knowledge_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate insights about patterns"""
        
        # Simple pattern insight: repeated similar interactions
        semantic_fingerprint = interaction_node.get("semantic_fingerprint", "")
        
        if semantic_fingerprint:
            similar_count = 0
            
            for node in knowledge_graph["nodes"].values():
                if node.get("semantic_fingerprint") == semantic_fingerprint:
                    similar_count += 1
            
            if similar_count > 3:
                return {
                    "id": f"repeated_pattern_{semantic_fingerprint}",
                    "type": "pattern_recognition",
                    "description": f"Repeated similar interactions detected ({similar_count} times)",
                    "confidence": 0.6,
                    "actionable": False,
                    "evidence": [f"Semantic fingerprint: {semantic_fingerprint}"]
                }
        
        return None