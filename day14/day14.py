import pathlib
import sys


def parse(parsedata):
    grid = [line for line in parsedata.splitlines()]
    return grid


def rotate_cw(grid):
    return ["".join(row) for row in zip(*grid[::-1])]


def rotate_ccw(grid):
    return ["".join(row) for row in zip(*grid)][::-1]


def tilt_platform(grid):
    for x, row in enumerate(grid):
        for _ in range(len(row) - 1):
            grid[x] = "".join(grid[x]).replace("O.", ".O")
    return grid


def spin_cycle(grid):
    for _ in range(4):
        grid = tilt_platform(rotate_cw(grid))
    return grid


def get_load(grid):
    return sum([len(grid) - y for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "O"])


def part1(data):
    grid = rotate_ccw(tilt_platform(rotate_cw(data)))
    return get_load(grid)


def part2(data):
    grid = data
    known = {}
    steps = 0
    found = False
    limit = 1_000_000_000

    while steps < limit:
        steps += 1
        grid = spin_cycle(grid)

        _key = str(grid)
        if _key in known and not found:
            cycle = steps - known[_key]
            steps += ((limit - steps) // cycle) * cycle
            found = True

        known[_key] = steps

    return get_load(grid)


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
