#Example 2: Using Optional Types
from typing import Optional

def get_user_age(name: str) -> Optional[int]:
    if name == "Alice":
        return 30
    return None

age = get_user_age("Alice")
age = get_user_age("Bob")