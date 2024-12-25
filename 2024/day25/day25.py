import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    keys = []
    locks = []
    for line in map(str.split, parsedata.split("\n\n")):
        if line[0][0] == "#":
            locks.append([column.count("#") - 1 for column in list(zip(*line))])
        else:
            keys.append([column.count("#") - 1 for column in list(zip(*line))])
    return keys, locks


def part1(data):
    keys, locks = data
    return sum(all(k + l < 6 for l, k in zip(key, lock)) for lock in locks for key in keys)


def part2(data):
    return "🎄Merry Christmas 🎄"


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
