#!/usr/bin/env python3
import sys

import yaml

from .program import Program


def main():
    if len(sys.argv) < 2:
        print("USAGE: python3 -m robot_overlord PROGRAM")
        sys.exit(1)

    with open(sys.argv[1]) as arg_file:
        args = yaml.safe_load(arg_file)

    program = Program(**args)
    program.install_requirements()
    program.fetch()
    program.setup()
    program.run()


if __name__ == "__main__":
    main()
