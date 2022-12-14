import pathlib

import pytest

from aoc202209 import parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())

@pytest.fixture
def example2():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example2.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text()) == [['R', 4], ['U', 4], ['L', 3],
                                                                                  ['D', 1], ['R', 4], ['D', 1],
                                                                                  ['L', 5], ['R', 2]]


def test_part1_example(example1):
    assert part1(example1) == 13


def test_part2_example(example2):
    assert part2(example2) == 36
