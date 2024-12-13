import pathlib
import sys
from copy import deepcopy
from queue import Queue

DIRECTIONS = {(-1, 0), (1, 0), (0, -1),(0, 1)}

max_x = 0
max_y = 0


def parse(parsedata):
    global max_x, max_y
    grid = {}
    starts = []

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            grid[(x, y)] = int(value)
            if value == "0":
                starts.append((x, y))

    max_x = x
    max_y = y

    return grid, starts


def score_trailhead(grid, start):
    global max_x, max_y
    visited_peaks = []
    q = Queue()
    q.put(start)

    while not q.empty():
        pos = q.get()

        if grid[pos] == 9:
            visited_peaks.append(pos)

        x, y = pos
        for dx, dy in DIRECTIONS:
            if 0 <= dx + x <= max_x and 0 <= dy + y <= max_y:
                if grid[(x + dx, y + dy)] == grid[(x, y)] + 1:
                    q.put((x + dx, y + dy))

    return len(set(visited_peaks)), len(visited_peaks)


def part1(data):
    grid, starts = data
    return sum(score_trailhead(grid, start)[0] for start in starts)


def part2(data):
    grid, starts = data
    return sum(score_trailhead(grid, start)[1] for start in starts)


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
