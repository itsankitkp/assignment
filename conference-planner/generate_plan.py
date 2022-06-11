import sys
import os

from app.main import entrypoint

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 2:
        print(f"File path containing conference details are not specified")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Given file path {file_path} is invalid ")
        sys.exit(1)
    entrypoint(file_path)
