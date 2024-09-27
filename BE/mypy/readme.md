# Mypy Usage Guide

## Installation

Using pip:
   ```
   pip install mypy
   ```

## Usage

1. Run mypy on a file or directory:
   ```
   mypy path/to/file_or_directory
   ```

2. Run mypy on the current directory:
   ```
   mypy .
   ```

3. Run mypy with specific Python version:
   ```
   mypy --python-version 3.11 path/to/file_or_directory
   ```

4. Show more detailed error messages:
   ```
   mypy --show-error-context path/to/file_or_directory
   ```

## Configuration in pyproject.toml

Create or edit a `pyproject.toml` file in your project root with the following content:

```toml
[tool.mypy]
python_version = "3.11"
disallow_untyped_defs = true
ignore_missing_imports = true
strict_optional = true
warn_return_any = true
warn_unused_ignores = true
show_error_codes = true
exclude = [
    '^file1\.py$',  # Exclude file1.py
    '^dir1/'        # Exclude everything in dir1/
]

[[tool.mypy.overrides]]
module = ["mycode.foo.*"]
disallow_untyped_defs = false

[tool.mypy-numpy]
ignore_missing_imports = true
```


- `python_version`: Specifies the Python version to use for type checking
- `disallow_untyped_defs`: Disallow functions without type annotations
- `ignore_missing_imports`: Ignore imports that can't be found or don't have stubs
- `strict_optional`: Enable strict optional checks
- `warn_return_any`: Warn about returning Any from functions
- `warn_unused_ignores`: Warn about unused `# type: ignore` comments
- `show_error_codes`: Show error codes in error messages
- `exclude`: Patterns for files/directories to exclude from type checking
- `[[tool.mypy.overrides]]`: Section for module-specific configurations
- `[tool.mypy-numpy]`: Module-specific settings (here, for numpy)

## Tips

- Add type annotations gradually to your project
- Use `# type: ignore` to suppress specific mypy warnings
- Regularly run mypy as part of your development workflow
- Consider using stub files (.pyi) for complex type hints

## References

- [Mypy Documentation](https://mypy.readthedocs.io/)
- [Mypy GitHub Repository](https://github.com/python/mypy)
```