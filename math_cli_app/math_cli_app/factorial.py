def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of the number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result 