import pathlib

import pytest

from aoc202201 import parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())


def test_parse_input():
    puzzle_input = parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())
    assert puzzle_input == [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]


def test_part1_example1(example1):
    assert part1(example1) == 24000


def test_part2_example1(example1):
    assert part2(example1) == 45000


