import pathlib

import pytest

import aoc202107 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 37


def test_part2_example1(example1):
    assert aoc.part2(example1) == 168