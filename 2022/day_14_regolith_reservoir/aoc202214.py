from collections import namedtuple
import itertools
import pathlib
import sys

from colorama import Fore, Style

PUZZLE_DIR = pathlib.Path(__file__).parent

Coordinate = namedtuple('Coordinate', ['x', 'y'])

Bounds = namedtuple('Coordinate', ['x1', 'y1', 'x2', 'y2'])

Size = namedtuple('Size', ['w', 'h'])

SAND_SOURCE = Coordinate(500, 0)


def parse_input(puzzle_input):
    def create_shapes(shape_data):
        for coord in shape_data.split('->'):
            x, y = tuple(map(int, coord.split(',')))
            yield Coordinate(x, y)
    return [list(create_shapes(shape)) for shape in puzzle_input.split('\n')]

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

class Scan:
    def __init__(self, shapes) -> None:
        self.position = Coordinate(SAND_SOURCE.x, SAND_SOURCE.y + 1)
        self.settled_sand = 0
        self.create_scan(shapes)

    def find_bounds(self, shapes: list[list[Coordinate]]):
        min_x = min([coords.x for shape in shapes for coords in shape] + [SAND_SOURCE.x])
        min_y = min([coords.y for shape in shapes for coords in shape] + [SAND_SOURCE.y])
        max_x = max([coords.x for shape in shapes for coords in shape] + [SAND_SOURCE.x])
        max_y = max([coords.y for shape in shapes for coords in shape] + [SAND_SOURCE.y])
        return Bounds(min_x, min_y, max_x + 1, max_y + 1)

    def find_size(self):
        return Size(self.bounds.x2 - self.bounds.x1, self.bounds.y2 - self.bounds.y1)

    def set_scan_position(self, coordinate: Coordinate, value):
        self.scan[coordinate.y - self.bounds.y2][coordinate.x - self.bounds.x1] = value
    
    def get_scan_position(self, coordinate):
        return self.scan[coordinate.y - self.bounds.y2][coordinate.x - self.bounds.x1]

    def create_scan(self, shapes):
        self.bounds = self.find_bounds(shapes)
        self.size = self.find_size()
        self.scan = [['.' for _ in range(self.size.w)] for _ in range(self.size.h)]
        self.set_scan_position(SAND_SOURCE, '+')
        self.set_scan_position(self.position, 'o')
        for shape in shapes:
            for coord_pair in pairwise(shape):
                if coord_pair[0].x == coord_pair[1].x:
                    min_y = min(coord_pair[0].y, coord_pair[1].y)
                    max_y = max(coord_pair[0].y, coord_pair[1].y)
                    for y in range(min_y, max_y + 1):
                        self.set_scan_position(Coordinate(coord_pair[0].x, y), '#')
                else:
                    min_x = min(coord_pair[0].x, coord_pair[1].x)
                    max_x = max(coord_pair[0].x, coord_pair[1].x)
                    for x in range(min_x, max_x + 1):
                        self.set_scan_position(Coordinate(x, coord_pair[0].y), '#')


    def print(self):
        for line in self.scan:
            print(''.join(line))

    def can_move_down(self):
        if self.position == self.size.h - 1:
            return False
        if self.get_scan_position(Coordinate((self.position.x), (self.position.y + 1))) != '.':
            return False
        return True

    def can_move_left_diagonal(self):
        if self.position.x == self.bounds.x1:
            return False
        if self.position.y == self.bounds.y2 - 1:
            return False
        if self.get_scan_position(Coordinate((self.position.x - 1), (self.position.y + 1))) != '.':
            return False
        return True
    
    def can_move_right_diagonal(self):
        if self.position.x == self.bounds.x2 - 1:
            return False
        if self.position.y == self.bounds.y2 - 1:
            return False
        if self.get_scan_position(Coordinate((self.position.x + 1), (self.position.y + 1))) != '.':
            return False
        return True

    def will_overlow(self):
        return self.position.x == self.bounds.x1 or self.position.x == self.bounds.x2 - 1


    def advance(self):
        if self.can_move_down():
            self.set_scan_position(self.position, '.')
            self.position = Coordinate(self.position.x, self.position.y + 1)
            self.set_scan_position(self.position, 'o')
            return True
        if self.can_move_left_diagonal():
            self.set_scan_position(self.position, '.')
            self.position = Coordinate(self.position.x - 1, self.position.y + 1)
            self.set_scan_position(self.position, 'o')
            return True
        if self.can_move_right_diagonal():
            self.set_scan_position(self.position, '.')
            self.position = Coordinate(self.position.x + 1, self.position.y + 1)
            self.set_scan_position(self.position, 'o')
            return True
        if self.will_overlow():
            return False
        self.position = Coordinate(SAND_SOURCE.x, SAND_SOURCE.y)
        self.settled_sand += 1
        if self.get_scan_position(self.position) == 'o':
            return False
        self.set_scan_position(self.position, 'o')
        return True


def part1(shapes):
    scan = Scan(shapes)
    while scan.advance():
        pass
    return scan.settled_sand


def part2(shapes):
    scan = Scan(shapes)
    height = scan.size.h
    scan = Scan(shapes + [[Coordinate(500 - round(height * 1.1), scan.bounds.y2 + 1), Coordinate(500 + round(height * 1.1), scan.bounds.y2 + 1)]])
    scan.print()
    while scan.advance():
        pass
    return scan.settled_sand


if __name__ == '__main__':
    for path in sys.argv[1:]:
        # print(f"Path: {path}")
        data = parse_input((PUZZLE_DIR / pathlib.Path(path)).read_text())
        print(
            f"How many units of sand come to rest before sand starts flowing into the abyss below? "
            f"{Fore.RED}{part1(data)}{Style.RESET_ALL}")
        print(
            f"How many units of sand come to rest? "
            f"{Fore.RED}{part2(data)}{Style.RESET_ALL}")
        