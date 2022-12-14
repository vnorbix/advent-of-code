import pathlib

import pytest

from aoc202211 import Monkey, parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())[0] == Monkey(
        items=(79, 98), op='old * 19', divisible_by=23, if_true=2, if_false=3)


def test_part1(example1):
    assert part1(example1) == 10605


def test_part2(example1):
    assert part2(example1) == 2713310158
