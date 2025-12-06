import math
import pathlib
import sys
from collections import defaultdict
from copy import deepcopy
from itertools import zip_longest


def parse(parsedata):
    mathbook = defaultdict(list)
    for line in parsedata.splitlines():
        temp = [item for item in line.strip().split(" ") if item != ""]

        for i in range(len(temp)):
            mathbook[i].append(temp[i])

    return mathbook


def parse_part2(parsedata):

    operators = []
    problems = []
    curr = []
    for col in zip_longest(*parsedata.splitlines(), fillvalue=" "):
        if all(c == " " for c in col):
            problems.append(curr)
            continue
        elif col[-1] != " ":
            operators.append(col[-1])
            curr = []

        curr.append(int("".join(col[:-1])))
    problems.append(curr)

    return problems, operators


def do_cephalopods_math(problems):
    result = 0
    for problem in problems.values():
        if problem[len(problem) - 1] == "+":
            result += sum(map(int, problem[:-1]))
        elif problem[len(problem) - 1] == "*":
            result += math.prod(map(int, problem[:-1]))

    return result


def part1(data):
    return do_cephalopods_math(data)


def part2(data):
    return do_cephalopods_math(defaultdict(list, {i: v + [o] for i, (v, o) in enumerate(zip(data[0], data[1]))}))


def solve(puzzle_data):
    solution1 = part1(parse(deepcopy(puzzle_data)))
    solution2 = part2(parse_part2(puzzle_data))
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
