import math
import pathlib
import sys
from copy import deepcopy
from collections import defaultdict


def parse(parsedata):
    grid = defaultdict(str)
    for x, line in enumerate(parsedata.splitlines()):
        for y, letter in enumerate(line):
            grid[(x, y)] = letter
    return grid

def part1(data):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    result = 0
    max_coord = int(math.sqrt(len(data)))
    for x in range(0, max_coord):
        for y in range(0, max_coord):
            for dx, dy in directions:
                if data[(x, y)] == "X" and \
                        data[(x + dx, y + dy)] == "M" and \
                        data[(x + 2 * dx, y + 2 * dy)] == "A" and \
                        data[(x + 3 * dx, y + 3 * dy)] == "S":
                    result += 1
    return result


def part2(data):
    result = 0
    max_coord = int(math.sqrt(len(data)))
    for x in range(0, max_coord):
        for y in range(0, max_coord):
            if data[(x, y)] == "M":
                if data[x + 1, y + 1] == "A" and data[(x + 2, y + 2)] == "S":
                    if data[(x + 2, y)] == "M" and data[(x, y + 2)] == "S" or \
                            data[(x + 2, y)] == "S" and data[(x, y + 2)] == "M":
                        result += 1
            if data[(x, y)] == "S":
                if data[x + 1, y + 1] == "A" and data[(x + 2, y + 2)] == "M":
                    if data[(x + 2, y)] == "M" and data[(x, y + 2)] == "S" or \
                            data[(x + 2, y)] == "S" and data[(x, y + 2)] == "M":
                        result += 1
    return result


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(deepcopy(data))
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
