import os
import sys

from app.main import entrypoint


def main():
    if len(sys.argv) != 2:
        raise Exception(f"File path containing conference details are not specified")

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        raise Exception(f"Given file path {file_path} is invalid ")

    entrypoint(file_path)


if __name__ == "__main__":
    main()
