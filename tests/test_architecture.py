"""
Tests for cognitive architecture functionality
"""

import pytest
import numpy as np
from tide.core.architecture import CognitiveArchitecture

def test_architecture_creation():
    """Test creating different architecture types"""
    # Should work
    nt = CognitiveArchitecture('NT')
    assert nt.type == 'NT'
    
    asd = CognitiveArchitecture('ASD')
    assert asd.type == 'ASD'
    
    adhd = CognitiveArchitecture('ADHD')
    assert adhd.type == 'ADHD'
    
    # Should fail
    with pytest.raises(ValueError):
        bad = CognitiveArchitecture('INVALID')

def test_behavioral_signatures():
    """Test that architectures have distinct signatures"""
    nt = CognitiveArchitecture('NT')
    asd = CognitiveArchitecture('ASD')
    adhd = CognitiveArchitecture('ADHD')
    
    nt_sig = nt.get_behavioral_signature()
    asd_sig = asd.get_behavioral_signature()
    adhd_sig = adhd.get_behavioral_signature()
    
    # Check expected patterns
    assert asd_sig['temporal_consistency'] > nt_sig['temporal_consistency']
    assert asd_sig['temporal_consistency'] > adhd_sig['temporal_consistency']
    assert adhd_sig['planning_horizon'] < nt_sig['planning_horizon']

def test_information_processing():
    """Test that each architecture processes information differently"""
    info = {'content': 'test', 'temporal_context': 'future planning'}
    
    nt = CognitiveArchitecture('NT')
    asd = CognitiveArchitecture('ASD')
    adhd = CognitiveArchitecture('ADHD')
    
    nt_result = nt.process_information(info)
    asd_result = asd.process_information(info)
    adhd_result = adhd.process_information(info)
    
    # Each should have unique processing
    assert 'temporal_flexibility' in nt_result
    assert 'temporal_structure' in asd_result
    assert 'temporal_compression' in adhd_result
