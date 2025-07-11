"""
Dimensional space mapping for cognitive elements.
Based on Levinson (2021) dissertation findings on internal/external processing.
"""

import numpy as np
from typing import Dict, List, Tuple
from ..config import INTERNAL_FEATURES, EXTERNAL_FEATURES

class DimensionalSpace:
    """
    Maps cognitive elements onto internal-external dimensional space.
    
    Internal dimension: fluid, experiential, social-emotional processing
    External dimension: structured, systematic, logical-temporal processing
    """
    
    def __init__(self):
        self.internal_features = INTERNAL_FEATURES
        self.external_features = EXTERNAL_FEATURES
        self._initialize_space()
    
    def _initialize_space(self):
        """Initialize the dimensional space with empirically-grounded features"""
        self.feature_vectors = {}
        
        # Internal features get positive internal dimension values
        for feature in self.internal_features:
            self.feature_vectors[feature] = np.array([1.0, 0.0])  # [internal, external]
        
        # External features get positive external dimension values  
        for feature in self.external_features:
            self.feature_vectors[feature] = np.array([0.0, 1.0])  # [internal, external]
    
    def compute_element_position(self, element: str, architecture: str = 'NT') -> np.ndarray:
        """
        Compute where a cognitive element lives in dimensional space.
        Position varies by cognitive architecture.
        
        Args:
            element: Cognitive element to map ('self', 'time', 'emotion', etc.)
            architecture: Cognitive architecture type ('NT', 'ASD', 'ADHD')
            
        Returns:
            2D position vector [internal_coord, external_coord]
        """
        if architecture == 'NT':
            return self._nt_mapping(element)
        elif architecture == 'ASD':
            return self._asd_mapping(element)
        elif architecture == 'ADHD':
            return self._adhd_mapping(element)
        else:
            raise ValueError(f"Unknown architecture: {architecture}")
    
    def _nt_mapping(self, element: str) -> np.ndarray:
        """Neurotypical dimensional mapping"""
        mappings = {
            'self': np.array([0.8, 0.2]),   # Primarily internal
            'time': np.array([0.2, 0.8]),   # Primarily external
            'emotion': np.array([0.9, 0.1]), # Strongly internal
            'logic': np.array([0.1, 0.9])    # Strongly external
        }
        return mappings.get(element, np.array([0.5, 0.5]))
    
    def _asd_mapping(self, element: str) -> np.ndarray:
        """ASD dimensional mapping - self shifts to external"""
        mappings = {
            'self': np.array([0.2, 0.8]),   # Shifted to external
            'time': np.array([0.1, 0.9]),   # Strongly external
            'emotion': np.array([0.9, 0.1]), # Remains internal
            'logic': np.array([0.0, 1.0])    # Maximally external
        }
        return mappings.get(element, np.array([0.5, 0.5]))
    
    def _adhd_mapping(self, element: str) -> np.ndarray:
        """ADHD dimensional mapping - time collapses to internal"""
        mappings = {
            'self': np.array([0.9, 0.1]),   # Strongly internal
            'time': np.array([0.8, 0.2]),   # Shifted to internal
            'emotion': np.array([1.0, 0.0]), # Maximally internal
            'logic': np.array([0.2, 0.8])    # Still external
        }
        return mappings.get(element, np.array([0.5, 0.5]))
    
    def compute_dimensional_distance(self, elem1: str, elem2: str, 
                                   architecture: str = 'NT') -> float:
        """
        Compute distance between two elements in dimensional space.
        Useful for understanding integration challenges.
        """
        pos1 = self.compute_element_position(elem1, architecture)
        pos2 = self.compute_element_position(elem2, architecture)
        return np.linalg.norm(pos1 - pos2)
