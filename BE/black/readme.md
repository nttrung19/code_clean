# Black: The Uncompromising Code Formatter for Python

## Installation

Using pip:
   ```
   pip install black
   ```

## Usage

### Command Line

1. Format a file or directory:
   ```
   black path/to/file_or_directory
   ```

2. Check if files are formatted without changing them:
   ```
   black --check path/to/file_or_directory
   ```

3. Show diff of changes without applying them:
   ```
   black --diff path/to/file_or_directory
   ```

4. Specify line length (default is 88):
   ```
   black --line-length 79 path/to/file_or_directory
   ```

5. Check all files in the current directory:
   ```
   black .
   ```

### In-Project Configuration

Create a `pyproject.toml` file in your project root:

```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | build
  | dist
)/
'''
verbose = false
diff = false
```

Configuration explanation:

- `line-length`: Maximum line length (default is 88)
- `target-version`: Target Python version
- `include`: Regex pattern for files to include
- `extend-exclude`: Regex pattern for files/directories to exclude
- `skip-string-normalization`: Don't normalize string quotes if set to true
- `skip-magic-trailing-comma`: Skip adding trailing commas if set to true

## Tips

- Run Black regularly to maintain consistent code style
- Integrate with CI/CD pipelines for automatic checks
- Use with other tools like isort for import sorting

## Resources

- [Official Documentation](https://black.readthedocs.io/en/stable/)
- [GitHub Repository](https://github.com/psf/black)
```