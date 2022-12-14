from collections import deque, namedtuple
from dataclasses import dataclass
import heapq
import math
import pathlib
import string
import sys
import parse

from colorama import Fore, Style


def parse_input(puzzle_input):
    return [[c for c in map_line] for map_line in puzzle_input.split('\n')]


def find_start_end(map_data):
    for i, row in enumerate(map_data):
        for j, v in enumerate(row):
            if v == 'S':
                start = (i, j)
            if v == 'E':
                end = (i, j)
    return start, end


def find_possible_neighbors(map_data, node):
    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        dest_node = node[0] + i, node[1] + j
        if 0 <= dest_node[0] < len(map_data) and 0 <= dest_node[1] < len(map_data[0]) and \
                node_value(map_data, dest_node) <= node_value(map_data, node) + 1:
            yield dest_node


def node_value(map_data, node):
    char = map_data[node[0]][node[1]]
    if char == 'S':
        return 0
    if char == 'E':
        return 25
    return string.ascii_lowercase.find(char)

def print_map(map_data: list[list[int]], visit_matrix, neighbor):
    # print('-' * 10)
    # for i, row in enumerate(map_data):
    #     row_copy = row.copy()
    #     if neighbor[0] == i:
    #         row_copy[neighbor[1]] = '*'
    #     print(row_copy)
    # print('-' * 10)
    # print('-' * 10)
    # for i, row in enumerate(visit_matrix):
    #     print(row)
    # print('-' * 10)
    pass

def search_path(map_data, start, end):
    visit_matrix = [[False for _ in range(len(map_data[0]))]
                    for row in range(len(map_data))]
    
    visit_matrix[start[0]][start[1]] = True
    node_heap = []
    heapq.heappush(node_heap, (0, (start[0], start[1])))

    while True:
        if len(node_heap) == 0:
            # No solution
            return None
        node = heapq.heappop(node_heap)
        for neighbor in find_possible_neighbors(map_data, node[1]):
            if visit_matrix[neighbor[0]][neighbor[1]]:
                continue
            visit_matrix[neighbor[0]][neighbor[1]] = True
            print_map(map_data, visit_matrix, neighbor)
            if neighbor == end:
                return node[0] + 1
            else:
                heapq.heappush(node_heap, (node[0] + 1, neighbor))

def part1(map_data):
    start, end = find_start_end(map_data)
    return search_path(map_data, start, end)


def part2(map_data):
    _, end = find_start_end(map_data)
    start_coords = [(i, j) for j in range(len(map_data[0]))
                    for i in range(len(map_data)) if map_data[i][j] == 'a']
    return min(filter(lambda steps: steps is not None, (search_path(map_data, start, end) for start in start_coords)))


if __name__ == '__main__':
    for path in sys.argv[1:]:
        # print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"What is the fewest steps required to move from your current position to the location that should get the best signal? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
