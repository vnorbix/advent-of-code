import pathlib

import pytest

from aoc202202 import parse_input_part1, part1, part2, Round, GameAction, parse_input_part2

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example_part1():
    return parse_input_part1(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())


@pytest.fixture
def example_part2():
    return parse_input_part2(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())


def test_parse_input_part1():
    puzzle_input = parse_input_part1(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())
    assert puzzle_input == [
        Round(GameAction.ROCK, GameAction.PAPER),
        Round(GameAction.PAPER, GameAction.ROCK),
        Round(GameAction.SCISSORS, GameAction.SCISSORS)
    ]


def test_parse_input_part2():
    puzzle_input = parse_input_part2(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text().strip())
    assert puzzle_input == [
        Round(GameAction.ROCK, GameAction.ROCK),
        Round(GameAction.PAPER, GameAction.ROCK),
        Round(GameAction.SCISSORS, GameAction.ROCK)
    ]


def test_part1_example1(example_part1):
    assert part1(example_part1) == 15


def test_part2_example1(example_part2):
    assert part2(example_part2) == 12
