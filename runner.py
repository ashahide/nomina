import subprocess
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("target", help="Target command to run")

    args = parser.parse_args()
