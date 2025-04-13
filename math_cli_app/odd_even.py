def check_odd_even(n: int) -> str:
    """
    Check if a number is odd or even.
    
    Args:
        n (int): Integer to check
        
    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd
    """
    return "Even" if n % 2 == 0 else "Odd" 