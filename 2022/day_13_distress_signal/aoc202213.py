import ast
from functools import cmp_to_key
from itertools import zip_longest
import pathlib
import sys

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [(ast.literal_eval(list_pair.split('\n')[0]), ast.literal_eval(list_pair.split('\n')[1]))
            for list_pair in puzzle_input.split('\n\n')]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, int):
        return right - left

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            if l == r:
                continue
            ret = compare(l, r)
            if ret == 0:
                # Cannot decide which value to choose
                continue
            return ret
        else:
            if len(left) != len(right):
                return len(right) - len(left)

        return 0


def part1(data):
    return sum(i if compare(*packet_pair) > 0 else 0 for i, packet_pair in enumerate(data, start=1))


def part2(data):
    data = [packet for packet_pair in data for packet in packet_pair]
    data.append([[2]])
    data.append([[6]])
    data.sort(key=cmp_to_key(compare), reverse=True)
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


if __name__ == '__main__':
    for path in sys.argv[1:]:
        # print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"What is the sum of the indices of those pairs? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"What is the decoder key for the distress signal? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
