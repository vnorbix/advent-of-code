import pathlib
import sys
from typing import Any

from colorama import Fore, Style


def find_dir(file_tree: dict[Any], current_dir_path: list[str]):
    ret_tree = file_tree
    for d in current_dir_path:
        ret_tree = ret_tree[d]
    return ret_tree


def parse_input(puzzle_input):
    current_dir_tree = file_tree = {}
    current_dir_path = []
    list_dir = False
    for line in puzzle_input.split('\n'):
        if line == '$ ls':
            list_dir = True
        elif line == ('$ cd ..'):
            current_dir_path.pop()
            current_dir_tree = find_dir(file_tree, current_dir_path)
            list_dir = False
        elif line.startswith('$ cd'):
            dir_name = line.split()[-1]
            current_dir_path.append(dir_name)
            current_dir_tree[dir_name] = {}
            current_dir_tree = current_dir_tree[dir_name]
            list_dir = False
        elif list_dir:
            tokens = line.split()
            if tokens[0] != 'dir':
                file_size, file_name = int(tokens[0]), tokens[1]
                current_dir_tree[file_name] = file_size
    return file_tree


def find_dirsizes(file_tree, dirsizes):
    dirsize = 0
    for key, value in file_tree.items():
        if type(value) is dict:
            ret = find_dirsizes(value, dirsizes)
            dirsize += ret
        else:
            dirsize += value
    dirsizes.append(dirsize)
    return dirsize


def part1(file_tree):
    dirsizes = []
    find_dirsizes(file_tree, dirsizes)
    return sum(filter(lambda ds: ds < 100000, dirsizes))


def part2(file_tree):
    dirsizes = []
    total_used = find_dirsizes(file_tree, dirsizes)
    TOTAL_DISK_SIZE = 70000000
    UPDATE_SPACE_REQUIRED = 30000000
    size_to_free = UPDATE_SPACE_REQUIRED - (TOTAL_DISK_SIZE - total_used)
    return sorted(filter(lambda ds: ds >= size_to_free, dirsizes))[0]


if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"Path: {path}")
        data = parse_input(pathlib.Path(path).read_text())
        print(
            f"What is the sum of the total sizes of those directories? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"What is the total size of that directory? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
