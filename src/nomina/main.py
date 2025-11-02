from .search.main import run_package_search
from .report import create_output_table
from typing import List
from .search.schema.schema import SearchResults

import argparse


def make_parser():
    parser = argparse.ArgumentParser(
        prog="nomina - a command line too for searching PyPI"
    )

    parser.add_argument("name", nargs="+")
    parser.add_argument("--table", action="store_true")

    return parser


def run() -> List[SearchResults]:
    parser = make_parser()

    args = parser.parse_args()

    results: List[SearchResults] = run_package_search(args)

    if args.table:
        table = create_output_table(results)

        print(table)

    return results


if __name__ == "__main__":
    run()
