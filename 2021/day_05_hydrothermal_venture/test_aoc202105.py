import pathlib

import pytest

import aoc202105 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_input(puzzle_input)


def test_parse_example1(example1):
    assert example1 == [((0, 9), (5, 9)), ((8, 0), (0, 8)), ((9, 4), (3, 4)), ((2, 2), (2, 1)), ((7, 0), (7, 4)),
                        ((6, 4), (2, 0)), ((0, 9), (2, 9)), ((3, 4), (1, 4)), ((0, 0), (8, 8)), ((5, 5), (8, 2))]


#
def test_part1_example1(example1):
    assert aoc.part1(example1) == 5


# @pytest.mark.parametrize("coordinate", [
#     ((2, 0), (4, 2)),  # NW -> SE
#     ((4, 2), (2, 0)),  # SE -> NW
#     ((1, 2), (3, 0)),  # SW -> NE
#     ((3, 0), (1, 2)),  # NE -> SW
# ])
# def test_calc_diagonal_covered_points(coordinate):
#     assert aoc.calc_diagonal_covered_points(coordinate) == 3


def test_part2_example1(example1):
    assert aoc.part2(example1) == 12
