from .search_pypi import PyPiPackage
from .schema.schema import SearchResults
from typing import List


def run_package_search(args) -> List[SearchResults]:
    """
    Main entry point for running package name searches and displaying results.

    This function processes a list of package names provided via CLI args, uses
    a search class to normalize and check availability, and outputs a formatted table.

    Args:
        args: A namespace-like object with a `.name` attribute containing package names.

    Returns:
        str: A table (as a string) summarizing search results for each package name.
    """
    # List to collect structured search results
    package_results = []

    # For now, only PyPI is supported — could be extended to other registries later
    search_class = PyPiPackage

    # Iterate over each user-provided package name
    for name in args.name:
        # Create a new search instance for the current name
        package_instance = search_class(name)

        # Normalize the package name according to the registry's rules
        package_instance.normalize_package_name()

        # Perform the package search (e.g., API call to PyPI)
        package_instance.search_package_index()

        # Retrieve structured results
        package_search_obj = package_instance.get_search_results()

        # Ensure the results conform to the expected format
        assert isinstance(package_search_obj, SearchResults)

        # Add results to output list
        package_results.append(package_search_obj)

    return package_results
