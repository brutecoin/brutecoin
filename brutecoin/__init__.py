from argparse import ArgumentParser

from .core import processing


def main(argv):
    arg_parser = ArgumentParser(
        prog='brutecoin',
        description='Application for brute-force private keys and the '
                    'corresponding addresses of Bitcoin puzzle transaction',
        add_help=False
    )

    args = arg_parser.parse_args(argv)

    processing(args)
