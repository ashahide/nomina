import pytest
from dataclasses import dataclass

from nomina.search.search_pypi import normalize_package_name_pypi_rules

"""
    Define fixtures
"""


@pytest.fixture
def data_package_name_is_false():

    results = normalize_package_name_pypi_rules(package_name=None)

    yield results


@pytest.fixture
def data_package_name_longer_than_255_characters():

    name = "haha" * 255

    results = normalize_package_name_pypi_rules(package_name=name)

    yield results


@pytest.fixture
def data_package_has_invalid_chars():

    name = "!!!!!!!!invalidNa%%^"

    results = normalize_package_name_pypi_rules(package_name=name)

    yield results


@pytest.fixture
def data_package_has_consecutive_separators():

    name = "pandas..numpy---a"

    results = normalize_package_name_pypi_rules(package_name=name)

    yield results


"""
    Individual tests
"""


def test_working_package_names():

    names = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "fastapi",
        "dask",
        "requests",
        "pytest",
    ]

    conditions = []

    for name in names:
        conditions.append(normalize_package_name_pypi_rules(name)[0])

    assert all(conditions)


def test_package_name_is_false(data_package_name_is_false):
    assert data_package_name_is_false == (False, "Package name cannot be empty", None)


def test_name_length_less_than_255(data_package_name_longer_than_255_characters):

    assert data_package_name_longer_than_255_characters == (
        False,
        "Package name exceeds maximum length of 255 characters",
        None,
    )


def test_name_valid_chars(data_package_has_invalid_chars):

    assert data_package_has_invalid_chars == (
        False,
        "Package name contains invalid characters",
        None,
    )


def test_consecutive_separators(data_package_has_consecutive_separators):

    assert data_package_has_consecutive_separators == (
        False,
        "Package name cannot contain consecutive '.', '-', or '_'",
        None,
    )
