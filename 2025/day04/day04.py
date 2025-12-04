import pathlib
import sys
from copy import deepcopy
import timeit

DIRS = [(0,1), (1,0), (1,1), (0,-1), (-1,0), (-1, -1), (1,-1), (-1,1)]

def parse(parsedata):

    grid = {}
    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            grid[(x,y)] = value

    return grid

def fewer_than_four_neighbors(pos, grid):
    return sum(grid.get((pos[0]+dx, pos[1]+dy)) == "@" for dx, dy in DIRS) < 4

def has_movable_roll(grid):
    return any(value=="@" and fewer_than_four_neighbors(key, grid) for key, value in grid.items())


def part1(data):
    return sum(value == "@" and fewer_than_four_neighbors(key, data) for key, value in data.items())

def part2(data):
    count = 0
    while has_movable_roll(data):
        for key, value in data.items():
            if value == "@" and fewer_than_four_neighbors(key, data):
                data[key] = "."
                count += 1
    return count

def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(deepcopy(data))
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        time1 = timeit.default_timer()
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
        print(timeit.default_timer() - time1)