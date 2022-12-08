import pathlib

import pytest

from aoc202208 import parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text()) == [[3, 0, 3, 7, 3],
                                                                                  [2, 5, 5, 1, 2],
                                                                                  [6, 5, 3, 3, 2],
                                                                                  [3, 3, 5, 4, 9],
                                                                                  [3, 5, 3, 9, 0]]


def test_part1_example(example):
    assert part1(example) == 21


def test_part2_example(example):
    assert part2(example) == 8
