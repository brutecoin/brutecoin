import logging
from multiprocessing import Process
from pathlib import Path

import bitcoin

from brutecoin.utils import generate_hex_in_range, split_range


logger = logging.getLogger(__name__)


def addresses_generator(keys):
    yield from map(bitcoin.privtoaddr, keys)


def read_keys(keys_path):
    with open(keys_path) as fp:
        yield from (line.strip() for line in fp.readlines())


def key_generator(start, stop, limit=None):
    num = 0
    while limit is None or num < limit:
        yield generate_hex_in_range(start, stop)
        num += 1


def addresses_processing(keys_path, compressed=True):
    keys = read_keys(keys_path)
    if compressed:
        keys = (bitcoin.encode_privkey(k, 'wif_compressed') for k in keys)

    generator = addresses_generator(keys)

    for address in generator:
        logger.info(address)


def keys_processing(keys_path, limit, start, stop):
    generator = key_generator(start, stop, limit)
    if keys_path:
        with open(keys_path, 'a') as fp:
            for key in generator:
                fp.write(key + '\n')
    else:
        for key in generator:
            logger.info(key)


def add_suffix_to_path(path: Path, suffix: str) -> Path:
    return path.with_suffix(f'{path.suffix}.{suffix}')


def processing(args):
    if args.mode == 'pk':
        # Split the range between all processes
        ranges = split_range(args.start, args.stop, args.processes)

        processes = [
            Process(
                target=keys_processing,
                kwargs={
                    'keys_path': (
                        args.keys_path
                        and add_suffix_to_path(args.keys_path, start)
                    ),
                    'limit': args.limit,
                    'start': start,
                    'stop': stop,
                },
            )
            for start, stop in ranges
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()
    elif args.mode == 'addr':
        addresses_processing(args.keys_path)
