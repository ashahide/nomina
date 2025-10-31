from .cli.make_parser import make_parser
from .search.main import run_package_search


def run():
    parser = make_parser()

    args = parser.parse_args()

    results = run_package_search(args)

    print(results)

    return


if __name__ == "__main__":
    run()
