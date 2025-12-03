import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    banks = []
    for line in parsedata.splitlines():
        banks.append(list(int(x) for x in line))
    return banks


def get_joltage(banks, size):
    joltage = 0
    for bank in banks:
        jolt = ""
        curr = bank
        while len(jolt) < size:
            curr_max = max(curr[:len(curr) + len(jolt) - (size - 1)])
            jolt = jolt + str(curr_max)
            curr = curr[curr.index(curr_max) + 1:]

        joltage = joltage + int(jolt)

    return joltage


def part1(data):
    return get_joltage(data, 2)


def part2(data):
    return get_joltage(data, 12)


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
