"""
Random utilities using os.urandom.
Shared utility for all team members.
"""
import os


def generate(n: int) -> bytes:
    """
    Generate n cryptographically random bytes using os.urandom.
    
    Args:
        n: number of bytes to generate
        
    Returns:
        n random bytes
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return os.urandom(n)


def random_bits(num_bits: int) -> bytes:
    """
    Generate random bits as bytes.
    
    Args:
        num_bits: number of bits to generate
        
    Returns:
        random bytes (ceil(num_bits / 8) bytes)
    """
    num_bytes = (num_bits + 7) // 8
    return generate(num_bytes)
