import math
import pathlib
import sys
import re


def parse(parsedata):
    times = [int(x) for x in re.findall(r"\d+", parsedata.splitlines()[0])]
    distances = [int(x) for x in re.findall(r"\d+", parsedata.splitlines()[1])]
    return times, distances


def get_num_of_solutions(times, distances):
    result = math.prod(sum(1 for j in range(times[i]) if j * (times[i] - j) > distances[i]) for i in range(len(times)))
    return result


def part1(data):
    return get_num_of_solutions(data[0], data[1])


def part2(data):
    times = int(''.join([str(x) for x in data[0]]))
    distances = int(''.join([str(x) for x in data[1]]))
    return get_num_of_solutions([times], [distances])


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
