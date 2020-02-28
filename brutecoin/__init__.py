from argparse import ArgumentParser
from pathlib import Path

from .core import processing

MODE_ADDR = 'addr'
MODE_PK = 'pk'
MODE_CHOICES = (MODE_ADDR, MODE_PK)


def int_or_hex(string):
    if isinstance(string, str):
        return int(string, 16)
    else:
        return int(string)


def main(argv):
    arg_parser = ArgumentParser(
        prog='brutecoin',
        description='Application for brute-force private keys and the '
        'corresponding addresses of Bitcoin puzzle transaction',
        add_help=False,
    )

    # Positional argument
    arg_parser.add_argument(
        'mode', type=str, choices=MODE_CHOICES, help='limit of the keys number'
    )

    # Optional arguments
    arg_parser.add_argument(
        '--keys-path',
        dest='keys_path',
        type=Path,
        default=None,
        help='keys file path',
    )

    arg_parser.add_argument(
        '--limit',
        type=int,
        default='1',
        help='limit of the keys number per process',
    )

    arg_parser.add_argument(
        '--processes', type=int, default='1', help='number of processes'
    )

    arg_parser.add_argument(
        '--start',
        type=int_or_hex,
        default='1',
        help='lower bound of private key range',
    )

    arg_parser.add_argument(
        '--stop',
        type=int_or_hex,
        default='1',
        help='upper bound of private key range',
    )

    args = arg_parser.parse_args(argv)

    if args.mode == MODE_ADDR and not args.keys_path:
        raise ValueError('In the specified mode, `keys_path` is required')

    processing(args)
