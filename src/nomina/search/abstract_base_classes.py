from abc import ABC, abstractmethod

class PackageABC(ABC):
    """
    Abstract Base Class (ABC) for managing package information.

    This class provides a framework for subclasses to manage:
    - Package name (input and normalized)
    - Package query URL (to search for the package)
    - Package query status (whether the package exists)
    - Package information (metadata about the package)

    Attributes:
        _input_package_name (str): The original name of the package, provided by the user.
        _package_query_url (str): The URL used to query a package manager or repository, constructed from the package name.
        _normalized_package_name (str): The normalized version of the package name, should be set by subclasses.
        _package_query_status (bool): The status of the package (True if exists, False if not), should be set by subclasses.
        _package_information (dict): Metadata about the package, should be set by subclasses.
    """

    def __init__(self, package_name: str):
        """
        Initialize a PackageABC instance with a package name.

        Args:
            package_name (str): The name of the package.
        """
        # Store the package name as a private attribute
        self._input_package_name = package_name

        # Initialize the other attributes as None. These will be set by subclasses.
        self._normalized_package_name = None  
        self._package_query_status = None  
        self._package_information = None  

    """ Enforce attributes with property decorators """

    @property
    def input_package_name(self) -> str:
        """Returns the original package name provided by the user."""
        return self._input_package_name  

    @property
    def normalized_package_name(self) -> str:
        """
        Returns the normalized package name.

        This will raise a ValueError if the normalized name hasn't been set by a subclass.
        """
        if self._normalized_package_name is None:
            raise ValueError("Normalized package name has not been set.")
        return self._normalized_package_name

    @normalized_package_name.setter
    def normalized_package_name(self, value: str):
        """
        Sets the normalized package name.
        
        Allows subclasses to assign the normalized name. 
        
        Args:
            value (str): The normalized package name.
        
        Raises:
            TypeError: If the value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("Normalized package name must be a string.")
        self._normalized_package_name = value

    @property
    def package_query_status(self) -> bool:
        """
        Returns the query status of the package (True if exists, False otherwise).

        This raises a ValueError if the status hasn't been set by a subclass.
        """
        if self._package_query_status is None:
            raise ValueError("Package query status has not been set.")
        return self._package_query_status

    @package_query_status.setter
    def package_query_status(self, value: bool):
        """
        Sets the query status for the package.
        
        Allows subclasses to update whether the package exists or not.
        
        Args:
            value (bool): The package query status (True if exists, False otherwise).
        
        Raises:
            TypeError: If the value is not a boolean.
        """
        if not isinstance(value, bool):
            raise TypeError("Package query status must be a boolean.")
        self._package_query_status = value

    @property
    def package_information(self) -> dict:
        """
        Returns the package metadata.

        This raises a ValueError if the package information hasn't been set by a subclass.
        """
        if self._package_information is None:
            raise ValueError("Package information has not been set.")
        return self._package_information

    @package_information.setter
    def package_information(self, value: dict):
        """
        Sets the package metadata information.
        
        Allows subclasses to update the package metadata.
        
        Args:
            value (dict): A dictionary containing package metadata information.
        
        Raises:
            TypeError: If the value is not a dictionary.
        """
        if not isinstance(value, dict):
            raise TypeError("Package information must be a dictionary.")
        self._package_information = value

    """ Enforce methods with abstract methods """

    @abstractmethod
    def get_normalized_package_name(self) -> str:
        """
        Computes and returns the normalized package name based on specific naming conventions.
        
        This method is abstract and must be implemented by subclasses.

        Returns:
            str: The normalized package name.
        """
        pass  # Subclasses must implement this method

    @abstractmethod
    def search_package_list(self) -> tuple[bool, dict]:
        """
        Searches for the package in the package manager or repository.
        
        Returns a tuple containing:
            - A boolean indicating whether the package exists or not.
            - A dictionary containing the package's metadata.
        
        This method is abstract and must be implemented by subclasses.

        Returns:
            tuple: (bool, dict) containing the package status and package information.
        """
        pass

    def get_package_query_url(self) -> str:
        """
        Returns the URL used to query the package information.

        This method is meant to be overridden by subclasses. For PyPI, the default 
        implementation constructs the query URL based on the package name.

        Returns:
            str: The package query URL.
        """
        # Default URL construction for PyPi, but this can be overridden by subclasses.
        return f"https://pypi.org/pypi/{self._input_package_name}/json"
