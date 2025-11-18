# python-template

Template Python project using [src layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).

## Setup

### Python Environment

```bash
# we use uv to manage Python dependencies because it is super fast and flexible
# https://docs.astral.sh/uv/concepts/projects/config/#build-isolation
# two-step uv sync process
uv sync

# install pre-commit hook (required for committing to this repo, otherwise CI check will fail)
uv run pre-commit install
```

NOTE: `uv` installs dependencies into `./venv` which is unknown for your shell by default. Therefore, you should use `uv run <command>` to run all commands using the dependencies. Check [`uv`'s documentation](https://docs.astral.sh/uv/concepts/projects/run) for details.

NOTE: Since we use `uv` for dependency management, you should avoid using `pip` to change dependencies. Instead, use `uv add` or `uv remove`. Check [`uv`'s documentation](https://docs.astral.sh/uv/concepts/projects/dependencies) for details.

## Development Notes

TODO

## Explanations to Engineering Practices

### Use [`pre-commit`](https://pre-commit.com) to format code

[`pre-commit`](https://pre-commit.com) is used to unify the format of all files. Basically after installing it, the linters will check the changed files before each commit. If there is any violation, it will block the commit and fix them. Then you need to `git add` the changes and `git commit` again.

### Specify dependencies with minimal constraints

Specify dependencies in [pyproject.toml](https://github.com/Co1lin/python-template/blob/main/pyproject.toml) with minimal constraints (no version specifiers if possible).

Dependencies required to just "use" the package should be specified in `[project] dependencies`.

Dependencies only required during development should be specified in `[dependency-groups] dev`.


### Use `fire` for command line arguments handling

[`fire`](https://github.com/google/python-fire) can automatically generate command line interfaces from your Python code. See [this](https://github.com/Co1lin/python-template/blob/main/src/hello/main.py) for an example.
