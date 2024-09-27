# isort Usage Guide

## Installation

1. Using pip:
   ```
   pip install isort
   ```

2. Using poetry:
   ```
   poetry add isort --dev
   ```

3. Using conda:
   ```
   conda install isort -c conda-forge
   ```

## Usage

1. Sort imports in a file or directory:
   ```
   isort path/to/file_or_directory
   ```

2. Check if imports are sorted without making changes:
   ```
   isort --check-only path/to/file_or_directory
   ```

3. Show diff without applying changes:
   ```
   isort --diff path/to/file_or_directory
   ```

4. Sort imports in all Python files recursively:
   ```
   isort .
   ```

## Configuration in pyproject.toml

Create or edit a `pyproject.toml` file in your project root with the following content:

```toml
[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
skip = [".gitignore", ".dockerignore"]
skip_glob = ["*/migrations/*", "*/venv/*"]
known_third_party = ["requests", "numpy", "pandas"]
```

Configuration explanation:

- `profile = "black"`: Use Black-compatible settings
- `line_length`: Maximum line length (should match Black's setting)
- `multi_line_output`: Defines how imports are wrapped
- `include_trailing_comma`: Include a trailing comma in multi-line imports
- `force_grid_wrap`: Force grid wrapping for imports above this number
- `use_parentheses`: Use parentheses for line continuation
- `ensure_newline_before_comments`: Ensures a blank line before comments
- `skip`: List of files to skip
- `skip_glob`: Glob patterns to skip
- `known_third_party`: List of known third-party modules

## Tips

- Run isort before Black to ensure consistent import formatting
- Use `# isort: skip` comment to skip sorting for specific imports
- Combine with Black for comprehensive code formatting

## References

- [isort Documentation](https://pycqa.github.io/isort/)
- [isort GitHub Repository](https://github.com/PyCQA/isort)