from .cli import make_parser
from .search import search_pypi


def main():
    
    parser = make_parser.make_parser()

    args = parser.parse_args()

    match args.environment:

        case "pypi":

            table, search_dict = search_pypi.main(args)
            
        case _:
            raise ModuleNotFoundError(f"Environment {args.environment} not found.")
        
    print(table)