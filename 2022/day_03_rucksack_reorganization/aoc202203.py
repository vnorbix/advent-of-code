import pathlib
import sys
from dataclasses import dataclass
from itertools import islice

from colorama import Fore, Style


def find_item_duplicate(item_lists):
    item_sets = list(map(set, item_lists))
    return item_sets[0].intersection(*item_sets[1:]).pop()


def find_item_priority(item):
    if ord(item) >= ord('a'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def group_elves_rucksacks(item_lists):
    it = iter(item_lists)
    while batch := list(islice(it, 3)):
        yield batch


def split_rucksack_to_compartments(items):
    compartment_size = len(items) // 2
    return [items[:compartment_size], items[compartment_size:]]


def parse_input(puzzle_input):
    return puzzle_input.split('\n')


def part1(rucksacks):
    return sum(
        find_item_priority(
            find_item_duplicate(split_rucksack_to_compartments(rucksack))
        ) for rucksack in rucksacks
    )


def part2(rucksacks):
    rucksack_groups = group_elves_rucksacks(rucksacks)
    return sum(
        find_item_priority(find_item_duplicate(rucksack_group)) for rucksack_group in rucksack_groups
    )


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"What is the sum of the priorities of the item types which appear is both compartments of each rucksack? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"What is the sum of the priorities of the batch item types of each three-Elf group? "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")
