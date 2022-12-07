import collections
import pathlib
import string
import sys
from collections import defaultdict
from itertools import islice

import parse
from colorama import Fore, Style

MARKER_SIZE = 4


def parse_input(puzzle_input):
    return puzzle_input


def sliding_window(iterable, n):
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def find_marker(data, size):
    for i, window in enumerate(sliding_window(data, size)):
        if len(set(window)) == size:
            return i + size


def part1(data):
    return find_marker(data, 4)


def part2(data):
    return find_marker(data, 14)


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"How many characters need to be processed before the first start-of-packet marker is detected? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"How many characters need to be processed before the first start-of-message marker is detected? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
