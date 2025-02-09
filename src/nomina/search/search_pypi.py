from ..search.abstract_base_classes import PackageABC, SearchResults

import requests
import re


def normalize_package_name_pypi_rules(package_name: str):
    """
    Normalize the package name according to PyPI naming conventions.

    Args:
        package_name (str): The original package name.

    Returns:
        tuple:
            - bool: Whether the package name is valid or not.
            - str: A message indicating the result.
            - str: The normalized package name.
    """
    name_match = re.match(r"^[a-zA-Z0-9_.-]+$", package_name)

    normalized_name = re.sub(r"[-_.]+", "-", package_name).lower()

    if name_match and normalized_name == package_name:
        return True, "Valid package name", normalized_name
    elif name_match and normalized_name != package_name:
        return (
            True,
            f"Valid package name, but normalized to {normalized_name}",
            normalized_name,
        )
    else:
        return False, "Invalid package name", None


def search_for_pypi_package(package_name: str):
    """
    Search for a PyPI package using the normalized name.

    Args:
        package_name (str): The original package name.

    Returns:
        tuple:
            - bool: Whether the package exists or not.
            - str: A message indicating the result of the search.
            - str: The normalized package name used in the search.
    """
    url = f"https://pypi.org/pypi/{package_name}/json"

    response_try_counter: int = 0

    while response_try_counter < 5:
        try:
            response = requests.get(url)
            break
        except:
            response_try_counter += 1

    if response_try_counter == 5:
        raise Exception(
            f"Unable to connect to PyPI after {response_try_counter} attempts"
        )

    match response.status_code:
        case 404:
            package_exists: bool = False
            package_message: str = "Package not found - Status 404"
        case 200:
            package_exists: bool = True
            package_message: str = "Package found - Status 200"
        case _:
            package_exists: bool = None
            package_message: str = "Unknown error"

    return response, package_exists, package_message


class PyPiPackage(PackageABC):
    def __init__(self, package_name: str):
        super().__init__(package_name)

    def normalize_package_name(self):
        _, _, self.normalized_package_name = normalize_package_name_pypi_rules(
            self.user_package_name_input
        )

    def search_package_index(self):
        self.search_response_object, self.package_exists, self.search_results = (
            search_for_pypi_package(self.normalized_package_name)
        )

    def get_search_results(self):
        return SearchResults(
            environment="pypi",
            user_input_package_name=self.user_package_name_input,
            package_exists=self.package_exists,
            normalized_package_name=self.normalized_package_name,
            search_response_object=self.search_response_object,
            search_response_message=self.search_results,
        )
