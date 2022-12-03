import pathlib
import sys
from enum import Enum
from dataclasses import dataclass
from typing import Optional

from colorama import Fore, Style


class GameAction(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class Outcome(Enum):
    LOOSE = 0
    DRAW = 1
    WIN = 2


win_outcomes = [
    (GameAction.ROCK, GameAction.PAPER),
    (GameAction.SCISSORS, GameAction.ROCK),
    (GameAction.PAPER, GameAction.SCISSORS)
]


def find_my_action(opponent_action: GameAction, outcome: Outcome):
    loose_outcomes = {
        GameAction.PAPER: GameAction.ROCK,
        GameAction.ROCK: GameAction.SCISSORS,
        GameAction.SCISSORS: GameAction.PAPER
    }
    if outcome == Outcome.WIN:
        return list(filter(lambda actions: actions[0] == opponent_action, win_outcomes))[0][1]
    if outcome == Outcome.DRAW:
        return opponent_action
    if outcome == Outcome.LOOSE:
        return loose_outcomes[opponent_action]


@dataclass
class Round:
    opponent_action: GameAction
    my_action: Optional[GameAction]

    def get_outcome_points(self):
        if self.opponent_action == self.my_action:
            return 3
        if (self.opponent_action, self.my_action) in win_outcomes:
            return 6
        return 0

    def get_shape_points(self):
        return {GameAction.ROCK: 1, GameAction.PAPER: 2, GameAction.SCISSORS: 3}[self.my_action]


def convert_line_part1(line):
    opponent_actions = {'A': GameAction.ROCK, 'B': GameAction.PAPER, 'C': GameAction.SCISSORS}
    my_actions = {'X': GameAction.ROCK, 'Y': GameAction.PAPER, 'Z': GameAction.SCISSORS}
    opponent_action, my_action = line.split()
    return Round(opponent_actions[opponent_action], my_actions[my_action])


def convert_line_part2(line):
    opponent_actions = {'A': GameAction.ROCK, 'B': GameAction.PAPER, 'C': GameAction.SCISSORS}
    outcomes = {'X': Outcome.LOOSE, 'Y': Outcome.DRAW, 'Z': Outcome.WIN}
    opponent_action, outcome = line.split()
    return Round(
        opponent_actions[opponent_action],
        find_my_action(opponent_actions[opponent_action], outcomes[outcome])
    )


def parse_input_part1(puzzle_input):
    return list(map(convert_line_part1, puzzle_input.split('\n')))


def parse_input_part2(puzzle_input):
    return list(map(convert_line_part2, puzzle_input.split('\n')))


def part1(rounds):
    return sum(round.get_shape_points() + round.get_outcome_points() for round in rounds)


def part2(rounds):
    return sum(round.get_shape_points() + round.get_outcome_points() for round in rounds)


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"What would your total score be if everything goes exactly according to your strategy guide? "
            f"{Fore.RED}{part1(parse_input_part1(puzzle_input))}{Style.RESET_ALL}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"Following the Elf's instructions for the second column, what would your total score be if everything goes "
            f"exactly according to your strategy guide? "
            f"{Fore.RED}{part2(parse_input_part2(puzzle_input))}{Style.RESET_ALL}")
