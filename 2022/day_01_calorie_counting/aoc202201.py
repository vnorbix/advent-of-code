import pathlib
import sys

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [list(map(int, elf_items.split('\n'))) for elf_items in puzzle_input.split('\n\n')]


def part1(data):
    return max(map(sum, data))


def part2(data):
    return sum(sorted(map(sum, data))[-3:])


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"How many calories the elf carried who carried the most calories? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"How many calories the first 3 elves carried altogether who carried the most calories? "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")
