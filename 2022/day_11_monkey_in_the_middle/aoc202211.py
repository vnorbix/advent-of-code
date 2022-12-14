from collections import deque
from dataclasses import dataclass
import math
import pathlib
import sys
import parse

from colorama import Fore, Style


@dataclass
class Monkey:
    items: tuple[int]
    op: str
    divisible_by: int
    if_true: int
    if_false: int
    inspected = 0

def parse_input(puzzle_input):
    def parse_monkey(data: str):
        lines = data.split('\n')
        items = tuple(map(int, parse.parse(
            '  Starting items: {}', lines[1]).fixed[0].split(',')))
        op = parse.parse('  Operation: new = {}', lines[2]).fixed[0]
        divisible_by = parse.parse('  Test: divisible by {:d}', lines[3]).fixed[0]
        if_true = parse.parse('    If true: throw to monkey {:d}', lines[4]).fixed[0]
        if_false = parse.parse('    If false: throw to monkey {:d}', lines[5]).fixed[0]
        return Monkey(
            items,
            op,
            divisible_by,
            if_true,
            if_false
        )
    return [parse_monkey(monkey_data) for monkey_data in puzzle_input.split('\n\n')]

def run_operation(worry_level, op):
    old = worry_level
    # ex.: old * 19
    new = eval(op)
    # print(f'  Worry level after eval: {new}.')
    return new

def play(monkeys: list[Monkey], rounds: int, reduce_worry: bool):
    if not reduce_worry:
        lcm = math.lcm(*[m.divisible_by for m in monkeys])
    for round in range(rounds):
        # print(f'Round {round}')
        for monkey_idx, monkey in enumerate(monkeys):
            # print(f'  Monkey {monkey_idx}')
            for worry_level in monkey.items:
                # print(f'  Monkey inspects an item with a worry level of {worry_level}.')
                monkey.inspected += 1
                new_worry_level = run_operation(worry_level, monkey.op)
                if reduce_worry:
                    new_worry_level = new_worry_level // 3
                    # print(f'Monkey gets bored with item. Worry level is divided by 3 to {new_worry_level}.')
                else:
                    new_worry_level = new_worry_level % lcm
                if new_worry_level % monkey.divisible_by == 0:
                    pass_to = monkey.if_true
                else:
                    pass_to = monkey.if_false
                # print(f'Item with worry level {new_worry_level} is thrown to monkey {pass_to}.')
                monkeys[pass_to].items = (*monkeys[pass_to].items, new_worry_level)
            monkey.items = tuple()
        # print(f'After round {round}, the monkeys are holding items with these worry levels:')
        # for idx, m in enumerate(monkeys):
        #     print(f'Monkey {idx}: {len(m.items)} ({m.items}) (inspected {m.inspected})')

    most_active = sorted(monkeys, key=lambda m: m.inspected, reverse=True)[:2]
    # print(f'Two most active monkeys are: {most_active}')
    return math.prod([m.inspected for m in most_active])

def part1(monkeys: list[Monkey]):
    return play(monkeys, 20, True)

def part2(monkeys: list[Monkey]):
    return play(monkeys, 10000, False)


if __name__ == '__main__':
    for path in sys.argv[1:]:
        # print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"What is the level of monkey business after 10000 rounds? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
