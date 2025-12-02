import pathlib
import sys
from copy import deepcopy
import re


def parse(parsedata):

    product_id_ranges = []

    for line in parsedata.split(","):
        product_id_ranges.append(list(map(int, line.split("-"))))

    return product_id_ranges

def part1(data):

    result = 0
    for line in data:
        for i in range(line[0], line[1]+1):
            l = len(str(i))
            if l % 2 != 0 or l < 2:
                continue

            if str(i)[:l//2] == str(i)[l//2:]:
                result = result + i

    return result


def part2(data):
    rep = re.compile(r"(.+?)\1+")
    result = 0
    for line in data:
        for i in range(line[0], line[1] + 1):
            match = rep.fullmatch((str(i)))
            sub = match.group(1) if match else None
            if sub:
                result = result + i

    return result



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