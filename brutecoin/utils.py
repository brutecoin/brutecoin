import math
import random


def format_as_hex(number, length=64):
    return f'{hex(number)[2:]:0>{length}}'


def generate_hex_in_range(start, stop):
    return format_as_hex(random.randrange(start, stop + 1))


def split_range(start, stop, parts):
    width = math.ceil((stop - start + 1) / parts)

    while start <= stop:
        yield (start, min(start + width - 1, stop))
        start = start + width
