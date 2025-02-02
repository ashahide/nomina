from ..formatting import search_output
from ..search.abstract_base_classes import PackageABC

import requests
import re
from typing import Tuple

def normalize_package_name(package_name: str) -> Tuple[bool, str, str]:
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
    name_match = re.match(r'^[a-zA-Z0-9_.-]+$', package_name)
    
    normalized_name = re.sub(r'[-_.]+', '-', package_name).lower()

    if name_match and normalized_name == package_name:
        return True, "Valid package name", normalized_name
    elif name_match and normalized_name != package_name:
        return True, f"Valid package name, but normalized to {normalized_name}", normalized_name
    else:
        return False, "Invalid package name", normalized_name


def search_for_pypi_package(package_name: str) -> Tuple[bool, str, str]:
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
    name_status, name_message, normalized_name = normalize_package_name(package_name)

    url = f"https://pypi.org/pypi/{normalized_name}/json"
    
    response_try_counter = 0
    
    while response_try_counter < 5:
        try:
            response = requests.get(url)
            break
        except:
            response_try_counter += 1

    if response_try_counter == 5:
        raise Exception(f"Unable to connect to PyPI after {response_try_counter} attempts")

    match response.status_code:
        case 404:
            return False, "Package not found - Status 404", normalized_name
        case 200:
            return True, "Package found - Status 200", normalized_name
        case _:
            return False, 'Unknown error', normalized_name


class PyPiPackage(PackageABC):
    """
    A subclass of PackageABC to handle searching for packages in the PyPI repository.

    Attributes:
        package_name (str): The original name of the package.
        normalized_package_name (str): The normalized package name used for querying.
        package_query_status (bool): Whether the package exists on PyPI.
        package_information (dict): Metadata about the package retrieved from PyPI.
    """

    def __init__(self, package_name: str):
        """
        Initialize a PyPiPackage instance with a package name.

        Args:
            package_name (str): The name of the package.
        """
        super().__init__(package_name)

    def get_normalized_package_name(self) -> str:
        """
        Normalize the package name according to PyPI naming conventions.

        Returns:
            str: The normalized package name.
        """
        _, _, self.normalized_package_name = normalize_package_name(self.input_package_name)
        return self.normalized_package_name

    def search_package_list(self) -> Tuple[bool, dict]:
        """
        Search for the package in PyPI using the normalized package name.

        Returns:
            tuple:
                - bool: Whether the package exists or not.
                - dict: Package metadata (in this case, empty).
        """
        package_exists, message, normalized_name = search_for_pypi_package(self.input_package_name)

        # Set the results
        self.package_query_status = package_exists
        self.package_information = {"message": message}
        
        return self.package_query_status, self.package_information



def main(args):
    """
    Main function to search for PyPI packages and generate a table with search results.
    
    Args:
        args (Namespace): Arguments containing the list of package names.

    Returns:
        tuple: A tuple containing the generated table and a list of PyPiPackage result objects.
    """
    
    # List to store the PyPiPackage instances (representing the search results for each package)
    package_results = []

    # Iterate over each package name provided in the arguments
    for name in args.name:
        # Create an instance of the PyPiPackage subclass
        package = PyPiPackage(name)

        # Get the normalized package name (call the method)
        package.get_normalized_package_name()  # Ensures it sets normalized_name

        # Perform the search and get the status and additional information
        package.search_package_list()  # Updates the status and message attributes

        # Append the package instance to the package_results list
        package_results.append(package)
    
    # Generate the output table (assuming search_output.create_pypi_output_table is defined elsewhere)
    table = search_output.create_pypi_output_table(
        [package.input_package_name for package in package_results],  # Access package_name directly
        [package.normalized_package_name for package in package_results],  # Access normalized_name (as a property)
        [package.package_query_status for package in package_results],  # Access status
        [package.package_information['message'] for package in package_results]  # Access message
    )

    return table, package_results