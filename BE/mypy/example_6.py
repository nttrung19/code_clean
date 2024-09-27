#Example 6: Type Error in a Function

def add_numbers(a: int, b: int) -> int:
    return a + b

a = 5
b = "10"
result = add_numbers(a, b)