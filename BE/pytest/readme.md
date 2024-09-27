# Pytest Usage Guide

## Installation

Using pip:
   ```
   pip install pytest
   ```

## Basic Usage

1. Run all tests in the current directory and subdirectories:
   ```
   pytest
   ```

2. Run tests in a specific file:
   ```
   pytest test_file.py
   ```

3. Run a specific test function:
   ```
   pytest test_file.py::test_function
   ```

4. Run tests with verbose output:
   ```
   pytest -v
   ```

5. Show extra test summary info:
   ```
   pytest -ra
   ```

## Writing Tests

1. Create test files with names starting or ending with `test_`.
2. Write test functions that start with `test_`.
3. Use `assert` statements to check expected outcomes.

Example:
```python
# test_example.py
def test_addition():
    assert 1 + 1 == 2
```

## Configuration in pyproject.toml

Create or edit a `pyproject.toml` file in your project root with the following content:

```toml
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "serial",
]
pythonpath = [
  "."
]

[tool.pytest.custom_options]
long_running_tests = false
```

Configuration explanation:

- `minversion`: Minimum required pytest version
- `addopts`: Default command line options
- `testpaths`: Directories to search for tests
- `markers`: Custom markers for test categorization
- `pythonpath`: Directories to add to Python path
- `custom_options`: Custom configuration options (example)

## Advanced Features

1. Parameterized testing:
   ```python
   import pytest

   @pytest.mark.parametrize("input,expected", [(1, 2), (2, 3), (3, 4)])
   def test_increment(input, expected):
       assert input + 1 == expected
   ```

2. Using fixtures:
   ```python
   import pytest

   @pytest.fixture
   def sample_data():
       return [1, 2, 3]

   def test_data(sample_data):
       assert len(sample_data) == 3
   ```

3. Running tests with markers:
   ```
   pytest -m slow
   ```

## IDE Integration

- VSCode: Install "Python" extension (includes pytest support)
- PyCharm: Built-in support for pytest

## Tips

- Use `pytest.raises()` to test for expected exceptions
- Utilize `conftest.py` for shared fixtures across multiple test files
- Run tests with coverage using pytest-cov plugin
- Use `--pdb` option to drop into debugger on test failures

## References

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest GitHub Repository](https://github.com/pytest-dev/pytest)
```