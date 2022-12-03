import pathlib

import numpy as np
import pytest

import aoc202103 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    assert np.allclose(
        example1,
        np.array(
            [
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0]
            ]
        )
    )


def test_part1_example1(example1):
    assert aoc.part1(example1) == 198


def test_part2_example1(example1):
    assert aoc.part2(example1) == 230


def test_part1_improved(example1):
    puzzle_input = aoc.parse_input_improved((PUZZLE_DIR / "input.txt").read_text())
    assert aoc.part1_improved(puzzle_input) == 1082324

def test_part2_improved(example1):
    puzzle_input = aoc.parse_input_improved((PUZZLE_DIR / "input.txt").read_text())
    assert aoc.part2_improved(puzzle_input) == 1353024