import argparse
import os
import pathlib
import shutil
import subprocess


def clean():
    print("Cleaning project files")
    paths_to_delete = [
        pathlib.Path(i) for i in [".venv", "venv", "dist", "uv.lock", "poetry.lock"]
    ]

    for p in paths_to_delete:
        print(f">>> Deleting {p}")
        try:
            os.remove(p)
        except FileNotFoundError:
            continue
        except:
            shutil.rmtree(p)


def make_venv():
    subprocess.run(["uv", "venv"])


if __name__ == "__main__":
    """ Get the arguments """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "target",
        nargs="*",
        help="command runner target",
        choices=["clean", "make-venv"],
    )

    args = parser.parse_args()

    if args.target:
        for c in args.target:
            print(c)
            match c:
                case "clean":
                    clean()

                case "make-venv":
                    print("Making a venv")
                    clean()
                    make_venv()

                case _:
                    continue
