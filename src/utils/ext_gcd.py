"""
Extended Euclidean Algorithm for computing modular inverse.
Shared utility for all team members.
Author: Raj
"""


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    
    Computes gcd(a, b) and finds x, y such that:
    a*x + b*y = gcd(a, b)
    
    Args:
        a: first integer
        b: second integer
        
    Returns:
        (gcd, x, y) where gcd = gcd(a,b) and a*x + b*y = gcd
        
    Example:
        >>> gcd, x, y = extended_gcd(10, 6)
        >>> gcd
        2
        >>> 10*x + 6*y
        2
    """
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)


def mod_inverse(a: int, m: int) -> int:
    """
    Compute modular inverse of a modulo m.
    
    Finds the unique x in range [0, m) such that:
    a * x ≡ 1 (mod m)
    
    Uses extended Euclidean algorithm.
    
    Args:
        a: value to invert
        m: modulus (must be positive)
        
    Returns:
        x such that (a * x) mod m = 1
        
    Raises:
        ValueError: if gcd(a, m) != 1 (no inverse exists)
        
    Example:
        >>> mod_inverse(3, 11)
        4
        >>> (3 * 4) % 11
        1
    """
    if m <= 0:
        raise ValueError("m must be positive")
    
    gcd, x, _ = extended_gcd(a, m)
    
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {a} mod {m} (gcd = {gcd})")
    
    # Ensure result is in range [0, m)
    return x % m
