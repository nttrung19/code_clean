#Example 4: Function Overloading
from typing import overload, Optional


@overload
def process(value: int) -> int:
    pass
@overload
def process(value: str) -> str:
    pass

def process(value: Optional[int | str]) -> Optional[int | str]:
    if isinstance(value, int):
        return value * 2
    if isinstance(value, str):
        return value.upper()
    return None

result = process(10)    # Valid: returns int
result = process("test") # Valid: returns str