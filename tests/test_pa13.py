"""
Tests for PA#13: Miller-Rabin Primality Testing
"""

import pytest
from src.primality.miller_rabin import is_prime, gen_prime


class TestMillerRabin:
    """Test Miller-Rabin primality testing."""
    
    def test_small_primes(self):
        """Test known small primes."""
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in small_primes:
            assert is_prime(p, k=20), f"{p} should be identified as prime"
    
    def test_small_composites(self):
        """Test known composite numbers."""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for n in composites:
            assert not is_prime(n, k=20), f"{n} should be identified as composite"
    
    def test_carmichael_number(self):
        """Test Carmichael numbers are correctly identified as composite."""
        # 561 is the smallest Carmichael number: 561 = 3 × 11 × 17
        assert not is_prime(561, k=40), "561 (Carmichael number) should be composite"
    
    def test_large_prime(self):
        """Test a known large prime."""
        # Mersenne prime: 2^31 - 1
        large_prime = 2147483647
        assert is_prime(large_prime, k=20), "2^31 - 1 should be prime"
    
    def test_deterministic_behavior(self):
        """Test that result is deterministic."""
        n = 123456789
        result1 = is_prime(n, k=20)
        result2 = is_prime(n, k=20)
        assert result1 == result2


class TestPrimeGeneration:
    """Test prime generation."""
    
    def test_gen_prime_returns_prime(self):
        """Test that generated number is probably prime."""
        p = gen_prime(bits=64, k=40)
        assert is_prime(p, k=40), "Generated prime should pass Miller-Rabin"
    
    def test_gen_prime_correct_bit_length(self):
        """Test that generated prime has correct bit length."""
        for bits in [32, 64, 128]:
            p = gen_prime(bits=bits, k=20)
            assert p.bit_length() == bits, f"Prime should have exactly {bits} bits"
    
    def test_gen_prime_different_outputs(self):
        """Test that multiple calls generate different primes."""
        primes = [gen_prime(bits=64, k=20) for _ in range(5)]
        assert len(set(primes)) == 5, "Different prime generations should yield different results"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
