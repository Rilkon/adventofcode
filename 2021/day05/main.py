import itertools
import re
from os.path import join, dirname


def write_lines_to_matrix(input: list, size: int, count_diagonal: bool) -> list:
    matrix = [[0 for x in range(size)] for y in range(size)]
    sign = lambda x: (x > 0) - (x < 0)
    for line in input:
        x1 = int(line.split(" -> ")[0].split(",")[0])
        y1 = int(line.split(" -> ")[0].split(",")[1])
        x2 = int(line.split(" -> ")[1].split(",")[0])
        y2 = int(line.split(" -> ")[1].split(",")[1])

        if x1 != x2 and y1 != y2 and count_diagonal is False:
            continue
        matrix[x1][y1] += 1

        while x1 != x2 or y1 != y2:
            x1 += sign(x2 - x1)
            y1 += sign(y2 - y1)
            matrix[x1][y1] += 1

    return matrix


def part1(input: list, size: int) -> str:
    return str(sum([sum(x > 1 for x in row) for row in write_lines_to_matrix(input, size, False)]))


def part2(input: list, size: int) -> str:
    return str(sum([sum(x > 1 for x in row) for row in write_lines_to_matrix(input, size, True)]))


if __name__ == '__main__':
    content = open(join(dirname(__file__), "day5input.txt"), 'r').read()
    lines = content.split("\n")
    size = max([x for x in itertools.chain(
        *[list(map(int, y)) for y in re.findall("(\\d+),(\\d+) -> (\\d+),(\\d+)", content)])]) + 1
    print("Part 1: " + part1(lines, size))
    print("Part 2: " + part2(lines, size))
