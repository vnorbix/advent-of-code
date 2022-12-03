import pathlib
import sys
from typing import List

import numpy as np
from colorama import Fore, Style


def parse_input(puzzle_input):
    bingo_data = puzzle_input.split('\n\n')
    drawn_numbers = [int(num) for num in bingo_data[0].split(",")]
    boards = np.array([
        [[int(value) for value in line.split()] for line in board_data.split('\n')] for board_data in bingo_data[1:]
    ])
    return drawn_numbers, boards


def calc_board_score(board):
    sum = 0
    for j in range(len(board)):
        line = board[j]
        for k in range(len(line)):
            board_number = line[k]
            if board_number != -1:
                sum += board_number
    return sum


def play_boards(number, boards: np.ndarray, play_until_last: bool = False, boards_won: List[int] = None):
    for i in range(len(boards)):
        if play_until_last and i in boards_won:
            continue
        board = boards[i]
        for j in range(len(board)):
            line = board[j]
            for k in range(len(line)):
                board_number = line[k]
                if board_number == number:
                    line[k] = -1
            if all([item == -1 for item in line]):
                if play_until_last:
                    if i not in boards_won:
                        print(f"board won: {i} ({number})")
                        boards_won.append(i)
                        if len(boards_won) == len(boards):
                            return calc_board_score(board) * number
                else:
                    return calc_board_score(board) * number
        for line in board.transpose():
            if all([item == -1 for item in line]):
                if play_until_last:
                    if i not in boards_won:
                        print(f"board won: {i} ({number})")
                        boards_won.append(i)
                        if len(boards_won) == len(boards):
                            return calc_board_score(board) * number
                else:
                    return calc_board_score(board) * number
    return None


def part1(data):
    drawn_numbers, boards = data
    for number in drawn_numbers:
        res = play_boards(number, boards)
        if res is not None:
            return res
    return None


def part2(data):
    drawn_numbers, boards = data
    boards_won = []
    for number in drawn_numbers:
        res = play_boards(number, boards, True, boards_won)
        if res is not None:
            return res
    return None


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"What will your final score be if you choose that board? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        print(
            f"Once it wins, what would its final score be? "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")
