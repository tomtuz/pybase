# Python template

### Components
- Poetry (dep management)
- Ruff (formatting/linting)
- Pre-commit-hooks
- Pytest (tests)
- MyPy (typecheck)

### Prerequisites

- Poetry
- Python 3.12+
- Make (optional)

### Quickstart

- **Select Python version (if using pyenv):**
```bash
# Install specific Python version
pyenv install $(cat .python-version)

# Set local version for this project
pyenv local $(cat .python-version)
```

- **With Make:**
```bash
make setup    # Sets everything else
make help     # Show commands
```

- **Manually:**

```sh
poetry install

# (optional)
poetry run pre-commit install

# (optional)
cp .env.example .env
```

## Running the Application

Use the 'pop' command to run the application:

```sh
> pop dev      # Run the development server
> pop other    # Run other command
```

## Development Workflow

### Linting / Formatting

Uses `Ruff`.

Manual commands:
```sh
> lint   # lint
> lintF  # lint --fix
> format # format + sort imports
```

### Type Checking

Uses `mypy`.

```sh
> typecheck
```

### Pre-commit Hooks

Pre-commit hooks are set up to run Ruff and mypy before each commit. They're installed when you run `pre-commit install`, but you can also run them manually:

```sh
poetry run pre-commit run --all-files
```

## Project Structure

```
├── src/               # Source code
│   └── core/          # Main package
├── dev/               # Development tools and scripts
├── docs/              # Documentation
├── tests/             # Test files
├── .env.example       # Example environment variables
├── pyproject.toml     # Project configuration
└── Makefile           # Common development commands
```

## Managing Dependencies

- Update packages: `poetry update`
- Resolve lock: `poetry lock --no-update`

- Clean pre-commit cache: `pre-commit clean`
- Install hook: `pre-commit install`
