# Contributing to PyX

Thank you for your interest in contributing to PyX! We welcome contributions from everyone. By participating in this project, you agree to abide by our Code of Conduct.

## 🚀 How to Contribute

### 1. Report Bugs or Suggest Features
- **Issues**: Use the [GitHub Issues](https://github.com/sukirman1901/usePyX/issues) tab to report bugs or suggest new features. 
- **Descriptive**: Be as descriptive as possible. Include steps to reproduce bugs or detailed explanations for feature requests.

### 2. Submit Pull Requests (PRs)
1.  **Fork** the repository to your own GitHub account.
2.  **Clone** your fork to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/usePyX.git
    cd usePyX
    ```
3.  **Create a Branch** for your specific feature or fix:
    ```bash
    git checkout -b feature/amazing-feature
    ```
4.  **Set up Development Environment**:
    ```bash
    # Install in editable mode
    pip install -e .
    ```
5.  **Make your changes**. Ensure your code follows the existing style (clean, Pythonic, "Zen Mode").
6.  **Run Tests** to ensure no regressions:
    ```bash
    pyx test
    # or manually
    python3 -m pytest tests/
    ```
7.  **Commit** your changes with a descriptive message:
    ```bash
    git commit -m "feat: Add amazing new component"
    ```
8.  **Push** to your fork:
    ```bash
    git push origin feature/amazing-feature
    ```
9.  **Open a Pull Request** on the main `usePyX` repository.

## 🛠️ Development Guidelines

- **Zen Mode**: Adhere to the philosophy "Write less, do more. Python only."
- **Type Hinting**: Use strict Python type hinting for better developer experience (IDE autocompletion).
- **Documentation**: If you add a new feature, please update the relevant documentation (e.g., `README.md` or docstrings).

## 🧪 Running Tests

We use `pytest` for testing.

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_core.py
```

## 🤝 Community

Join the discussion!
- [GitHub Discussions](https://github.com/sukirman1901/usePyX/discussions) (if enabled)

Thank you for building with us! 🚀
