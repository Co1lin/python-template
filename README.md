# python-template

Template Python project using [src layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout).

## Setup

```bash
# for development, editable install # https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs
pip install -e '.[dev]'
pre-commit install
```

## Build

```bash
python -m build
```

## Usage

```bash
python src/hello/main.py hello --name Bill
pytest tests -x # -n 4
```
