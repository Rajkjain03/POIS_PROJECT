"""
Modular exponentiation with square-and-multiply algorithm.
Shared utility for all team members.
Author: Raj
"""


def square_and_multiply(base: int, exp: int, mod: int) -> int:
    """
    Compute base^exp mod mod using square-and-multiply (binary exponentiation).
    
    This is the standard efficient algorithm for modular exponentiation.
    Time complexity: O(log exp)
    
    Args:
        base: base value
        exp: exponent value
        mod: modulus
        
    Returns:
        base^exp mod mod
        
    Example:
        >>> square_and_multiply(2, 10, 1000)
        24  # because 2^10 = 1024 = 24 (mod 1000)
    """
    if mod == 1:
        return 0
    
    if exp == 0:
        return 1
    
    result = 1
    base = base % mod
    
    # Process each bit of exponent from least significant to most significant
    while exp > 0:
        # If current bit is 1, multiply result by base
        if exp & 1:
            result = (result * base) % mod
        
        # Square the base and shift exponent right
        exp >>= 1
        base = (base * base) % mod
    
    return result
