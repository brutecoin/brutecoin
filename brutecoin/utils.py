import math
import random


def format_as_hex(number, length=64):
    return f'{hex(number)[2:]:0>{length}}'


def generate_hex_in_range(start, stop):
    return format_as_hex(random.randrange(start, stop + 1))


def split_range(start, stop, max_parts):
    if max_parts < 1:
        raise ValueError("max_parts cannot be less then 1")

    width = math.ceil((stop - start + 1) / max_parts)

    while start <= stop:
        yield (start, min(start + width - 1, stop))
        start += width
