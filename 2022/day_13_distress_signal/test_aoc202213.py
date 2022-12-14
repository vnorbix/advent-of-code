import pathlib

import pytest

from aoc202213 import compare, parse_input, part1, part2

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    return parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text())


def test_parse_input():
    assert parse_input(pathlib.Path(PUZZLE_DIR / 'example1.txt').read_text()) == [
        ([1, 1, 3, 1, 1],
         [1, 1, 5, 1, 1]),

        ([[1], [2, 3, 4]],
            [[1], 4]),

        ([9],
         [[8, 7, 6]]),

        ([[4, 4], 4, 4],
         [[4, 4], 4, 4, 4]),

        ([7, 7, 7, 7],
            [7, 7, 7]),

        ([],
         [3]),

        ([[[]]],
         [[]]),

        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
         [1, [2, [3, [4, [5, 6, 0]]]], 8, 9])
    ]


def test_integers():
    """
    If both values are integers, the lower integer should come first. If the left
    integer is lower than the right integer, the inputs are in the right order. If
    the left integer is higher than the right integer, the inputs are not in the
    right order. Otherwise, the inputs are the same integer; continue checking
    the next part of the input.
    """
    assert compare(1, 2) > 0 
    assert compare(2, 1 )< 0


def test_list():
    """
    If both values are lists, compare the first value of each list, then the second
    value, and so on. If the left list runs out of items first, the inputs are in
    the right order. If the right list runs out of items first, the inputs are not
    in the right order. If the lists are the same length and no comparison makes a
    decision about the order, continue checking the next part of the input.
    """
    assert compare([1, 2], [2, 2]) > 0
    assert compare([2, 2], [1, 2]) < 0
    assert compare([1], [1, 2]) > 0
    assert compare([1, 1], [1]) < 0


def test_integer_list():
    """
    If exactly one value is an integer, convert the integer to a list which contains
    that integer as its only value, then retry the comparison. For example, if
    comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2);
    the result is then found by instead comparing [0,0,0] and [2].
    """
    assert compare([[0, 0, 0]], [2]) > 0


def test_pair1():
    """
    == Pair 1 ==
    - Compare [1,1,3,1,1] vs [1,1,5,1,1]
        - Compare 1 vs 1
        - Compare 1 vs 1
        - Compare 3 vs 5
            - Left side is smaller, so inputs are in the right order
    """
    assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) > 0


def test_pair2():
    """
    - Compare [[1],[2,3,4]] vs [[1],4]
        - Compare [1] vs [1]
            - Compare 1 vs 1
        - Compare [2,3,4] vs 4
            - Mixed types; convert right to [4] and retry comparison
            - Compare [2,3,4] vs [4]
            - Compare 2 vs 4
                - Left side is smaller, so inputs are in the right order
    """
    assert compare([[1], [2, 3, 4]], [[1], 4]) > 0


def test_pair3():
    """
    - Compare [9] vs [[8,7,6]]
        - Compare 9 vs [8,7,6]
            - Mixed types; convert left to [9] and retry comparison
            - Compare [9] vs [8,7,6]
                - Compare 9 vs 8
                    - Right side is smaller, so inputs are not in the right order
    """
    assert compare([9], [[8, 7, 6]]) < 0


def test_pair4():
    """
    - Compare [[4,4],4,4] vs [[4,4],4,4,4]
        - Compare [4,4] vs [4,4]
            - Compare 4 vs 4
            - Compare 4 vs 4
        - Compare 4 vs 4
        - Compare 4 vs 4
        - Left side ran out of items, so inputs are in the right order
    """
    assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) > 0


def test_pair5():
    """
    - Compare [7,7,7,7] vs [7,7,7]
        - Compare 7 vs 7
        - Compare 7 vs 7
        - Compare 7 vs 7
        - Right side ran out of items, so inputs are not in the right order
    """
    assert compare([7, 7, 7, 7], [7, 7, 7]) < 0


def test_pair6():
    """
    - Compare [] vs [3]
        - Left side ran out of items, so inputs are in the right order
    """
    assert compare([], [3]) > 0 


def test_pair7():
    """
    - Compare [[[]]] vs [[]]
        - Compare [[]] vs []
            - Right side ran out of items, so inputs are not in the right order
    """
    assert compare([[[]]], [[]]) < 0


def test_pair8():
    """
    - Compare [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
        - Compare 1 vs 1
        - Compare [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
            - Compare 2 vs 2
            - Compare [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
                - Compare 3 vs 3
                - Compare [4,[5,6,7]] vs [4,[5,6,0]]
                    - Compare 4 vs 4
                    - Compare [5,6,7] vs [5,6,0]
                        - Compare 5 vs 5
                        - Compare 6 vs 6
                        - Compare 7 vs 0
                            - Right side is smaller, so inputs are not in the right order
    """
    assert compare([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [
                              1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) < 0

def test_error_case():
    assert compare([[[1], 8, 3, 7, 10]], 
    [[[[1], [9, 2, 0, 6], 6, [5, 4, 7], [1, 9, 4]], 7, 0, []], [2, 4], [[9, 9, [10, 5, 5], 6], 3, 0, [[1, 8], [], 10, 0], 10]]) > 0


def test_part1(example1):
    assert part1(example1) == 13


def test_part2(example1):
    assert part2(example1) == 140
