"""
Integer root computation for PA#14 (Håstad broadcast attack).
Shared utility for all team members.
Author: Raj
"""


def integer_root(n: int, k: int, epsilon: float = 1e-10) -> int:
    """
    Compute the k-th integer root of n using Newton's method.
    
    Finds the largest integer x such that x^k <= n.
    
    Args:
        n: non-negative integer
        k: positive integer (root degree)
        epsilon: convergence threshold
        
    Returns:
        floor(n^(1/k))
        
    Example:
        >>> integer_root(27, 3)
        3
        >>> integer_root(1000, 3)
        10
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if k <= 0:
        raise ValueError("k must be positive")
    
    if n == 0 or k == 1:
        return n
    
    # Newton's method: x_{n+1} = ((k-1)*x_n + N/x_n^(k-1)) / k
    x = n  # Initial guess
    
    while True:
        x_new = ((k - 1) * x + n // (x ** (k - 1))) // k
        
        if x_new >= x:
            break
        x = x_new
    
    return x
