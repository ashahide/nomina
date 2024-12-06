import argparse

def main():
    parser = argparse.ArgumentParser(description="My Command Line Tool")
    parser.add_argument('--name', help="Your name", required=True)
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if '__main__' == __name__:
    main()