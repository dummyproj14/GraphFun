# /usr/bin/python
# Command line interface (CLI) for friendly user interaction

import argparse as argp

from .manager import manager

parser = argp.ArgumentParser("Command Line Interface (CLI) for playersMindset")
parser.add_argument("input_filepath", help="Input text filepath containing data entries")

if __name__ == '__main__':
    args = parser.parse_args()
    manager(args.input_filepath)
