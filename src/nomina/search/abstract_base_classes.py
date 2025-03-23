from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SearchResults:
    """
    Data container for storing results of a package name search.
    """
    user_input_package_name: str         # The original package name provided by the user
    package_exists: bool                 # True if the package exists in the registry, False otherwise
    normalized_package_name: str         # The registry-normalized version of the input name
    official_package_name: str           # The official name of the package from the registry metadata (if it exists)
    search_response_object: object       # The raw response object from the registry API (e.g., requests.Response)
    search_response_message: str         # A human-readable message describing the outcome of the search


class PackageABC(ABC):
    """
    Abstract base class for defining a common interface to search
    and validate package names across different package registries.

    Subclasses must implement normalization, search, and result handling.
    """

    def __init__(self, user_package_name_input: str):
        """
        Initialize with the user-provided package name.

        Args:
            user_package_name_input (str): The original package name entered by the user.
        """
        self.user_package_name_input = user_package_name_input

    @abstractmethod
    def normalize_package_name(self):
        """
        Normalize the user-provided package name according to the target registry's rules.
        This should set the instance attribute `self.normalized_package_name`.
        """
        pass

    @abstractmethod
    def search_package_index(self):
        """
        Perform the search against the target package index (e.g., PyPI, crates.io).
        This should set relevant instance attributes like `self.package_exists`, 
        `self.official_package_name`, `self.search_results`, and `self.search_response_object`.
        """
        pass

    @abstractmethod
    def get_search_results(self) -> SearchResults:
        """
        Return a structured SearchResults object summarizing the search outcome.
        
        Returns:
            SearchResults: The collected data about the search result.
        """
        pass
