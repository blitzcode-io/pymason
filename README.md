# PyMason

**PyMason** is a command-line tool designed to simplify Python project management. It handles Python version installation, project creation, dependency management, and more. The tool integrates with [Poetry](https://python-poetry.org/) for managing dependencies and project environments, and uses [Copier](https://copier.readthedocs.io/) for templating.

---

## Features

- **Install Python**: Install specific Python versions silently.
- **Manage Projects**:
  - Create new Python projects using Poetry or Copier templates.
  - Install dependencies in isolated virtual environments.
- **Package Management**:
  - Add or remove packages using Poetry.
- **Cross-platform**: Starting with Windows support, future releases will support other platforms.
- **Pre-commit Hooks**: Integrated with `ruff` for linting and `black` for code formatting.
- **GitFlow**: Follows the GitFlow branching model for development and releases.

---

## Installation

You can install **PyMason** using `pip` from PyPI:


