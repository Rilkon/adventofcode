import pathlib
import sys
from copy import deepcopy
from collections import defaultdict


def parse(parsedata):
    stones = defaultdict(int)
    for value in (map(int, parsedata.split(" "))):
        stones[value] += 1
    print(stones)
    return stones


def blink(stones, n):
    for i in range(n):

        temp = defaultdict(int)
        for key, value in stones.items():

            str_key = str(key)
            length = len(str_key)
            if key == 0:
                temp[1] += value
            elif len(str_key) % 2 == 0:
                temp[int(str_key[:length // 2])] += value
                temp[int(str_key[length // 2:])] += value
            else:
                temp[key * 2024] += value

        stones = temp
    return stones


def part1(data):
    stones = blink(data, 25)
    return sum(value for key, value in stones.items())


def part2(data):
    stones = blink(data, 75)
    return sum(value for key, value in stones.items())


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
