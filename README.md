# Nomina

## Overview

nomina is a package designed to help users create relevant and context-specific names for Python packages. Nomina seeks to ensure given package names are available and appropriate, or generate additional options to satisfy those criteria if the package name is taken.

## Installation

First clone the repo from github (if you haven't already). 

Next, go to the directory where you cloned the repo and run 

```bash
pip install -e .
```

## Usage

# Running the Program

Run the following command to get information about how to use the command line tool

```python3
nomina -h
```

To search PyPI for "pandas" and "numpy", the following command

```python3
nomina pandas numpy
```

which will generate a table showing the results for pandas and numpy.

# Running tests

Tests are run automatically with the following command. 

```python3
python3 -m unittest discover -s tests
```

This command must be run from the root directory of nomina (e.g. /path/to/nomina)


## Other tools

https://pypi.org/project/pkg-name-validator/
