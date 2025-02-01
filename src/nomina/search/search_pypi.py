from ..formatting import search_output

import requests
import re

def check_pypi_package_name(package_name):

    """
    pypi naming conventions according to https://packaging.python.org/en/latest/specifications/name-normalization/
    
    """

    name_match = re.match(r'^[a-zA-Z0-9_.-]+$', package_name)

    normalized_name = re.sub(r'[-_.]+', '-', package_name).lower()

    if name_match and normalized_name == package_name:
        return True, "Valid package name", normalized_name
    
    elif name_match and normalized_name != package_name:
        return True, "Valid package name, but normalized to " + normalized_name, normalized_name
    
    else:
        return False, "Invalid package name", normalized_name



def check_pypi_package(package_name):

    name_status, name_message, normalized_name = check_pypi_package_name(package_name)

    url = f"https://pypi.org/pypi/{normalized_name}/json"

    response_try_counter = 0
    
    while response_try_counter < 5:
        try:
            response = requests.get(url)
            break
        except:
            response_try_counter += 1

    if response_try_counter == 5:
        raise Exception(f"Unable to connect to PyPI after {response_try_counter} attempts")

    match response.status_code:
        case 404:
            return False, "Package not found - Status 404", normalized_name
        
        case 200:
            return True, "Package found - Status 200", normalized_name
        
        case _:
            return False, 'Unknown error', normalized_name
        


def main(args):

    package_names = []
    package_normalized_names = []
    package_status = []
    package_messages = []

    search_dict = {}

    for name in args.name:

        status, message, normalized_name = check_pypi_package(name)

        package_names.append(name)
        package_normalized_names.append(normalized_name)
        package_status.append(status)
        package_messages.append(message)

        search_dict[name] = {"Status": status, "Message": message, "Normalized Name": normalized_name}
        
    table = search_output.create_pypi_output_table(package_names, package_normalized_names, package_status, package_messages)

    return table, search_dict