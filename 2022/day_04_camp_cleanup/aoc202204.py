import pathlib
import sys
from collections import namedtuple
from itertools import count

import parse
from colorama import Fore, Style

SectionRange = namedtuple('SectionRange', ['start', 'end'])


def parse_input(puzzle_input):
    def convert(data):
        return [SectionRange(data[0], data[1]), SectionRange(data[2], data[3])]
    return [convert(parse.search('{:d}-{:d},{:d}-{:d}', line)) for line in puzzle_input.split('\n')]


def range_contains(range_a: SectionRange, range_b: SectionRange):
    return range_b.start >= range_a.start and range_b.end <= range_a.end


def range_overlap(range_a: SectionRange, range_b: SectionRange):
    return range_b.start <= range_a.end and range_b.end >= range_a.start

def part1(pairs):
    cnt = 0
    for pair in pairs:
        if range_contains(pair[0], pair[1]) or range_contains(pair[1], pair[0]):
            cnt += 1
    return cnt


def part2(pairs):
    cnt = 0
    for pair in pairs:
        if range_overlap(pair[0], pair[1]):
            cnt += 1
    return cnt



if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = parse_input(pathlib.Path(path).read_text().strip())
        print(
            f"In how many assignment pairs does one range fully contain the other? "
            f"{Fore.RED}{part1(puzzle_input)}{Style.RESET_ALL}")
        print(
            f"In how many assignment pairs do the ranges overlap? "
            f"{Fore.RED}{part2(puzzle_input)}{Style.RESET_ALL}")
