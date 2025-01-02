# Contributing to Hirst Painting Project

First off, thank you for considering contributing to the Hirst Painting Project! It's people like you that make this project better.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Exercise consideration and empathy
- Gracefully accept constructive criticism

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues list. When you create a bug report, include as many details as possible:

- Use a clear and descriptive title
- Describe the exact steps to reproduce the problem
- Provide specific examples
- Describe the behavior you observed and what behavior you expected
- Include screenshots if possible

### Suggesting Enhancements

If you have ideas for new features or improvements:

- Use a clear and descriptive title
- Provide a detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- List any additional requirements

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Update the documentation if needed

#### Pull Request Process

1. Update the README.md with details of changes if needed
2. Follow the style guidelines
3. Include relevant tests
4. Link any relevant issues in the PR description

## Development Process

1. Clone the repository
```bash
git clone https://github.com/your-username/hirst-painting-project.git
cd hirst-painting-project
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a branch
```bash
git checkout -b feature/your-feature-name
```

### Style Guidelines

- Follow PEP 8 style guide
- Use type hints
- Format code using Black
- Add docstrings to all functions and classes
- Keep functions focused and small
- Use meaningful variable names

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_specific_file.py

# Run with coverage report
pytest --cov=.

# Run style checks
flake8 .
black . --check
```

### Documentation

- Keep docstrings up to date
- Follow Google style docstrings format
- Update README.md if adding new features
- Include example usage in docstrings

Example docstring format:
```python
def function_name(param1: type, param2: type) -> return_type:
    """Short description of function.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ErrorType: Description of when this error occurs
    """
```

## Project Structure

When adding new features, maintain the existing project structure:

```
hirst_painting_project/
├── main.py               # Entry point
├── painter.py            # Painting logic
├── color_palette.py      # Color management
├── art_manager.py        # Workflow coordination
├── utils.py             # Utilities
└── test/                # Test files
```

## Questions?

Feel free to open an issue with the "question" label if you have any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file). 