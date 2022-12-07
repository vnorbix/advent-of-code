import pathlib

import pytest

from aoc202207 import parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text()) == {
        '/': {
            'a': {
                'e': {
                    'i': 584
                },
                'f': 29116,
                'g': 2557,
                'h.lst': 62596
            },
            'b.txt': 14848514,
            'c.dat': 8504156,
            'd': {
                'j': 4060174,
                'd.log': 8033020,
                'd.ext': 5626152,
                'k': 7214296
            }
        }
    }


def test_part1_example(example):
    assert part1(example) == 95437


def test_part2_example(example):
    assert part2(example) == 24933642
