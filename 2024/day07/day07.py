import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    return [[int(left), list(map(int, right.split(" ")))] for line in parsedata.splitlines() for left, right in [line.split(": ")]]


def elephant_math(result, nums, part2=False):
    possible_results = {nums[0]}

    for curr in nums[1:]:
        temp = set()
        for res in possible_results:
            temp.add(res + curr)
            temp.add(res * curr)
            if part2:
                temp.add(int(str(res) + str(curr)))
        possible_results = temp

    if result in possible_results:
        return True
    return False


def part1(data):
    return sum(left for left, right in data if elephant_math(left, right))


def part2(data):
    return sum(left for left, right in data if elephant_math(left, right, True))


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
