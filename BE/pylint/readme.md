# Pylint Usage Guide

## Installation

Using pip:
   ```
   pip install pylint
   ```

## Usage

1. Run pylint on a file or directory:
   ```
   pylint path/to/file_or_directory
   ```

2. Run pylint on multiple files:
   ```
   pylint file1.py file2.py
   ```

3. Generate a report:
   ```
   pylint --output-format=html path/to/file > report.html
   ```

4. List all available messages:
   ```
   pylint --list-msgs
   ```

5. Show messages of a certain category:
   ```
   pylint --disable=all --enable=C path/to/file
   ```

6. Check All Files in a Directory
    ```
    pylint .
    ```

## Configuration in pyproject.toml

Create or edit a `pyproject.toml` file in your project root with the following content:

```toml
[tool.pylint.master]
ignore-patterns = ["^\\.#"]

[tool.pylint.messages_control]
disable = [
    "C0111",  # missing-docstring
    "C0103",  # invalid-name
    "C0330",  # bad-continuation
]

[tool.pylint.format]
max-line-length = 100

[tool.pylint.design]
max-args = 5
max-attributes = 7

[tool.pylint.similarities]
min-similarity-lines = 4
ignore-comments = "yes"
ignore-docstrings = "yes"
ignore-imports = "yes"

[tool.pylint.miscellaneous]
notes = ["FIXME", "XXX", "TODO"]

[tool.pylint.variables]
init-import = "no"
dummy-variables-rgx = "_$|dummy"

[tool.pylint.typecheck]
generated-members = "REQUEST,acl_users,aq_parent"
```

Configuration explanation:

- `[tool.pylint.master]`: General settings
- `[tool.pylint.messages_control]`: Enable/disable specific messages
- `[tool.pylint.format]`: Code formatting settings
- `[tool.pylint.design]`: Design-related checks
- `[tool.pylint.similarities]`: Duplicate code detection settings
- `[tool.pylint.miscellaneous]`: Miscellaneous settings
- `[tool.pylint.variables]`: Variable-related checks
- `[tool.pylint.typecheck]`: Type checking settings

## IDE Integration

- VSCode: Install "Python" extension (includes Pylint support)
- PyCharm: Go to Settings > Tools > External Tools > Add Pylint

## Tips

- Run pylint regularly as part of your development workflow
- Use inline comments to disable specific warnings: # pylint: disable=warning-name
- Customize the configuration to fit your project's needs
- Use with other tools like Black and isort for comprehensive code quality checks

## References

- [Pylint Documentation](https://pylint.pycqa.org/)
- [Pylint GitHub Repository](https://github.com/PyCQA/pylint)