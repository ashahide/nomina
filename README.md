# Nomina

## Overview

**Nomina** is a Python command line tool that checks if package names are valid and available on popular package registries. Currently, it supports checking availability on [PyPI](https://pypi.org/), and future versions will support other ecosystems like Rust (`crates.io`) and Go (`pkg.go.dev`).

Nomina is useful for:

- Validating that your package name follows naming rules (e.g., PEP 426/508 for PyPI)
- Checking if the name is already taken
- Getting normalized versions of your name (e.g., collapsing `.` and `_` into `-`)
- Avoiding surprises when uploading packages or publishing projects

---

## Installation

Clone the repository and install it in development mode:

```bash
git clone https://github.com/YOUR_USERNAME/nomina.git
cd nomina
pip install -e .
```

---

## Usage

### View CLI Help

Run the following command to see all options:

```bash
nomina -h
```

### Basic Example

To search PyPI for availability of `pandas` and `numpy`:

```bash
nomina pandas numpy
```

### Output

This will generate a table like the following:

```
+--------------+-------------------+----------+----------------------------+
| Input Name   | Normalized Name   | Status   | Message                    |
+==============+===================+==========+============================+
| pandas       | pandas            | True     | Package found - Status 200 |
| numpy        | numpy             | True     | Package found - Status 200 |
+--------------+-------------------+----------+----------------------------+
```

### Handling Invalid Names

Nomina validates names according to PEP 426/508. For example:

```bash
nomina "my--invalid__name" ".badStart" "good_name"
```

Will return:

```
+---------------------+-------------------+----------+------------------------------------------+
| Input Name          | Normalized Name   | Status   | Message                                  |
+=====================+===================+==========+==========================================+
| my--invalid__name   |                   | False    | Invalid package name - not searched      |
| .badStart           |                   | False    | Invalid package name - not searched      |
| good_name           | good-name         | True     | Valid, but normalized to good-name       |
+---------------------+-------------------+----------+------------------------------------------+
```

---

## Running Tests

Tests are discovered automatically. From the root directory of the project, run:

```bash
python3 -m unittest discover -s tests
```

---

## Roadmap

Planned features for future releases:

- Support for other registries:
  - `crates.io` (Rust)
  - `pkg.go.dev` (Go)
  - `npm` (JavaScript)
- Name suggestion/generation if the desired name is unavailable
- JSON or markdown output formats
- GitHub Action integration for CI checks on repo names

---

## Related Tools

- [pkg-name-validator](https://pypi.org/project/pkg-name-validator/): Basic PyPI name validator
- [twine check](https://twine.readthedocs.io/en/latest/#twine-check): Validates PyPI metadata before upload

---

## License

MIT License
