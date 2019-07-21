from multiprocessing import Process

from brutecoin.utils import generate_hex_in_range, split_range


def key_generator(start, stop, limit=None):
    num = 0
    while limit is None or num < limit:
        yield generate_hex_in_range(start, stop)
        num += 1


def keys_processing(keys_path, limit, start, stop):
    generator = key_generator(start, stop, limit)
    if keys_path:
        with open(keys_path, 'a') as fp:
            for key in generator:
                fp.write(key + '\n')
    else:
        for key in generator:
            print(key)


def processing(args):
    # Split the range between all processes
    ranges = split_range(args.start, args.stop, args.processes)

    processes = [
        Process(
            target=keys_processing,
            kwargs=dict(
                keys_path=args.keys_path,
                limit=args.limit,
                start=start,
                stop=stop
            ))
        for start, stop in ranges
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
