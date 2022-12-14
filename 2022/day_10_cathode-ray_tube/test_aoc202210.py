import pathlib

import pytest

from aoc202210 import get_sprite_line, parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input('addx -1\nnoop\naddx 1') == [('addx', -1), ('noop',), ('addx', 1)]

def test_get_sprite_line():
    assert get_sprite_line(0) == '###.....................................'
    assert get_sprite_line(1) == '###.....................................'
    assert get_sprite_line(16) == '...............###......................'

def test_part1(example1):
    assert part1(example1) == 13140


def test_part2(example1):
    assert part2(example1) == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
