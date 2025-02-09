from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SearchResults:
    environment: str
    user_input_package_name: str
    package_exists: bool
    normalized_package_name: str
    official_package_name: str
    search_response_object: object
    search_response_message: str


class PackageABC(ABC):
    def __init__(self, user_package_name_input: str):
        self.user_package_name_input = user_package_name_input

    @abstractmethod
    def normalize_package_name(self):
        pass

    @abstractmethod
    def search_package_index(self):
        pass

    @abstractmethod
    def get_search_results(self) -> SearchResults:
        pass
