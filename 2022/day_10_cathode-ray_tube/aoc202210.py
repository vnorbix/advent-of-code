from collections import deque
import pathlib
import sys
from typing import Any
import parse

from colorama import Fore, Style


def parse_input(puzzle_input):
    def parse_line(line):
        if len(line) > 1:
            return (line[0], int(line[1]))
        return (line[0],)
    return [parse_line(line.split()) for line in puzzle_input.split('\n')]


def part1(ops):
    op_cycles = {
        'noop': 1,
        'addx': 2
    }
    cycles = 0
    cycles_to_find = deque([20, 60, 100, 140, 180, 220])
    signal_strengths = []
    x = 1
    for op in ops:
        for _ in range(op_cycles[op[0]]):
            cycles += 1
            print(f'{cycles=} {op=}')
            if len(cycles_to_find) != 0 and cycles_to_find[0] == cycles:
                signal_strengths.append(x * cycles)
                cycles_to_find.popleft()
        if op[0] == 'addx':
            x += op[1]
    return sum(signal_strengths)


def get_sprite_line(sprite_center):
    sprite_left = max(sprite_center - 1, 0)
    return '.' * sprite_left + '#' * 3 + '.' * (40 - 3 - sprite_left)


def part2(ops):
    op_cycles = {
        'noop': 1,
        'addx': 2
    }
    cycles = 0
    x = 1
    screen = [[]]
    screen_index = 0
    for op in ops:
        for _ in range(op_cycles[op[0]]):
            if screen_index == 40:
                screen_index = 0
                screen.append([])
            screen[-1].append(get_sprite_line(x)[screen_index])
            screen_index += 1
            cycles += 1
            print(f'{cycles=} {op=}')
        if op[0] == 'addx':
            x += op[1]
    s = ''
    for line in screen:
        s += ''.join(line) + '\n'
    return s


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"What is the sum of the six signal strengths? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"\n{Fore.RED}{part2(data)}{Style.RESET_ALL}")
