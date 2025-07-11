"""
Integration engine for modeling self-time binding dynamics.
Uses insights from BIND framework for integration metrics.
"""

import numpy as np
from typing import Tuple, Dict
from ..config import INTEGRATION_PARAMS

class IntegrationEngine:
    """
    Models how self-representation and temporal processing bind together.
    Different architectures achieve integration through distinct mechanisms.
    """
    
    def __init__(self, architecture_type: str):
        self.architecture = architecture_type
        self.params = INTEGRATION_PARAMS
        self.integration_history = []
        
    def compute_integration(self, self_state: np.ndarray, 
                          time_state: np.ndarray) -> float:
        """
        Compute integration strength (Φ) between self and time.
        Based on BIND framework's boundary dynamics.
        
        Args:
            self_state: Current self-representation state vector
            time_state: Current temporal processing state vector
            
        Returns:
            Integration strength (0-1)
        """
        if self.architecture == 'NT':
            # Dynamic oscillating integration
            phi = self._dynamic_integration(self_state, time_state)
        elif self.architecture == 'ASD':
            # Crystallized lock integration
            phi = self._crystallized_integration(self_state, time_state)
        elif self.architecture == 'ADHD':
            # Quantum collapse integration
            phi = self._collapsed_integration(self_state, time_state)
        else:
            raise ValueError(f"Unknown architecture: {self.architecture}")
        
        self.integration_history.append(phi)
        return phi
    
    def _dynamic_integration(self, self_state: np.ndarray, 
                           time_state: np.ndarray) -> float:
        """NT: Flexible, oscillating integration"""
        base_integration = 1.0 / (1.0 + np.linalg.norm(self_state - time_state))
        oscillation = 0.2 * np.sin(len(self.integration_history) * 0.1)
        return np.clip(base_integration + oscillation, 0, 1)
    
    def _crystallized_integration(self, self_state: np.ndarray,
                                time_state: np.ndarray) -> float:
        """ASD: Stable, locked integration when aligned"""
        distance = np.linalg.norm(self_state - time_state)
        if distance < self.params['boundary_threshold']:
            # Strong integration when both are external
            return 0.9
        else:
            # Weak integration when misaligned
            return 0.2
    
    def _collapsed_integration(self, self_state: np.ndarray,
                             time_state: np.ndarray) -> float:
        """ADHD: Intense but unstable integration"""
        base_integration = 1.0 / (1.0 + np.linalg.norm(self_state - time_state))
        # Add noise for instability
        noise = np.random.normal(0, 0.3)
        return np.clip(base_integration + noise, 0, 1)
    
    def get_integration_stability(self) -> float:
        """
        Measure stability of integration over time.
        ASD should show highest stability, ADHD lowest.
        """
        if len(self.integration_history) < 2:
            return 1.0
        
        history = np.array(self.integration_history)
        return 1.0 - np.std(history)
