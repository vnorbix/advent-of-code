import pathlib

import pytest

from aoc202206 import parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text()) == 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'


def test_part1_example(example):
    assert part1(example) == 7


def test_part2_example(example):
    assert part2(example) == 19
