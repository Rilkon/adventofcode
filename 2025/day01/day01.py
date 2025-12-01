import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    instructions = []
    for line in parsedata.splitlines():
        instructions.append([1 if line[0] == "R" else -1, int(line[1:])])

    return instructions


def part1(data):
    position = 50
    count = 0

    for instr in data:
        position = (position + (instr[0] * instr[1])) % 100
        if position == 0:
            count += 1

    return count


def part2(data):
    position = 50
    count = 0

    for instr in data:
        for _ in range(instr[1]):
            position = (position + instr[0]) % 100
            if position == 0:
                count += 1

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
