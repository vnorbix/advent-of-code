import pathlib

import numpy as np
import pytest

import aoc202104 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    drawn_numbers, boards = example1
    assert drawn_numbers == [7,
                             4,
                             9,
                             5,
                             11,
                             17,
                             23,
                             2,
                             0,
                             14,
                             21,
                             24,
                             10,
                             16,
                             13,
                             6,
                             15,
                             25,
                             12,
                             22,
                             18,
                             20,
                             8,
                             19,
                             3,
                             26,
                             1]
    assert np.allclose(
        boards,
        np.array(
            [
                [
                    [22, 13, 17, 11, 0],
                    [8, 2, 23, 4, 24],
                    [21, 9, 14, 16, 7],
                    [6, 10, 3, 18, 5],
                    [1, 12, 20, 15, 19],
                ],
                [
                    [3, 15, 0, 2, 22],
                    [9, 18, 13, 17, 5],
                    [19, 8, 7, 25, 23],
                    [20, 11, 10, 24, 4],
                    [14, 21, 16, 12, 6]
                ],
                [
                    [14, 21, 17, 24, 4],
                    [10, 16, 15, 9, 19],
                    [18, 8, 23, 26, 20],
                    [22, 11, 13, 6, 5],
                    [2, 0, 12, 3, 7]
                ]
            ]
        )
    )


def test_part1_example1(example1):
    assert aoc.part1(example1) == 4512

def test_part2_example1(example1):
    assert aoc.part2(example1) == 1924
