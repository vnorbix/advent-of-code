import pathlib
import sys

import numpy as np
from colorama import Fore, Style


def parse_input(puzzle_input):
    return np.array([
        [int(bit) for bit in line] for line in puzzle_input.split('\n')
    ])


def parse_input_improved(puzzle_input):
    return [line for line in puzzle_input.strip().split('\n')]


def part1(data: np.ndarray):
    gamma_rate = 0
    epsilon_rate = 0
    for row in data.transpose():
        count_1s = 0
        for bit in row:
            if bit == 1:
                count_1s += 1
        gamma_rate = gamma_rate << 1
        epsilon_rate = epsilon_rate << 1
        if count_1s > len(row) - count_1s:
            gamma_rate |= 1
        else:
            epsilon_rate |= 1
    return gamma_rate * epsilon_rate


def common(strs, i) -> str:  # '1' or '0'
    """The bit that is most common in position i among strs."""
    bits = [s[i] for s in strs]
    return '1' if bits.count('1') >= bits.count('0') else '0'


def uncommon(strs, i) -> str:  # '1' or '0'
    """The bit that is least common in position i among strs."""
    return '1' if common(strs, i) == '0' else '0'


def epsilon(strs) -> str:
    """The bit string formed from most common bit at each position."""
    return ''.join(common(strs, i) for i in range(len(strs[0])))


def gamma(strs) -> str:
    """The bit string formed from most uncommon bit at each position."""
    return ''.join(uncommon(strs, i) for i in range(len(strs[0])))


def part1_improved(data):
    return int(epsilon(data), 2) * int(gamma(data), 2)


def search_num(data, commonity_func, i=0):
    bit_at_position = commonity_func(data, i)
    numbers = [num for num in data if num[i] == bit_at_position]
    if len(numbers) == 1:
        return numbers[0]
    return search_num(numbers, commonity_func, i + 1)


def part2_improved(data):
    return int(search_num(data, common), 2) * int(search_num(data, uncommon), 2)


def find_number(data, index, most_common: bool):
    filtered_numbers = []
    count_1s = 0
    for bit in data.transpose()[index]:
        if bit == 1:
            count_1s += 1
    if count_1s == len(data.transpose()[index]) / 2:
        significant = 1 if most_common else 0
    elif count_1s > len(data.transpose()[index]) - count_1s:
        significant = 1 if most_common else 0
    else:
        significant = 0 if most_common else 1

    for number in data:
        if number[index] == significant:
            filtered_numbers.append(number)
    if len(filtered_numbers) == 1:
        return int("".join([str(n) for n in filtered_numbers[0]]), 2)
    else:
        return find_number(np.array(filtered_numbers), index + 1, most_common)


def part2(data: np.ndarray):
    oxygen_generator_rating = find_number(data, 0, True)
    co2_scrubber_rating = find_number(data, 0, False)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        puzzle_input = pathlib.Path(path).read_text().strip()
        print(
            f"What is the power consumption of the submarine? "
            f"{Fore.RED}{part1(parse_input(puzzle_input))}{Style.RESET_ALL}")
        print(
            f"What is the life support rating of the submarine "
            f"{Fore.RED}{part2(parse_input(puzzle_input))}{Style.RESET_ALL}")
