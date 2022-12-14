import pathlib

import pytest

from aoc202212 import find_possible_neighbors, find_start_end, node_value, parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text()) == [
        ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
        ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
        ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
        ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
        ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
    ]

def test_find_start_end(example1):
    assert find_start_end(example1) == ((0, 0), (2, 5))

def test_find_possible_neighbors(example1):
    assert list(find_possible_neighbors(example1, (0, 0))) == [(0, 1), (1, 0)]
    assert list(find_possible_neighbors(example1, (4, 0))) == [(4, 1), (3, 0)]
    assert list(find_possible_neighbors(example1, (4, 7))) == [(3, 7), (4, 6)]
    assert list(find_possible_neighbors(example1, (0, 7))) == [(1, 7), (0, 6)]
    assert list(find_possible_neighbors(example1, (2, 2))) == [(3, 2), (1, 2), (2, 1)]
    assert list(find_possible_neighbors(example1, (4, 1))) == [(3, 1), (4, 0)]
    assert list(find_possible_neighbors(example1, (2, 6))) == [(2, 7), (3, 6), (1, 6)]

def test_node_value(example1):
    assert node_value(example1, (0, 0)) == 0
    assert node_value(example1, (0, 2)) == 1
    assert node_value(example1, (2, 5)) == 24

def test_part1(example1):
    assert part1(example1) == 31


def test_part2(example1):
    assert part2(example1) == 2713310158

