"""Configuration settings for TIDE framework"""

import numpy as np

# Dimensional mappings based on empirical findings
ARCHITECTURE_CONFIGS = {
    'NT': {
        'self_dimension': 'internal',
        'time_dimension': 'external',
        'integration_style': 'dynamic',
        'processing_flexibility': 0.8,
        'temporal_consistency': 0.6,
        'planning_horizon': 30  # days
    },
    'ASD': {
        'self_dimension': 'external',
        'time_dimension': 'external',
        'integration_style': 'crystallized',
        'processing_flexibility': 0.3,
        'temporal_consistency': 0.9,
        'planning_horizon': 90  # days
    },
    'ADHD': {
        'self_dimension': 'internal',
        'time_dimension': 'internal',
        'integration_style': 'collapsed',
        'processing_flexibility': 0.9,
        'temporal_consistency': 0.2,
        'planning_horizon': 1  # days
    }
}

# Feature dimensions from dissertation findings
INTERNAL_FEATURES = ['emotion', 'social', 'morality', 'thought', 'polarity']
EXTERNAL_FEATURES = ['time', 'space', 'number', 'logic', 'structure']

# Integration parameters
INTEGRATION_PARAMS = {
    'boundary_threshold': 0.5,
    'phi_normalization': True,
    'temporal_window': 100
}
