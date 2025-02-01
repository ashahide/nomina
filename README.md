# Nomina

## Overview

nomina is a package designed to help users create relevant and context-specific names for Python packages. Nomina seeks to ensure given package names are available and appropriate, or generate additional options to satisfy those criteria if the package name is taken.


## Usage

# Running the Program

Run the following command to get information about how to use the command line tool

```python3
python3 -m src/nomina/main -h
```

To search PyPI for "pandas" and "numpy", the following command

```python3
python3 -m src/nomina/main pandas numpy
```

which will generate a table showing the results for pandas and numpy.

# Running tests

Tests are run automatically with the following command 

```python3
python3 -m unittest discover -s tests
```


## Other tools

https://pypi.org/project/pkg-name-validator/
