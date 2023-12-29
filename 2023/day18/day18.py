import operator
import pathlib
import sys
from collections import defaultdict
from shapely import Polygon

DELTAS = {"U": (0, -1),
          "D": (0, 1),
          "L": (-1, 0),
          "R": (1, 0),
          "3": (0, -1),
          "1": (0, 1),
          "2": (-1, 0),
          "0": (1, 0)}


def parse(parsedata):
    result = []
    for line in parsedata.splitlines():
        direction, meters, rgb = line.split(" ")
        rgb = rgb[2:-1]
        result.append((direction, int(meters), rgb))

    return result


def dig_path(instructions, p2=False):
    digpath = defaultdict(str)
    curr = (0, 0)

    for direction, meters, rgb in instructions:
        if p2:
            meters = int(rgb[:5], 16)
            delta = DELTAS[rgb[-1]]
        else:
            delta = DELTAS[direction]

        curr = add_tuple(curr, fast_forward(delta, meters))
        digpath[curr] = "#"

    pgon = Polygon(digpath.keys()).buffer(0.5, join_style=2)
    return int(pgon.area)


def part1(data):
    return dig_path(data)


def part2(data):
    return dig_path(data, True)


def add_tuple(a, b):
    return tuple(map(operator.add, a, b))


def fast_forward(coords, factor):
    x, y = coords
    return x * factor, y * factor


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
