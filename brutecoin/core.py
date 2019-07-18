import random


KEYS_PATH = 'keys.txt'


def format_as_hex(number, length=64):
    return f'{hex(number)[2:]:0>{length}}'


def generate_hex_in_range(start, stop):
    return format_as_hex(random.randrange(start, stop + 1))


def generate_private_keys(start, stop, limit=None):
    num = 0
    while limit is None or num < limit:
        yield generate_hex_in_range(start, stop)
        num += 1


def processing(args):
    with open(KEYS_PATH, 'a') as fp:
        for key in generate_private_keys(args.start, args.stop, args.limit):
            fp.write(key + '\n')
            print(key)
