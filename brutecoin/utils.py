import random


def format_as_hex(number, length=64):
    return f'{hex(number)[2:]:0>{length}}'


def generate_hex_in_range(start, stop):
    return format_as_hex(random.randrange(start, stop + 1))
