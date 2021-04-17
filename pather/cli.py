import argparse


def cli():
    parser = argparse.ArgumentParser(prog="pather")
    subparsers = parser.add_subparsers(title="command")
    add_parser = subparsers.add_parser(name="add")
    add_parser.add_argument("source_path")
    add_parser.add_argument("name")
    add_parser.add_argument("-k", "--keep", action="store_true")
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    cli()

"""
Planning:

pather
|_____ add source_path name [-k/--keep]
|_____ release (name|--all) [-d/--dest_path dest_path] # name|--all might be tricky; multiple names?
|_____ rename name new_name
|_____ edit name
|_____ export (name|--all) [-d/--dest_path dest_path] [-i/--importable] # name|--all might be tricky; multiple names?
|_____ config
       |_____ get option
       |_____ set option value
       |_____ unset option
       |_____ list
       |_____ reset
"""
