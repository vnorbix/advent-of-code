import pathlib
import sys
from functools import reduce
import matplotlib.pyplot as plt


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split()]


def part1(data):
    increases = 0
    last_depth = None
    for depth in data:
        if last_depth is not None and depth > last_depth:
            increases += 1
        last_depth = depth
    return increases


def part1_improved(data):
    return sum(1 for i in range(1, len(data)) if data[i - 1] < data[i])


def part2(data):
    """How many measurements are larger than the previous measurement?"""
    last_depth_sum = None
    increases = 0
    while len(depth_window := data[:3]) == 3:
        depth_sum = sum(depth_window)
        if last_depth_sum is not None and depth_sum > last_depth_sum:
            increases += 1
        last_depth_sum = depth_sum
        data = data[1:]
    return increases


def part2_improved(data):
    """How many sliding windows of 3 numbers are larger than the previous?"""
    WINDOW_SIZE = 3
    return sum(1 for i in range(1, len(data) - WINDOW_SIZE + 1) if
               sum(data[i - 1:i - 1 + WINDOW_SIZE]) < sum(data[i:i + WINDOW_SIZE]))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(f"How many measurements are larger than the previous measurement? {part1(parse(puzzle_input))}")
        print(f"How many sums are larger than the previous sum? {part2_improved(parse(puzzle_input))}")
        plt.plot(parse(puzzle_input))
        plt.ylabel('Depth')
        plt.gca().invert_yaxis()
        plt.show()
