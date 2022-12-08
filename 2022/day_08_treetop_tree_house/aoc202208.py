import pathlib
import sys
from typing import Any

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [[int(c) for c in line] for line in puzzle_input.split('\n')]


def is_tree_visible(trees_to_check, tree_height):
    print(f"is_tree_visible {trees_to_check}?")
    ret = not any([t >= tree_height for t in trees_to_check])
    print(f"{ret}")
    return ret


def part1(tree_map):
    # Assume it's square
    size = len(tree_map)
    trees_visible = 0
    transposed = [[row[i] for row in tree_map] for i in range(len(tree_map[0]))]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            tree_height = tree_map[i][j]
            print(f"{tree_height} - {i} {j}")
            if is_tree_visible(tree_map[i][0:j], tree_height) or \
                    is_tree_visible(transposed[j][0:i], tree_height) or \
                    is_tree_visible(tree_map[i][j + 1:size], tree_height) or \
                    is_tree_visible(transposed[j][i + 1:size], tree_height):
                trees_visible += 1
    return trees_visible + size * 4 - 4


def find_trees_around(trees_to_check: list[int], tree_height, reverse_check=False):
    print(f"find_trees_around {trees_to_check}?")
    trees_num = 0
    if reverse_check:
        trees_to_check = reversed(trees_to_check)
    for t in trees_to_check:
        trees_num += 1
        if t >= tree_height:
            break
    ret = trees_num
    print(f"{ret}")
    return ret


def part2(tree_map):
    # Assume it's square
    size = len(tree_map)
    max_scenic_score = 0
    transposed = [[row[i] for row in tree_map] for i in range(len(tree_map[0]))]
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            tree_height = tree_map[i][j]
            print(f"{tree_height} - {i} {j}")
            scenic_score = find_trees_around(tree_map[i][0:j], tree_height, True) * \
                           find_trees_around(transposed[j][0:i], tree_height, True) * \
                           find_trees_around(tree_map[i][j + 1:size], tree_height) * \
                           find_trees_around(transposed[j][i + 1:size], tree_height)
            print(f"{scenic_score=}")
            max_scenic_score = max(scenic_score, max_scenic_score)
    return max_scenic_score


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"How many trees are visible from outside the grid? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"What is the highest scenic score possible for any tree? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
