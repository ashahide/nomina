from abc import ABC, abstractmethod
from .schema import SearchResults


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
