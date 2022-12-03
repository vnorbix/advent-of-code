import collections
import functools
import pathlib
import sys
from typing import List

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [int(num) for num in puzzle_input.split(',')]


def get_lanternfish_population(initial_fishes: List[int], days: int):
    fishes = initial_fishes
    for day in range(days):
        new_fishes = []
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                new_fishes.append(8)
            else:
                fishes[i] -= 1
        fishes += new_fishes
        print(f"After {(day + 1)} day: {len(fishes)}")
    return len(fishes)


def part1(initial_fishes: List[int]):
    collections.Counter(initial_fishes)
    return get_lanternfish_population(initial_fishes, 80)


@functools.lru_cache
def lanternfish_create_in_days(days):
    if days < 1:
        return 1

    return lanternfish_create_in_days(days - 7) + lanternfish_create_in_days(days - 9)


def part2(initial_fishes: List[int]):
    fish_counter = collections.Counter(initial_fishes)
    all_fishes = 0
    for timer, fish_count in fish_counter.items():
        all_fishes += fish_count * lanternfish_create_in_days(256 - timer)
    return all_fishes


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"ow many lanternfish would there be after 80 days? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        print(
            f"How many lanternfish would there be after 256 days? "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")