## Stack

- Poetry (dep management)
- Ruff (formatting/linting)
- pre-commit-hooks
- pytest (tests)
- mypy (typecheck)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/totmuz/pybase.git
   cd pybase
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Set up pre-commit hooks:
   ```
   poetry run pre-commit install
   ```

4. Create a `.env` file in the project root and add your environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file and add your actual values.

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

```
poetry run pre-commit run --all-files
```

## Project Structure

- `src/core/`: Main package code
- `dev/`: Development helpers
- `pyproject.toml`: Poetry configuration and project metadata
- `.pre-commit-config.yaml`: Pre-commit hook configuration
- `.editorconfig`: Editor configuration for consistent coding styles

## Managing Dependencies

- Update packages: `poetry update`
- Resolve lock: `poetry lock --no-update`

- Clean pre-commit cache: `pre-commit clean`
- Install hook: `pre-commit install`
