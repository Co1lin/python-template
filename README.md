# python-template

Template Python project using [src layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).

## Setup

```bash
# for development, editable install # https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
pip install -e '.[dev]'
pre-commit install
```

### Note: [`pre-commit`](https://pre-commit.com)

[`pre-commit`](https://pre-commit.com) is used to unify the format of all files. Basically after installing it, the linters will check the changed files before each commit. If there is any violation, it will block the commit and fix them. Then you need to `git add` the changes and `git commit` again.

## Build

```bash
python -m build
```

## Usage

```bash
python src/hello/main.py hello --name Bill
pytest tests -x # -n 4
```
