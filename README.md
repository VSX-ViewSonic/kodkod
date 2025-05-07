# Kodkod Pre-Commit Plugin Suite
Welcome to Kodkod, a suite of agile pre-commit plugins designed to enhance your development workflow. Named after the swift and elusive wildcat, Kodkod embodies precision, efficiency, and adaptability. Our first plugin in this suite focuses on ensuring that your commit messages meet our standards, with more plugins to come.

## Getting Started
### Prerequisites
* Python 3.10 or later
* Git
## Installation
To use the Kodkod pre-commit plugins, first, ensure you have pre-commit installed. If not, you can install it using pip:

```bash
pip install pre-commit
```

Next, add Kodkod to your project's .pre-commit-config.yaml file:

```yaml
default_install_hook_types:
  - pre-commit
  - commit-msg

repos:
  - repo: https://github.com/VSX-ViewSonic/Kodkod
    rev: 0.4.0
    hooks:
    - id: check-commit-message
    - id: format-dotnet
```
Finally, install the git hook scripts:

```bash
pre-commit install
```
