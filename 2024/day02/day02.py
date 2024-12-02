import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    reports = []
    for line in parsedata.splitlines():
        reports.append([int(x) for x in line.split(" ")])

    return reports


def is_ok(report):
    if ((all(b > a for a, b in zip(report, report[1:])) or
         all(b < a for a, b in zip(report, report[1:]))) and
            all(1 <= abs(b - a) <= 3 for a, b in zip(report, report[1:]))):
        return True
    return False


def part1(data):
    return sum([1 if is_ok(report) else 0 for report in data])


def part2(data):
    return sum([1 if any(is_ok(report[:i] + report[i + 1:]) for i, _ in enumerate(report)) else 0 for report in data])


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
