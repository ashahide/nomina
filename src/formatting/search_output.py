import tabulate

def create_pypi_output_table(package_name, normalized_name, status, message):

    assert isinstance(package_name, list), "package_name must be a list"
    assert isinstance(normalized_name, list), "normalized_name must be a list"
    assert isinstance(status, list), "status must be a list"
    assert isinstance(message, list), "message must be a list"

    assert len(package_name) == len(normalized_name)== len(status) == len(message), "package_name, normalized_name, status, and message must be lists of the same size"

    table = [
        ["Package Name", "Normalized Name", "Status", "Message"]
    ] + list(zip(package_name, normalized_name, status, message))

    return tabulate.tabulate(table, headers="firstrow", tablefmt="grid")