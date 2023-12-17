import pathlib
import sys
from queue import PriorityQueue
import operator

import math

DELTAS = {"UP": (0, -1),
          "DOWN": (0, 1),
          "LEFT": (-1, 0),
          "RIGHT": (1, 0)}

DIRECTIONS = {(0, -1): "UP",
              (0, 1): "DOWN",
              (-1, 0): "LEFT",
              (1, 0): "RIGHT"}

TURNS = {
    ("LEFT", "LEFT"): (0, -1),
    ("LEFT", "RIGHT"): (0, 1),
    ("RIGHT", "LEFT"): (0, 1),
    ("RIGHT", "RIGHT"): (0, -1),
    ("UP", "LEFT"): (-1, 0),
    ("UP", "RIGHT"): (1, 0),
    ("DOWN", "LEFT"): (1, 0),
    ("DOWN", "RIGHT"): (-1, 0),
}


def parse(parsedata):
    grid = {}
    max_x = 0
    max_y = 0

    for y, line in enumerate(parsedata.splitlines()):
        for x, cell in enumerate(line):
            grid[x, y] = int(cell)

        max_x = max(x, max_x)
        max_y = max(y, max_y)

    return grid, max_x, max_y


def heat(grid, max_x, max_y, max_straight=math.inf, min_straight=0):
    q = PriorityQueue()
    q.put((0, (0, 0), "DOWN", -1))
    q.put((0, (0, 0), "RIGHT", -1))

    visited = set()
    destination = (max_x, max_y)
    while not q.empty():

        cost, curr_pos, direction, steps = q.get()

        if curr_pos == destination and steps >= min_straight:
            return cost
        if (curr_pos, direction, steps) in visited:
            continue

        visited.add((curr_pos, direction, steps))

        straight_pos = add_tuple(curr_pos, DELTAS[direction])
        if steps < max_straight - 1 and straight_pos in grid:
            straight_cost = cost + grid[straight_pos]
            q.put((straight_cost, straight_pos, direction, steps + 1))

        if steps >= min_straight - 1:

            left_delta = TURNS[(direction, "LEFT")]
            left_pos = add_tuple(curr_pos, left_delta)

            if left_pos in grid:
                left_cost = cost + grid[left_pos]
                q.put((left_cost, left_pos, DIRECTIONS[left_delta], 0))

            right_delta = TURNS[(direction, "RIGHT")]
            right_pos = add_tuple(curr_pos, right_delta)

            if right_pos in grid:
                right_cost = cost + grid[right_pos]
                q.put((right_cost, right_pos, DIRECTIONS[right_delta], 0))


def add_tuple(a, b):
    return tuple(map(operator.add, a, b))


def part1(data):
    grid, max_x, max_y = data
    return heat(grid, max_x, max_y, 3)


def part2(data):
    grid, max_x, max_y = data
    return heat(grid, max_x, max_y, 10, 4)


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
