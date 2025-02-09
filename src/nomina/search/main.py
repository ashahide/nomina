from .search_pypi import PyPiPackage, SearchResults

import tabulate


""" Create Table to Display Output """


def create_output_table(package_search_results):
    table = [["Package Name", "Normalized Name", "Status", "Message"]]

    for package in package_search_results:
        breakpoint()

        table.append(
            [
                package.user_input_package_name,
                package.normalized_package_name,
                package.package_exists,
                package.search_response_message,
            ]
        )

    return tabulate.tabulate(table, headers="firstrow", tablefmt="grid")


""" Main Search Function """


def run_package_search(args):
    # List to store the package instances (representing the search results for each package)
    package_results = []

    # Define class
    match args.environment:
        case "pypi":
            search_class = PyPiPackage
        case _:
            raise Exception(f"Unknown environment: {args.env}")

    # Iterate over each package name provided in the arguments
    for name in args.name:
        # Create an instance of the search class for each package name
        package_instance = search_class(name)

        # Normalize name
        package_instance.normalize_package_name()

        # Search package index
        package_instance.search_package_index()

        # Get the results
        package_search_obj = package_instance.get_search_results()
        assert isinstance(package_search_obj, SearchResults)

        # Append the results to the list
        package_results.append(package_search_obj)

    # Format the results into a table
    output_table = create_output_table(package_results)

    return output_table
