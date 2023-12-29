import pathlib
import sys
from queue import Queue

grid = {}
max_x = 0
max_y = 0

directions = {"LEFT": (-1, 0),
              "RIGHT": (1, 0),
              "UP": (0, -1),
              "DOWN": (0, 1)}

turns = {
    ("|", "RIGHT"): ["UP", "DOWN"],
    ("|", "LEFT"): ["UP", "DOWN"],
    ("-", "UP"): ["LEFT", "RIGHT"],
    ("-", "DOWN"): ["LEFT", "RIGHT"],
    ("/", "DOWN"): ["LEFT"],
    ("/", "UP"): ["RIGHT"],
    ("/", "LEFT"): ["DOWN"],
    ("/", "RIGHT"): ["UP"],
    ("\\", "DOWN"): ["RIGHT"],
    ("\\", "UP"): ["LEFT"],
    ("\\", "LEFT"): ["UP"],
    ("\\", "RIGHT"): ["DOWN"]}


def parse(parsedata):
    global grid
    global max_x
    global max_y

    for y, line in enumerate(parsedata.splitlines()):
        for x, cell in enumerate(line):
            grid[x, y] = cell

        max_x = max(x, max_x)
        max_y = max(y, max_y)

    return grid


def pewpew(start):
    q = Queue()
    q.put(start)

    visited = {}
    while not q.empty():

        curr = q.get()

        pos = next(iter(curr))
        x, y = pos
        direction = next(iter(curr.values()))

        if pos in visited and visited[pos] == direction:
            continue

        visited[pos] = direction

        tile = grid[pos]
        if (tile, direction) in turns:
            for turn in turns[(tile, direction)]:
                new_dir = turn
                dx, dy = directions[new_dir]
                new_pos = (x + dx, y + dy)

                if 0 <= new_pos[0] <= max_x and 0 <= new_pos[1] <= max_y:
                    q.put({new_pos: new_dir})

        else:
            dx, dy = directions[direction]
            new_pos = (x + dx, y + dy)
            if 0 <= new_pos[0] <= max_x and 0 <= new_pos[1] <= max_y:
                q.put({new_pos: direction})

    return len(visited)


def part1(data):
    return pewpew({(0, 0): "RIGHT"})


def part2(data):
    starts = [[{(x, 0): "DOWN"} for x in range(max_x)],
              [{(x, max_y): "UP"} for x in range(max_x)],
              [{(0, y): "RIGHT"} for y in range(max_y)],
              [{(max_x, y): "LEFT"} for y in range(max_y)]]

    return max([pewpew(value) for start in starts for value in start])


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
