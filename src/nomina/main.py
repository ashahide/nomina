import sys

from .cli import make_parser
from .search import search_pypi
parser = make_parser.make_parser()


if __name__ == "__main__":

    args = parser.parse_args()

    match args.environment:

        case "pypi":

            table, search_dict = search_pypi.main(args)
            
        case _:
            raise ModuleNotFoundError(f"Environment {args.environment} not found.")
        
    print(table)