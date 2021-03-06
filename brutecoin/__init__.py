from argparse import ArgumentParser
from pathlib import Path

from .core import processing


def main(argv):
    arg_parser = ArgumentParser(
        prog='brutecoin',
        description='Application for brute-force private keys and the '
                    'corresponding addresses of Bitcoin puzzle transaction',
        add_help=False
    )

    arg_parser.add_argument(
        '--keys-path',
        dest='keys_path',
        type=Path,
        default=None,
        help='keys file path'
    )

    arg_parser.add_argument(
        '--limit',
        type=int,
        default='1',
        help='limit of the keys number per process'
    )

    arg_parser.add_argument(
        '--processes',
        type=int,
        default='1',
        help='number of processes'
    )

    arg_parser.add_argument(
        '--start',
        type=int,
        default='1',
        help='lower bound of private key range'
    )

    arg_parser.add_argument(
        '--stop',
        type=int,
        default='1',
        help='upper bound of private key range'
    )

    args = arg_parser.parse_args(argv)

    processing(args)
