import pathlib
import sys
from collections import defaultdict
import numpy as np


def parse(parsedata):

    grid = defaultdict(str)

    count = 1
    x, y = 0
    for line in parsedata.splitlines():
        for tile in line:
            if tile == "#":
                grid[x, y]  = count
                count +=1
            else:
                grid[x, y] = tile

            x+=1

        y += 1

    print(grid)



    return grid


def part1(data):
    return ""


def part2(data):
    return ""


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
