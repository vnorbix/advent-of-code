import pathlib
import statistics
import sys
from typing import List

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [int(num) for num in puzzle_input.split(',')]


def part1(crab_positions: List[int]):
    return sum(abs(statistics.median(crab_positions) - p) for p in crab_positions)

def calculate_cost_by_distance(distance):
    return distance * (distance + 1) / 2

def part2(crab_positions: List[int]):
    check_range = (min(crab_positions), max(crab_positions))
    best_cost = 1e9
    for position_to_calculate in range(*check_range):
        fuel_cost = sum(calculate_cost_by_distance(abs(actual_position - position_to_calculate)) for actual_position in crab_positions)
        best_cost = min(best_cost, fuel_cost)
    return best_cost



if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"How much fuel must they spend to align to that position? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        print(
            f"How much fuel must they spend to align to that position? "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")
