import pathlib
import sys
from collections import defaultdict


def parse(parsedata):
    rows = [line for line in parsedata.splitlines()]
    cols = ["".join(c)[::-1] for c in zip(*parsedata.splitlines())]

    return rows, cols


def solve_line(line):
    result = 0
    for x, el in enumerate(line):
        if el == "O":
            remaining = line[x + 1:]
            if remaining.count("#") > 0:
                hashlimit = remaining.index("#") + x + 1
            else:
                hashlimit = len(line)
            remaining_to_hash = remaining[:hashlimit - x - 1]
            result += hashlimit - remaining_to_hash.count("O")

    return result


def part1(data):
    result = 0
    for line in data[1]:
        result += solve_line(line)

    return result


def part2(data):
    return ""


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
