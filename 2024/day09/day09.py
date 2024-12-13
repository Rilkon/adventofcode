import pathlib
import sys
from copy import deepcopy
import re
from itertools import repeat


def parse(parsedata):
    filesystem = []
    n = 0
    for i, value in enumerate(parsedata):
        if i % 2 == 0:
            filesystem.extend(repeat(n, int(value)))
            n += 1
        else:
            filesystem.extend(repeat("X", int(value)))

    return filesystem


def part1(data):
    front = 0
    back = len(data) - 1

    while front < back:
        if data[front] == "X":
            while back > front and data[back] == "X":
                back -= 1

            if back > front:
                data[front], data[back] = data[back], "X"

        front += 1


    return sum(value * i for i, value in enumerate(data) if value != "X")



def part2(data):
    return ""



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
