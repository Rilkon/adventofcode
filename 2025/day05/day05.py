import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    r, i = parsedata.split("\n\n")
    ranges = []
    ids = []
    for line in r.splitlines():
        x, y = line.split("-")
        ranges.append(range(int(x), int(y) + 1))

    for line in i.splitlines():
        ids.append(int(line))

    return ranges, ids


def part1(data):
    return sum(any((x in r) for r in data[0]) for x in data[1])


def part2(data):
    intervals = sorted((r.start, r.stop) for r in data[0])
    count = 0

    current_start, current_end = intervals[0]
    for start, end in intervals:
        if start > current_end:
            count += current_end - current_start
            current_start = start
        current_end = max(current_end, end)
    count += (current_end - current_start)

    return count


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
