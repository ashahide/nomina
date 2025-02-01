import argparse

def make_parser():

    parser = argparse.ArgumentParser(description="Nomina - a CLI tool for generating Python package names.")

    parser.add_argument('name', type=str, help="Candidate package name.", nargs='+')

    return parser