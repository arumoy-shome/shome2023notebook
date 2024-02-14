"""Check if the given Jupyter notebooks contains valid JSON."""

import argparse
import nbformat

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", help="Path to Jupyter Notebook.")
    args = parser.parse_args()

    try:
        nb_dict = nbformat.read(args.notebook, nbformat.NO_CONVERT)
    except Exception as err:
        print(f"ERROR:{args.notebook}:{err}")
    else:
        print(f"INFO:{args.notebook}:is valid")
