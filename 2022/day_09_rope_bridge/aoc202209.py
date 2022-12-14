import pathlib
import sys
from typing import Any

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [[line.split()[0], int(line.split()[1])] for line in
            puzzle_input.split('\n')]


def part1(moves):
    pass


def part2(moves):
    move_transformation = {
        'R': [1, 0],
        'L': [-1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }
    knots = [[0, 0] for i in range(10)]
    tail_touched_positions = {tuple(knots[0])}
    tail_touched_positions2 = []
    for move in moves:
        trf = move_transformation[move[0]]
        for i in range(move[1]):
            knots[0][0] = trf[0] + knots[0][0]
            knots[0][1] = trf[1] + knots[0][1]

            knot_pairs = list(zip(knots, knots[1:]))
            for knot_pair in knot_pairs:
                diff = [knot_pair[0][0] - knot_pair[1][0], knot_pair[0][1] - knot_pair[1][1]]
                if any([abs(diff[0]) > 1, abs(diff[1]) > 1]):
                    knot_pair[1][0] += (1 if diff[0] > 0 else -1) if diff[0] != 0 else 0
                    knot_pair[1][1] += (1 if diff[1] > 0 else -1) if diff[1] != 0 else 0
            tail = knots[-1]
            tail_touched_positions.add(tuple(tail))
            tail_touched_positions2.append(tuple(tail))
    return len(tail_touched_positions)


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"How many positions does the tail of the rope visit at least once? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"How many positions does the tail of the rope visit at least once? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
