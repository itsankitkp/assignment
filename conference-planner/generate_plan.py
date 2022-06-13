import os
import sys

from app.main import entrypoint


def main() -> None:
    """
    Calls code which reads from the specified file.
    ToDO: Implement this using args.

    Raises:
        Exception: if argu,ent is invalid or if file doesn't exists
    """

    # validate argument
    if len(sys.argv) != 2:
        raise Exception(f"File path containing conference details are not specified")

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        raise Exception(f"Given file path {file_path} is invalid ")

    # call main app
    entrypoint(file_path)


if __name__ == "__main__":
    main()
