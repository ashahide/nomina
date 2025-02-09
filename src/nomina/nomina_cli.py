from .cli import make_parser
from .search.main import run_package_search


def main():
    parser = make_parser.make_parser()

    args = parser.parse_args()

    match args.environment:
        case "pypi":
            table = run_package_search(args)

        case _:
            raise ModuleNotFoundError(f"Environment {args.environment} not found.")

    print(table)
