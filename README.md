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
python src/hello/main.py hello --name Colin --prefix haha
pytest tests -x # -n 4
```

## Explanation & Recommendations

### Use [`pre-commit`](https://pre-commit.com) to format code

[`pre-commit`](https://pre-commit.com) is used to unify the format of all files. Basically after installing it, the linters will check the changed files before each commit. If there is any violation, it will block the commit and fix them. Then you need to `git add` the changes and `git commit` again.

### Use Miniforge/Mamba to manage virtual environments

Mamba is a drop-in replacement for Conda that is generally **faster and better at resolving dependencies**. You may have seen conda uses lots of time to resolve dependencies and seems to be stuck, mamba will not have this issue!

Use [miniforge](https://github.com/conda-forge/miniforge) to install mamba. Go to the [release page](https://github.com/conda-forge/miniforge/releases) and download the latest version of [Miniforge3-Linux-x86_64.sh](https://github.com/conda-forge/miniforge/releases/download/24.11.0-1/Miniforge3-Linux-x86_64.sh) to install mamba on Linux.

After installation, you can use both conda and mamba. Since mamba resolves dependencies way faster, for installation/env creation, it’s better to use mamba, like:

```bash
mamba create -y -n py310 python=3.10
mamba install nvitop
```

For environment switching, you can still use conda, or just stick to mamba.

```bash
mamba activate py310
conda activate py310
```

## src-layout, import, and editable install

[src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout) is a common style of the package structure.

Always import dependencies from the root path, like [this](https://github.com/Co1lin/python-template/blob/main/tests/test_main.py#L2). Avoid relative imports.

With [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout), we need to do editable install to run the package during development:

```bash
pip install -e '.[dev]'
```

### Specify dependencies with minimal constraints

Specify dependencies in [pyproject.toml](https://github.com/Co1lin/python-template/blob/main/pyproject.toml) with minimal constraints (no version specifiers if possible).

Dependencies required to just "use" the package should be specified in `[project] dependencies`.

Dependencies only required during development should be specified in `[project.optional-dependencies] dev`, and they will be installed when `pip install '<pkg_name>[dev]'`.


### Use `fire` for command line arguments handling

[`fire`](https://github.com/google/python-fire) can automatically generate command line interfaces from your Python code. See [this](https://github.com/Co1lin/python-template/blob/main/src/hello/main.py) for an example.
