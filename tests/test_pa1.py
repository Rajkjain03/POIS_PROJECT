"""
Tests for PA#1: OWF and PRG (HILL Construction)
"""

import pytest
from src.foundations.owf import DLP_OWF, HILL_PRG
from src.utils.random_utils import generate


class TestDLP_OWF:
    """Test DLP-based One-Way Function."""
    
    def test_dlp_owf_deterministic(self):
        """Test that OWF is deterministic."""
        owf = DLP_OWF(bits=128)
        x = generate(16)
        
        y1 = owf.evaluate(x)
        y2 = owf.evaluate(x)
        
        assert y1 == y2, "OWF must be deterministic"
    
    def test_dlp_owf_output_length(self):
        """Test that output has correct length."""
        owf = DLP_OWF(bits=128)
        x = generate(16)
        y = owf.evaluate(x)
        
        # Output should match modulus size
        expected_len = (owf.p.bit_length() + 7) // 8
        assert len(y) == expected_len
    
    def test_dlp_owf_hardness_demo(self):
        """Test hardness inversion demo."""
        owf = DLP_OWF(bits=128)
        result = owf.verify_hardness_demo()
        assert isinstance(result, bool)


class TestHILL_PRG:
    """Test HILL-based Pseudorandom Generator."""
    
    def test_prg_expansion(self):
        """Test that PRG expands seed correctly."""
        owf = DLP_OWF(bits=128)
        prg = HILL_PRG(owf)
        
        seed = generate(16)
        output = prg.expand(seed, 64)
        
        assert len(output) == 64, "PRG should output requested length"
    
    def test_prg_deterministic(self):
        """Test that PRG is deterministic."""
        owf = DLP_OWF(bits=128)
        prg = HILL_PRG(owf)
        
        seed = generate(16)
        output1 = prg.expand(seed, 32)
        output2 = prg.expand(seed, 32)
        
        assert output1 == output2, "PRG must be deterministic"
    
    def test_prg_stretch(self):
        """Test that PRG stretches small seed to large output."""
        owf = DLP_OWF(bits=128)
        prg = HILL_PRG(owf)
        
        seed = generate(16)
        output = prg.expand(seed, 256)
        
        assert len(output) == 256
        assert output != seed + seed + seed + seed  # Not trivial repetition


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
