import pathlib
import sys

import parse
from colorama import Fore, Style


def parse_input(puzzle_input):
    return [parse.search("{direction} {value:d}", line.strip()).named for line in puzzle_input.split('\n')]


def part1(data):
    horizontal_position = 0
    depth = 0

    for command in data:
        direction = command["direction"]
        value = command["value"]
        if direction == "forward":
            horizontal_position += value
        elif direction == "up":
            depth -= value
        elif direction == "down":
            depth += value

        if depth < 0:
            depth = 0

    return depth * horizontal_position


def part2(data):
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in data:
        direction = command["direction"]
        value = command["value"]
        if direction == "forward":
            horizontal_position += value
            depth += aim * value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value

    return depth * horizontal_position


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"What do you get if you multiply your final horizontal position by your final "
            f"depth? {Fore.RED} {part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        print(
            f"W What do you get if you multiply your final horizontal position "
            f"by your final depth? {Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")