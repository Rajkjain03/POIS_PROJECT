"""
Tests for PA#2: PRF via GGM Tree
"""

import pytest
from src.prf.ggm_prf import GGM_PRF, PRG_from_GGM_PRF
from src.utils.random_utils import generate


class TestGGM_PRF:
    """Test GGM Tree-based Pseudorandom Function."""
    
    def test_prf_deterministic(self):
        """Test that PRF is deterministic."""
        prf = GGM_PRF()
        
        key = generate(prf.get_key_length())
        x = generate(prf.get_input_length())
        
        y1 = prf.evaluate(key, x)
        y2 = prf.evaluate(key, x)
        
        assert y1 == y2, "PRF must be deterministic"
    
    def test_prf_output_length(self):
        """Test that output has correct length."""
        prf = GGM_PRF()
        
        key = generate(prf.get_key_length())
        x = generate(prf.get_input_length())
        y = prf.evaluate(key, x)
        
        assert len(y) == prf.get_output_length()
    
    def test_prf_different_inputs(self):
        """Test that different inputs produce different outputs (statistically)."""
        prf = GGM_PRF()
        
        key = generate(prf.get_key_length())
        
        outputs = set()
        for _ in range(10):
            x = generate(prf.get_input_length())
            y = prf.evaluate(key, x)
            outputs.add(y)
        
        # All 10 outputs should be different (probability of collision is negligible)
        assert len(outputs) == 10, "Different inputs should produce different PRF outputs"
    
    def test_prf_different_keys(self):
        """Test that different keys produce different outputs."""
        prf = GGM_PRF()
        
        x = generate(prf.get_input_length())
        
        key1 = generate(prf.get_key_length())
        key2 = generate(prf.get_key_length())
        
        y1 = prf.evaluate(key1, x)
        y2 = prf.evaluate(key2, x)
        
        # Outputs should be different for different keys
        assert y1 != y2


class TestPRG_from_PRF:
    """Test backward direction: PRG from PRF."""
    
    def test_prg_from_prf_expansion(self):
        """Test PRG construction from PRF."""
        prf = GGM_PRF()
        prg = PRG_from_GGM_PRF(prf)
        
        seed = generate(prg.get_seed_length())
        output = prg.expand(seed, 64)
        
        assert len(output) == 64


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
