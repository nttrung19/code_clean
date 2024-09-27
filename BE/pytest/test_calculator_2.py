# test_calculator.py

import pytest

from BE.pytest.calculator_2 import divide


def test_divide():
    assert divide(10, 2) == 5.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)



