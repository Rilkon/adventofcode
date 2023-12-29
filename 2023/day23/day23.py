import pathlib
import sys

sys.setrecursionlimit(10_000_000)

DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

SLOPEDELTAS = {"^": (0, -1),
               "v": (0, 1),
               "<": (-1, 0),
               ">": (1, 0)}


def parse(parsedata, p2=False):
    grid = {}
    max_x = 0
    max_y = 0

    for y, line in enumerate(parsedata.splitlines()):
        for x, trail in enumerate(line):
            grid[x, y] = trail

            max_y = max(max_x, x)
            max_x = max(max_y, y)

            if p2 and trail in SLOPEDELTAS.keys():
                grid[x, y] = "."

    return grid, max_x, max_y


def dfs(g, curr, end, visited=None):
    if visited is None:
        visited = set()

    if curr == end:
        return len(visited) - 1

    visited.add(curr)

    x, y = curr

    best = None
    for delta in DELTAS:

        dx, dy = delta
        newpos = (x + dx, y + dy)
        if newpos not in g.keys() or g[newpos] == "#":
            continue
        if g[newpos] != "." and (g[newpos] in SLOPEDELTAS.keys() and SLOPEDELTAS[g[newpos]]) != delta:
            continue
        if newpos in visited:
            continue

        visited.add(newpos)
        result = dfs(g, newpos, end, visited)
        best = max(best, result) if best and result else result
        visited.remove(newpos)

    return best


def part1and2(data):
    grid, max_x, max_y = data

    start = (1, 0)
    end = (max_x - 1, max_y)

    return dfs(grid, (1, 0), end)


def solve(puzzle_data):
    solution1 = part1and2(parse(puzzle_data))
    solution2 = part1and2(parse(puzzle_data, True))
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
