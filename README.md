# 📦 my_krml_24669044

**Author**: Rohan Yadav  
**Version**: 2025.0.1.0  
**License**: None



## Installation

```bash
$ pip install my_krml_24669044
```

## Setup steps

**Create an account in TestPypi (https://test.pypi.org/)**

### Step 1: Create Package Structure Using Cookiecutter

```bash
pip install cookiecutter
cookiecutter https://github.com/py-pkgs/py-pkgs-cookiecutter.git
```

### Step 2: Setup Python Environment with Pyenv
```bash
pyenv install 3.11.4

pyenv local 3.11.4
```

### Step 3: Initialize Poetry and Install Dependencies
```bash
poetry init
poetry env use 3.11.4

# Core dependencies
poetry add pandas==2.2.2 scikit-learn==1.5.1

# Dev & Notebook dependencies
poetry add pytest==8.2.2 jupyterlab==4.2.3
```

### Step 4: Configure Poetry for Test PyPI
```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/

poetry config pypi-token.test-pypi pypi-<your_api_key>
```

### Step 5: Run Tests & Build the Package
```bash
poetry run pytest

# Set version
poetry version 2025.0.1.0

# Build wheel and source distribution
poetry build
```

### Step 6: Publish to Test PyPI
```bash
poetry publish -r test-pypi
```


## Usage

- `my_krml_24669044` is a Python package designed to **identify and remove duplicate records** efficiently, making life easier for coders working with large datasets.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`my_krml_24669044` was created by Rohan Yadav. Rohan Yadav retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.

## Credits

`my_krml_24669044` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
