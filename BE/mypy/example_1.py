# Example 1: Basic Type Checking
def greet(name: str) -> str:
    return f"Hello, {name}!"

result = greet("Alice")  # Valid
result = greet("42")       # Type error


"", '' -> "" -> ''
