from nomina.cli import make_parser
from nomina.search.main import run_package_search


def main():
    parser = make_parser.make_parser()

    args = parser.parse_args()

    table = run_package_search(args)

    print(table)


if __name__ == "__main__":
    main()
