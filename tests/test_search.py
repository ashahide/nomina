import unittest
from unittest.mock import patch
from src.search.search_pypi import check_pypi_package

class TestSearchPypi(unittest.TestCase):

    @patch('requests.get')
    def test_check_pypi_package_valid(self, mock_get):
        mock_get.return_value.status_code = 200
        status, message, normalized_name = check_pypi_package('requests')
        self.assertTrue(status)
        self.assertEqual(message, "Package found - Status 200")
        self.assertEqual(normalized_name, 'requests')

    @patch('requests.get')
    def test_check_pypi_package_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        status, message, normalized_name = check_pypi_package('nonexistentpackage')
        self.assertFalse(status)
        self.assertEqual(message, "Package not found - Status 404")
        self.assertEqual(normalized_name, 'nonexistentpackage')

    @patch('requests.get')
    def test_check_pypi_package_invalid_name(self, mock_get):
        status, message, normalized_name = check_pypi_package('invalid....package...name')
        self.assertFalse(status)
        self.assertEqual(message, "Unknown error")
        self.assertEqual(normalized_name, 'invalid-package-name')

    @patch('requests.get')
    def test_check_pypi_package_connection_error(self, mock_get):
        mock_get.side_effect = Exception("Connection error")
        with self.assertRaises(Exception) as context:
            check_pypi_package('requests')
        self.assertTrue("Unable to connect to PyPI" in str(context.exception))

if __name__ == "__main__":
    unittest.main()