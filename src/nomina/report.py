from .search.schema.schema import SearchResults
import tabulate


def create_output_table(package_search_results: list[SearchResults]) -> str:
    """
    Format a list of SearchResults objects into a grid-style table for display.

    Args:
        package_search_results (list[SearchResults]): A list of search results from different package checks.

    Returns:
        str: A string representation of the results in a table format using `tabulate`.
    """
    # Initialize table with column headers
    table = [["Input Name", "Normalized Name", "Status", "Message"]]

    # Populate the table with result rows
    for package in package_search_results:
        table.append(
            [
                package.user_input_package_name,
                package.normalized_package_name or "",  # empty string if None
                "True" if package.package_exists else "False",
                package.search_response_message,
            ]
        )

    # Generate formatted output table
    return tabulate.tabulate(table, headers="firstrow", tablefmt="grid")
