# Pre-commit Usage Guide

## Installation

Using pip:
   ```
   pip install pre-commit
   ```

## Setup

1. Create a `.pre-commit-config.yaml` file in your project root:
   ```
   touch .pre-commit-config.yaml
   ```

2. Install the git hook scripts:
   ```
   pre-commit install
   ```

## Configuration

Edit the `.pre-commit-config.yaml` file with the following content:

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    -   id: black
        language_version: python3

-   repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
    -   id: isort
        args: ["--profile", "black"]

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
    -   id: mypy
        additional_dependencies: [types-all]

-   repo: https://github.com/PyCQA/pylint
    rev: v2.17.4
    hooks:
    -   id: pylint
        args: [
          "--disable=C0111", # missing-docstring
        ]

-   repo: local
    hooks:
    -   id: pytest-check
        name: pytest-check
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true

```

This configuration includes:
- Basic pre-commit hooks
- Black for code formatting
- isort for import sorting
- flake8 for linting

## Usage

1. Run against all files:
   ```
   pre-commit run --all-files
   ```

2. Run against staged files:
   ```
   pre-commit run
   ```

3. Update hooks to the latest version:
   ```
   pre-commit autoupdate
   ```

## Skipping Hooks

To skip a specific hook:
```
SKIP=black,isort,mypy git commit -m "Commit message"
```

## CI Integration

Add this to your CI config (e.g., .travis.yml):
```yaml
   - pip install pre-commit
   - pre-commit run --all-files
```

## Tips

1. Commit the `.pre-commit-config.yaml` file to share the configuration with your team.
2. Run `pre-commit install` after cloning a repository that uses pre-commit.
3. Use `pre-commit run` before pushing to catch issues early.
4. Customize hook configurations in `.pre-commit-config.yaml` as needed.


This adds a local hook to run pytest.

## References

- [Pre-commit Documentation](https://pre-commit.com/)
- [Pre-commit Hooks](https://pre-commit.com/hooks.html)
- [Pre-commit GitHub Repository](https://github.com/pre-commit/pre-commit)