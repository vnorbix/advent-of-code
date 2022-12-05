import pathlib

import pytest

from aoc202203 import part1, part2, group_elves_rucksacks, parse_input, find_item_duplicate, \
    split_rucksack_to_compartments, find_item_priority

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())


def test_parse_input():
    puzzle_input = parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().split('\n')[0])
    assert puzzle_input == [
        'vJrwpWtwJgWrhcsFMMfFFhFp'
    ]


def test_find_compartment_duplicate(example):
    assert find_item_duplicate(split_rucksack_to_compartments(example[0])) == 'p'


def test_find_priority():
    assert [find_item_priority(item) for item in ('p', 'L', 'P', 'v', 't', 's')] == [16, 38, 42, 22, 20, 19]


def test_group_elves_rucksack(example):
    groups = list(group_elves_rucksacks(example))
    assert len(groups) == 2


def test_find_item_duplicate_in_group_rucksacks(example):
    assert find_item_duplicate(example[0:3]) == 'r'
    assert find_item_duplicate(example[3:6]) == 'Z'


def test_part1_example(example):
    assert part1(example) == 157


def test_part2_example(example):
    assert part2(example) == 70
