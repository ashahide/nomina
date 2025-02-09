import unittest
from unittest.mock import patch

from src.nomina.search.search_pypi import (
    normalize_package_name_pypi_rules,
    search_for_pypi_package,
    PyPiPackage,
)


class TestSearchPypiPackage(unittest.TestCase):
    @patch("src.nomina.search.search_pypi.requests.get")
    def test_search_for_pypi_package_exists(self, mock_get):
        # Test case: Package exists
        mock_get.return_value.status_code = 200
        _, package_exists, package_message = search_for_pypi_package("requests")
        self.assertTrue(package_exists)
        self.assertEqual(package_message, "Package found - Status 200")

    @patch("src.nomina.search.search_pypi.requests.get")
    def test_search_for_pypi_package_not_exists(self, mock_get):
        # Test case: Package does not exist
        mock_get.return_value.status_code = 404
        _, package_exists, package_message = search_for_pypi_package(
            "nonexistent-package"
        )
        self.assertFalse(package_exists)
        self.assertEqual(package_message, "Package not found - Status 404")

    @patch("src.nomina.search.search_pypi.requests.get")
    def test_search_for_pypi_package_network_error(self, mock_get):
        # Test case: Network error (simulated by raising an exception)
        mock_get.side_effect = Exception("Network error")
        with self.assertRaises(Exception) as context:
            search_for_pypi_package("requests")
        self.assertTrue(
            "Unable to connect to PyPI after 5 attempts" in str(context.exception)
        )


class TestPypiNormalization(unittest.TestCase):
    def test_normalize_package_name_valid(self):
        # Test case: Valid package name
        result = normalize_package_name_pypi_rules("requests")
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Valid package name")
        self.assertEqual(result[2], "requests")

    def test_normalize_package_name_invalid(self):
        # Test case: Invalid package name
        result = normalize_package_name_pypi_rules("i$$$$$nvalid..package..name")
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "Invalid package name")
        self.assertEqual(result[2], None)

    def test_normalize_package_name_uppercase(self):
        # Test case: Package name with uppercase letters
        result = normalize_package_name_pypi_rules("NUMPY")
        self.assertEqual(result[0], True)
        self.assertEqual(result[1], "Valid package name, but normalized to numpy")
        self.assertEqual(result[2], "numpy")


class TestPypiPackageClass(unittest.TestCase):
    def test_pypi_package_initialization(self):
        # Test case: Initialize PyPiPackage with a valid package name
        package = PyPiPackage("requests")
        self.assertEqual(package.user_package_name_input, "requests")

    @patch("src.nomina.search.search_pypi.normalize_package_name_pypi_rules")
    def test_normalize_package_name(self, mock_normalize):
        # Test case: Normalize package name
        mock_normalize.return_value = (True, "Valid package name", "requests")
        package = PyPiPackage("requests")
        package.normalize_package_name()
        self.assertEqual(package.normalized_package_name, "requests")

    def test_search_package_index(self):
        # Test case: Search for a package index
        package = PyPiPackage("requests")
        package.normalize_package_name()
        package.search_package_index()
        self.assertTrue(package.package_exists)
        self.assertEqual(
            package.get_search_results().search_response_message,
            "Package found - Status 200",
        )


if __name__ == "__main__":
    unittest.main()
