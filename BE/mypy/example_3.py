#Example 3: Type Aliases
from typing import List

Vector = List[float]

def scale(vector: Vector, factor: float) -> Vector:
    return [x * factor for x in vector]

result = scale([1.0, 2.0, 3.0], 2.0)