import pathlib
import sys
from copy import deepcopy
from collections import defaultdict

DIRECTIONS = ["^", ">", "v", "<"]

DELTA = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

START = (0, 0)


def turn_right(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]


def move_forward(position, direction):
    dx, dy = DELTA[direction]
    x, y = position
    return x + dx, y + dy


def parse(parsedata):
    grid = defaultdict(str)
    global START

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            grid[(x, y)] = value
            if value == "^":
                START = (x, y)

    return grid


def part1(grid):
    visited = set()
    curr_pos = START
    direction = grid[START]

    while True:
        visited.add(curr_pos)
        next_position = move_forward(curr_pos, direction)

        if grid[next_position] == "":
            break

        if grid[next_position] == "#":
            direction = turn_right(direction)

        curr_pos = move_forward(curr_pos, direction)

    return len(visited)

def simulate_guard(grid):
    visited = set()
    curr_pos = START
    direction = grid[START]

    while True:
        if (curr_pos, direction) in visited:
            return True

        visited.add((curr_pos, direction))
        next_position = move_forward(curr_pos, direction)

        if grid[next_position] == "":
            return False

        if grid[next_position] == "#":
            direction = turn_right(direction)
        else:
            curr_pos = next_position



def part2(grid):
    options = 0
    open_positions = [position for position, value in grid.items() if value == "."]

    for position in open_positions:
        grid[position] = "#"
        if simulate_guard(grid):
            options += 1
        grid[position] = "."

    return options

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
