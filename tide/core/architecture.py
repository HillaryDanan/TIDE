"""
Cognitive architecture implementation based on dimensional organization patterns.
"""

import numpy as np
from typing import Dict, Any, List
from ..config import ARCHITECTURE_CONFIGS
from .dimensional_space import DimensionalSpace

class CognitiveArchitecture:
    """
    Models cognitive architecture patterns based on neuroscience findings.
    
    Each architecture represents a valid solution to information integration,
    with different dimensional organizations creating distinct processing styles.
    """
    
    def __init__(self, architecture_type: str = 'NT'):
        """
        Initialize cognitive architecture.
        
        Args:
            architecture_type: One of 'NT', 'ASD', 'ADHD'
        """
        if architecture_type not in ARCHITECTURE_CONFIGS:
            raise ValueError(f"Unknown architecture type: {architecture_type}")
        
        self.type = architecture_type
        self.config = ARCHITECTURE_CONFIGS[architecture_type]
        self.dimensional_space = DimensionalSpace()
        self._initialize_architecture()
    
    def _initialize_architecture(self):
        """Set up architecture-specific parameters"""
        self.self_position = self.dimensional_space.compute_element_position(
            'self', self.type
        )
        self.time_position = self.dimensional_space.compute_element_position(
            'time', self.type
        )
        self.integration_distance = np.linalg.norm(
            self.self_position - self.time_position
        )
    
    def process_information(self, information: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process information according to architecture-specific patterns.
        
        Args:
            information: Input information with 'content' and 'temporal_context'
            
        Returns:
            Processed information with architecture-specific modifications
        """
        processed = information.copy()
        
        if self.type == 'NT':
            # Flexible processing with dynamic self-time integration
            processed['temporal_flexibility'] = self._apply_temporal_flexibility(
                information
            )
            processed['self_adaptation'] = self._apply_self_adaptation(information)
            
        elif self.type == 'ASD':
            # Systematic processing with crystallized patterns
            processed['temporal_structure'] = self._apply_temporal_structure(
                information
            )
            processed['rule_consistency'] = self._apply_rule_consistency(information)
            
        elif self.type == 'ADHD':
            # Immediate processing with collapsed temporal dimension
            processed['temporal_compression'] = self._compress_to_now(information)
            processed['intensity_focus'] = self._apply_intensity_focus(information)
        
        processed['architecture_signature'] = self.type
        return processed
    
    def _apply_temporal_flexibility(self, info: Dict[str, Any]) -> float:
        """NT: Flexible temporal processing"""
        return np.random.normal(0.5, 0.2)  # Variable temporal scaling
    
    def _apply_self_adaptation(self, info: Dict[str, Any]) -> float:
        """NT: Adaptive self-representation"""
        return 1.0 - self.integration_distance  # Better integration = more adaptation
    
    def _apply_temporal_structure(self, info: Dict[str, Any]) -> Dict[str, Any]:
        """ASD: Structured temporal processing"""
        return {
            'schedule': self._create_rigid_schedule(info),
            'adherence': 0.9  # High adherence to structure
        }
    
    def _apply_rule_consistency(self, info: Dict[str, Any]) -> float:
        """ASD: Consistent rule application"""
        return self.config['temporal_consistency']
    
    def _compress_to_now(self, info: Dict[str, Any]) -> Dict[str, Any]:
        """ADHD: Collapse temporal dimension to present"""
        return {
            'temporal_window': 'now',
            'past_discount': 0.9,  # Heavy discounting of past
            'future_discount': 0.8  # Heavy discounting of future
        }
    
    def _apply_intensity_focus(self, info: Dict[str, Any]) -> float:
        """ADHD: Intense focus on current stimuli"""
        return np.random.choice([0.1, 0.9])  # Either no focus or hyperfocus
    
    def _create_rigid_schedule(self, info: Dict[str, Any]) -> List[Dict]:
        """Create structured schedule for ASD processing"""
        # Simplified example - would be more complex in practice
        return [{'time': i, 'action': f"step_{i}"} for i in range(10)]
    
    def get_behavioral_signature(self) -> Dict[str, float]:
        """
        Get observable behavioral metrics for this architecture.
        Useful for validation and comparison.
        """
        return {
            'temporal_consistency': self.config['temporal_consistency'],
            'processing_flexibility': self.config['processing_flexibility'],
            'planning_horizon': self.config['planning_horizon'],
            'self_time_integration': 1.0 / (1.0 + self.integration_distance)
        }
