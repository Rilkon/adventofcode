# removed imports and f-strings to run in pypy (probably 3 times quicker runtime)
import collections
import sys
from copy import deepcopy

max_x = 70
max_y = 70
max_bytes = 1024

DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}


def parse(parsedata):
    grid = []
    for i, line in enumerate(parsedata.splitlines()):
        x, y = list(map(int, (line.split(","))))
        grid.append((x, y))

    return grid


def is_valid(grid, seen, pos):
    global max_x, max_y
    x, y = pos
    return (
            pos not in grid and
            0 <= x <= max_x and
            0 <= y <= max_y and
            pos not in seen
    )


def bfs(grid, start, goal):
    queue = collections.deque()
    queue.append([start])
    seen = {start}

    while queue:
        path_taken = queue.popleft()
        current_pos = path_taken[-1]

        if current_pos == goal:
            return path_taken

        for (dx, dy) in DIRECTIONS:
            x, y = current_pos
            next_pos = (x + dx, y + dy)

            if is_valid(grid, seen, next_pos):
                new_path = path_taken + [next_pos]
                queue.append(new_path)
                seen.add(next_pos)

    return None


def part1(data):
    start = (0, 0)
    goal = (max_x, max_y)
    return len(bfs(data[:max_bytes], start, goal)) - 1


def part2(data):
    start = (0, 0)
    goal = (max_x, max_y)
    new_data = []
    result = []

    for i, value in enumerate(data):

        new_data.append(value)
        # Only calculate the next iteration if the new element is on the previous best path
        if i == 0 or value in result:
            result = bfs(new_data, start, goal)

        if result is None:
            break

    return str(new_data[i]).replace("(", "").replace(")", "").replace(" ", "")


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(deepcopy(data))
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, 'r') as f:
            puzzle_input = f.read().strip()
        solutions = solve(puzzle_input)
        for solution in solutions:
            print(solution)
