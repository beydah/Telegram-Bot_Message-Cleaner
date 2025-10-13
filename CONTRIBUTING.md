# Contributing to Telegram Service Message Cleaner Bot

Thank you for your interest in contributing to this project! We welcome contributions from everyone, whether you're fixing bugs, adding features, improving documentation, or suggesting enhancements.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors. Please be kind, constructive, and professional in all interactions.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/beydah/Telegram-Bot_Message-Cleaner.git
   cd Telegram-Bot_Message-Cleaner
   ```
3. **Create a new branch** for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Types of Contributions We Welcome

- **Bug fixes**: Fix existing issues or problems
- **Feature additions**: Add new functionality
- **Documentation improvements**: Enhance README, comments, or guides
- **Code optimization**: Improve performance or code quality
- **Testing**: Add or improve test coverage
- **Translations**: Help translate documentation or messages

### Areas Where Help is Needed

- Adding support for more service message types
- Improving error handling and logging
- Adding configuration file support
- Creating unit tests
- Performance optimizations
- Documentation improvements
- Adding multi-language support

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- A Telegram bot token (for testing)
- A test Telegram group

### Installation

1. **Install dependencies**:

   ```bash
   pip install python-telegram-bot
   ```

2. **Set up your test environment**:

   - Create a test bot via [@BotFather](https://t.me/botfather)
   - Create a test group and add your bot as admin
   - Configure `main.py` with your test credentials

3. **Test the setup**:
   ```bash
   python main.py
   ```

## Coding Standards

### Code Style

We follow these coding conventions:

#### Naming Conventions

- **Functions**: Use `F_` prefix with PascalCase (e.g., `F_Delete_Service_Message`)
- **Parameters**: Use `p_` prefix with snake_case (e.g., `p_update`, `p_context`)
- **Variables**: Use descriptive names in snake_case
- **Constants**: Use UPPER_CASE (e.g., `BOT_TOKEN`, `GROUP_ID`)
- **Library imports**: Use `LB_` prefix with aliases (e.g., `import asyncio as LB_ASYNC`)

#### Code Organization

- Use region comments to organize code sections:
  ```python
  # region -------------------- SECTION_NAME --------------------------------------------------------------------------------
  # Code here
  # endregion
  ```

#### Documentation

- Add descriptive comments for all functions:
  ```python
  async def F_Your_Function(p_param: type):
      # DESC: Brief description of what this function does
      pass
  ```

### Code Quality Guidelines

- **Keep functions focused**: Each function should have a single responsibility
- **Use meaningful variable names**: Avoid abbreviations unless they're well-known
- **Add error handling**: Always handle potential exceptions gracefully
- **Include logging**: Add appropriate console output for debugging
- **Optimize for readability**: Code should be self-documenting

## Testing

### Manual Testing

Before submitting changes:

1. **Test basic functionality**:

   - Bot starts without errors
   - `/test` command works
   - Service messages are detected and deleted
   - `/cleanup` command functions properly

2. **Test edge cases**:

   - Bot behavior with insufficient permissions
   - Rate limiting scenarios
   - Invalid configuration handling
   - Network connectivity issues

3. **Test in different environments**:
   - Different Python versions (3.7+)
   - Various group sizes
   - Different service message types

### Future: Automated Testing

We plan to add automated testing. Contributions for test frameworks are welcome!

## Submitting Changes

### Pull Request Process

1. **Ensure your code follows our standards**
2. **Test your changes thoroughly**
3. **Update documentation** if needed
4. **Create a clear commit message**:

   ```
   feat: add support for new service message type

   - Added detection for custom service messages
   - Updated logging to include new message types
   - Added error handling for edge cases
   ```

5. **Submit a pull request** with:
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Screenshots or examples if applicable
   - Reference to any related issues

### Commit Message Format

Use conventional commit format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for code style changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

## Reporting Issues

### Before Reporting

1. **Check existing issues** to avoid duplicates
2. **Test with the latest version**
3. **Gather relevant information**:
   - Python version
   - Operating system
   - Error messages or logs
   - Steps to reproduce

### Issue Template

When reporting bugs, please include:

```markdown
**Bug Description**
A clear description of what the bug is.

**Steps to Reproduce**

1. Go to '...'
2. Click on '....'
3. See error

**Expected Behavior**
What you expected to happen.

**Actual Behavior**
What actually happened.

**Environment**

- OS: [e.g., Windows 10, Ubuntu 20.04]
- Python Version: [e.g., 3.9.0]
- Bot Version: [e.g., 1.0.0]

**Additional Context**
Any other context about the problem.
```

## Feature Requests

We welcome feature suggestions! When requesting features:

1. **Check existing feature requests** first
2. **Describe the problem** you're trying to solve
3. **Explain your proposed solution**
4. **Consider alternative solutions**
5. **Provide use cases** and examples

### Feature Request Template

```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Problem Statement**
What problem does this feature solve?

**Proposed Solution**
How would you like this feature to work?

**Alternatives Considered**
What other solutions have you considered?

**Use Cases**
Specific examples of how this feature would be used.
```

## Development Workflow

### Branching Strategy

- `main`: Stable, production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature branches
- `fix/*`: Bug fix branches
- `docs/*`: Documentation updates

### Release Process

1. Features are merged into `develop`
2. Testing is performed on `develop`
3. Stable versions are merged to `main`
4. Releases are tagged with version numbers

## Getting Help

If you need help with contributing:

- **Create an issue** with the `question` label
- **Check existing documentation** and issues
- **Be specific** about what you need help with

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes for significant contributions
- GitHub contributors page

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for contributing to make this project better! 🚀
