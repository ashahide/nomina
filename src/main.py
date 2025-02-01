import sys

import cli.make_parser
import search

import formatting.search_output
import search.search_pypi

parser = cli.make_parser.make_parser()


if __name__ == "__main__":

    args = parser.parse_args()

    match args.environment:

        case "pypi":

            table, search_dict = search.search_pypi.main(args)
            
        case _:
            raise ModuleNotFoundError(f"Environment {args.environment} not found.")
        
    print(table)