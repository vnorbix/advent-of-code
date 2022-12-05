import pathlib
from collections import namedtuple

import pytest

from aoc202204 import range_contains, parse_input, part1, part2, SectionRange

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    puzzle_input = parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())
    assert puzzle_input[0] == [SectionRange(start=2, end=4), SectionRange(start=6, end=8)]



def test_range_contains():
    assert not range_contains(SectionRange(2, 4), SectionRange(6, 8))
    assert not range_contains(SectionRange(5, 7), SectionRange(7, 9))
    assert range_contains(SectionRange(2, 8), SectionRange(3, 7))
    assert not range_contains(SectionRange(3, 7), SectionRange(2, 8))


def test_part1_example(example):
    assert part1(example) == 2


def test_part2_example(example):
    assert part2(example) == 4
