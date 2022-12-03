import pathlib

import pytest
import aoc202101 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1_example1(example1):
    assert aoc.part1(example1) == 7


def test_part2_example1(example1):
    assert aoc.part2(example1) == 5


def test_part1_improved(example1):
    assert aoc.part1_improved(example1) == 7


def test_part2_improved(example1):
    assert aoc.part2_improved(example1) == 5
