import pathlib
import sys
from typing import List, Tuple

import numpy as np
import parse
from colorama import Fore, Style


def parse_input(puzzle_input):
    def result_to_coords(result):
        return (result[0], result[1]), (result[2], result[3])
    return [result_to_coords(parse.search("{:d},{:d} -> {:d},{:d}", line.strip())) for line in puzzle_input.split('\n')]


def part1(data: List[Tuple[Tuple[int, int]]]):
    return calculate_vents(data)


def part2(data: List[Tuple[Tuple[int, int]]]):
    return calculate_vents(data, True)


def calculate_vents(data, include_diagonals=False):
    vent_map = np.zeros((2000, 2000), int)
    for vector in data:
        x1, y1 = vector[0][0], vector[0][1]
        x2, y2 = vector[1][0], vector[1][1]
        if x1 == x2:
            # horizontal
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vent_map[y][x1] += 1
        elif y1 == y2:
            # vertical
            for x in range(min(x1, x2), max(x1, x2) + 1):
                vent_map[y1][x] += 1
        elif include_diagonals:
            # diagonal
            # NW -> SE: 2,0 -> 4,2 or 4,2 -> 2,0
            # SW -> NE: 1,2 -> 3,0 or 3,0 -> 1,2
            min_x, max_x = min(x1, x2), max(x1, x2)
            if min_x == x1:
                y = y1
                y_incr = 1 if y2 > y1 else -1
            else:
                y = y2
                y_incr = -1 if y2 > y1 else 1
            for x in range(min_x, max_x + 1):
                vent_map[y][x] += 1
                y += y_incr

    return np.bincount(vent_map.flatten())[2:].sum()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"At how many points do at least two lines overlap? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        print(
            f"At how many points do at least two lines overlap? "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")
