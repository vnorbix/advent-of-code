import pathlib
import string
import sys
from collections import defaultdict

import parse
from colorama import Fore, Style


def parse_crate_state(text):
    state = defaultdict(list)
    for line in text.split('\n'):
        for i, crate_letter in enumerate(line[1::4]):
            if crate_letter in string.ascii_uppercase:
                state[i + 1].insert(0, crate_letter)
    return dict(state)


def parse_instructions(text):
    return [parse.parse('move {move:d} from {from:d} to {to:d}', line).named for line in text.split('\n')]


def parse_input(puzzle_input):
    crate_state_text, instructions_text = puzzle_input.split('\n\n')
    return parse_crate_state(crate_state_text), parse_instructions(instructions_text)


def print_step(i, crate_state, instruction):
    print(crate_state)
    print(f'line {i + 1}: move {instruction["move"]} from {instruction["from"]} to {instruction["to"]}')


def part1(crate_state, instructions):
    for instruction in instructions:
        for i in range(instruction['move']):
            crate = crate_state[instruction['from']].pop()
            crate_state[instruction['to']].append(crate)
    return ''.join([item[1][-1] for item in sorted(crate_state.items())])


def part2(crate_state, instructions):
    for instruction in instructions:
        crates = crate_state[instruction['from']][-1 * instruction['move']:]
        crate_state[instruction['to']] += crates
        del crate_state[instruction['from']][-1 * instruction['move']:]
    return ''.join([item[1][-1] for item in sorted(crate_state.items())])


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        crate_state, instructions = parse_input(pathlib.Path(path).read_text())
        print(
            f"After the rearrangement procedure completes, what crate ends up on top of each stack? "
            f"{Fore.RED}{part1(crate_state, instructions)}{Style.RESET_ALL}")
        crate_state, instructions = parse_input(pathlib.Path(path).read_text())
        print(
            f"After the rearrangement procedure completes, what crate ends up on top of each stack? "
            f"{Fore.RED}{part2(crate_state, instructions)}{Style.RESET_ALL}")
