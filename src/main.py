import cli.make_parser
import search.search_pypi
import formatting.search_output

parser = cli.make_parser.make_parser()


if __name__ == "__main__":

    args = parser.parse_args()

    package_names = []
    package_normalized_names = []
    package_status = []
    package_messages = []

    for name in args.name:

        status, message, normalized_name = search.search_pypi.check_pypi_package(name)

        package_names.append(name)
        package_normalized_names.append(normalized_name)
        package_status.append(status)
        package_messages.append(message)

    table = formatting.search_output.format_pypi_output(package_names, package_normalized_names, package_status, package_messages)

    print(table)