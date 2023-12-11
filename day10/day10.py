import pathlib
import sys
from collections import defaultdict
from queue import Queue
from matplotlib import path as matplotpath

# | = UP DOWN
# - = LEFT RIGHT
# L = UP RIGHT
# J = UP LEFT
# 7 = DOWN LEFT
# F = DOWN RIGHT
PIPES = {"|": [(0, -1), (0, 1)],
         "-": [(-1, 0), (1, 0)],
         "L": [(0, -1), (1, 0)],
         "J": [(0, -1), (-1, 0)],
         "7": [(-1, 0), (0, 1)],
         "F": [(1, 0), (0, 1)]}

DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def parse(parsedata):
    grid = defaultdict(str)
    for y, line in enumerate(parsedata.splitlines()):
        for x, tile in enumerate(line):
            grid[(x, y)] = tile

            if tile == "S":
                start = (x, y)

    return grid, start, x, y


def part1and2(data):
    grid, start, max_x, max_y = data
    q = Queue()

    # find starting directions
    for dx, dy in DELTAS:
        tile = grid[(start[0] + dx, start[1] + dy)]

        if not tile in PIPES.keys():
            continue
        for dir_x, dir_y in PIPES[tile]:
            # only connecting ones
            if dir_x - dx == 0 and dir_y - dy == 0:
                q.put((start[0] + dx, start[1] + dy))

    visited = {start: None}
    while not q.empty():
        # get next and ignore already visited
        if (current := q.get()) in visited:
            continue

        # add elements connecting to current element to queue
        for dx, dy in PIPES[grid[current]]:
            q.put((current[0] + dx, current[1] + dy))

        visited[current] = None

    # p2
    points = list(set(visited).symmetric_difference(set(grid.keys())))
    inside = matplotpath.Path(list(visited)).contains_points(points)

    # Part 1: Half the roundtrip should be the farthest stepdistance
    # Part 2: Sum over list of booleans if each point is inside the path
    return len(visited) // 2, sum(inside)


def solve(puzzle_data):
    data = parse(puzzle_data)
    return part1and2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
