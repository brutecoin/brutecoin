import random


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
    generator = generate_private_keys(args.start, args.stop, args.limit)
    if args.keys_path:
        with open(args.keys_path, 'a') as fp:
            for key in generator:
                fp.write(key + '\n')
    else:
        for key in generator:
            print(key)
