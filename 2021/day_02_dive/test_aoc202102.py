import pathlib

import pytest

import aoc202102 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [
        {"direction": "forward", "value": 5},
        {"direction": "down", "value": 5},
        {"direction": "forward", "value": 8},
        {"direction": "up", "value": 3},
        {"direction": "down", "value": 8},
        {"direction": "forward", "value": 2}
    ]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 150


def test_part2_example1(example1):
    assert aoc.part2(example1) == 900
