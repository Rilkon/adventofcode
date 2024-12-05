import pathlib
import sys
from copy import deepcopy
import regex as re


def parse(parsedata):
    return "".join(parsedata).replace("\n", "")


def part1(data):
    positivePattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(positivePattern, data)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])

    return result


def part2(data):
    data = re.sub(r"don't\(\).*?do\(\)", "", data)
    data = re.sub(r"don't\(\).*", "", data)
    return part1(data)


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
