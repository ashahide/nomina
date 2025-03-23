from ..search.abstract_base_classes import PackageABC, SearchResults

import requests
import re


def normalize_package_name_pypi_rules(package_name: str) -> tuple[bool, str, str | None]:
    """
    Normalize and validate a package name according to PEP 426/508 rules.

    This function checks whether the given package name is valid according to PyPI distribution rules,
    and returns a normalized version if valid.

    Args:
        package_name (str): The original user-provided package name.

    Returns:
        tuple:
            - bool: Whether the package name is valid for PyPI distribution.
            - str: A message describing the validation result.
            - str | None: The normalized package name, or None if the input was invalid.
    """
    if not package_name:
        return False, "Package name cannot be empty", None

    # Check maximum length
    if len(package_name) > 255:
        return False, "Package name exceeds maximum length of 255 characters", None

    # Check that name contains only valid characters
    if not re.match(r"^[a-zA-Z0-9_.-]+$", package_name):
        return False, "Package name contains invalid characters", None

    # Ensure name starts and ends with alphanumeric characters
    if not (package_name[0].isalnum() and package_name[-1].isalnum()):
        return False, "Package name must start and end with a letter or digit", None

    # Disallow consecutive separator characters (., -, _)
    if re.search(r"[-_.]{2,}", package_name):
        return False, "Package name cannot contain consecutive '.', '-', or '_'", None

    # Normalize by collapsing all separators to a single hyphen and converting to lowercase
    normalized = re.sub(r"[-_.]+", "-", package_name).lower()

    # Determine if the input matches the normalized form
    if normalized == package_name:
        return True, "Valid package name", normalized
    else:
        return True, f"Valid, but normalized to {normalized}", normalized


def search_for_pypi_package(package_name: str) -> tuple[object, bool, str]:
    url = f"https://pypi.org/pypi/{package_name}/json"
    response_try_counter: int = 0

    while response_try_counter < 5:
        try:
            response = requests.get(url)
            break
        except requests.exceptions.RequestException as e:
            response_try_counter += 1

    if response_try_counter == 5:
        raise Exception("Network Error: Unable to connect to PyPI after 5 attempts")

    match response.status_code:
        case 404:
            return response, False, "Package not found - Status 404"
        case 200:
            return response, True, "Package found - Status 200"
        case _:
            return response, None, f"Unexpected response status: {response.status_code}"


class PyPiPackage(PackageABC):
    """
    Concrete implementation of PackageABC for Python packages hosted on PyPI.

    This class handles validation, normalization, and search of package names
    using PyPI's naming conventions and API.
    """

    def __init__(self, package_name: str):
        """
        Initialize the PyPiPackage with a user-provided package name.

        Args:
            package_name (str): The package name to validate and search.
        """
        super().__init__(package_name)

    def normalize_package_name(self):
        """
        Normalize the user-provided package name and store the result.

        This sets `self.normalized_package_name`.
        """
        _, _, self.normalized_package_name = normalize_package_name_pypi_rules(
            self.user_package_name_input
        )

    def search_package_index(self):
        """
        Search the PyPI index for the normalized package name.

        Sets:
            - self.search_response_object
            - self.package_exists
            - self.search_results (message)
            - self.official_package_name (if found)
        """
        self.search_response_object, self.package_exists, self.search_results = (
            search_for_pypi_package(self.normalized_package_name)
        )

        # Extract official name from metadata if package exists
        if self.package_exists:
            self.official_package_name = self.search_response_object.json()["info"]["name"]
        else:
            self.official_package_name = None

    def get_search_results(self) -> SearchResults:
        """
        Compile and return a structured summary of the search results.

        Returns:
            SearchResults: Dataclass containing search metadata and results.
        """
        return SearchResults(
            user_input_package_name=self.user_package_name_input,
            official_package_name=self.official_package_name,
            package_exists=self.package_exists,
            normalized_package_name=self.normalized_package_name,
            search_response_object=self.search_response_object,
            search_response_message=self.search_results,
        )
