import pydantic


class NormalizedReturnMessage(pydantic.BaseModel):
    valid: bool
    message: str


class NormalizedPackage(pydantic.BaseModel):
    """
    Data structure for holding normalized package
    """

    # User input name
    input_name: str

    # Normalized name
    normalized_name: str

    # Note about normalization results
    message: NormalizedReturnMessage


class SearchResults(pydantic.BaseModel):
    """
    Data structure for storing results of a package name search.
    """

    # The original package name provided by the user
    user_input_package_name: str

    # True if the package exists in the registry, False otherwise
    package_exists: bool

    # The registry-normalized version of the input name
    normalized_package_name: str

    # The official name of the package from the registry metadata (if it exists)
    official_package_name: str

    # The raw response object from the registry API (e.g., requests.Response)
    search_response_object: object

    # A human-readable message describing the outcome of the search
    search_response_message: str
