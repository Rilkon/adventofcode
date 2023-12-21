import pathlib
import sys
from collections import deque

STEPGOAL = 64

DELTAS = {"U": (0, -1),
          "D": (0, 1),
          "L": (-1, 0),
          "R": (1, 0)}


def parse(parsedata):
    max_x = 0
    max_y = 0
    start = (0, 0)
    grid = {}

    for y, line in enumerate(parsedata.splitlines()):
        for x, cell in enumerate(line):
            grid[(x, y)] = cell
            if cell == "S":
                start = (x, y)

            max_x = max(x, max_x)
        max_y = max(y, max_y)

    return grid, start, max_x, max_y,


def part1(data):
    # grid, start, max_x, max_y = data
    #
    # q = deque()
    # q.append((start, 0))
    #
    # visited = set()
    # goals = set()
    #
    # while q:
    #     curr, steps = q.popleft()
    #
    #     if steps == STEPGOAL:
    #         goals.add(curr)
    #         continue
    #
    #     if (curr, steps) in visited:
    #         continue
    #
    #     visited.add((curr, steps))
    #
    #     for delta in DELTAS.values():
    #         dy, dx = delta
    #         x, y = curr
    #         newpos = (x+dx, y+dy)
    #         if newpos in grid.keys() and grid[newpos] != "#":
    #             q.append((newpos, steps + 1))
    return ""
    return len(goals)





def part2(data):
    grid, start, max_x, max_y = data



    for value in [6, 10, 50, 100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 6000, 7000, 8000]:
        q = deque()
        q.append((start, 0))

        visited = set()

        allgoals = {}
        goals = set()
        PART2GOAL = value

        while q:
            curr, steps = q.popleft()

            if steps == PART2GOAL:
                goals.add(curr)
                continue

            if (curr, steps) in visited:
                continue

            visited.add((curr, steps))

            for delta in DELTAS.values():
                dy, dx = delta
                x, y = curr
                newpos = (x+dx, y+dy)
                if newpos in grid.keys():
                    if grid[newpos] != "#":
                        q.append((newpos, steps + 1))
                else:
                    x, y = newpos

                    if x > max_x:
                        x = x % (max_x+1)
                    if y > max_y :
                        y = y % (max_y+1)
                    if x < 0:
                        x = (x % (max_x+1) + max_x+1) % (max_x+1)
                    if y < 0:
                        y = (y % (max_y+1) + max_y+1) % (max_y+1)

                    if grid[(x,y)] != "#":
                        q.append((newpos, steps + 1))



        allgoals[PART2GOAL] = len(goals)
        print(allgoals)

    return ""
    return allgoals


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
