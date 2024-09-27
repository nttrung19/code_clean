#Example 2: Testing Exceptions
# calculator.py

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b