import pydantic


class SearchResults(pydantic.BaseModel):
    """
    Data container for storing results of a package name search.
    """

    user_input_package_name: str  # The original package name provided by the user
    package_exists: bool  # True if the package exists in the registry, False otherwise
    normalized_package_name: str  # The registry-normalized version of the input name
    official_package_name: str  # The official name of the package from the registry metadata (if it exists)
    search_response_object: object  # The raw response object from the registry API (e.g., requests.Response)
    search_response_message: (
        str  # A human-readable message describing the outcome of the search
    )
