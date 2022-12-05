import pathlib

import pytest

from aoc202205 import parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    crate_state, instructions = parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())
    return crate_state, instructions


def test_parse_input():
    crate_state, instructions = parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())
    assert crate_state == {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    assert instructions == [
        {'from': 2, 'move': 1, 'to': 1},
        {'from': 1, 'move': 3, 'to': 3},
        {'from': 2, 'move': 2, 'to': 1},
        {'from': 1, 'move': 1, 'to': 2}
    ]


def test_part1_example(example):
    assert part1(example[0], example[1]) == 'CMZ'


def test_part2_example(example):
    assert part2(example[0], example[1]) == 'MCD'
