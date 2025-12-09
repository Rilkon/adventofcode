import itertools
import pathlib
import sys
from copy import deepcopy
from shapely.geometry import Polygon, box
from shapely.prepared import prep


def parse(parsedata):
    return [tuple(map(int, line.split(","))) for line in parsedata.splitlines()]


def part1(data):
    biggest = 0

    for pos1, pos2 in itertools.combinations(data, 2):
        area = (1 + max(abs(pos2[0] - pos1[0]), 1)) * (1 + max(abs(pos2[1] - pos1[1]), 1))
        biggest = max(area, biggest)

    return biggest


def part2(data):
    polygon = prep(Polygon(data))
    biggest = 0

    for pos1, pos2 in itertools.combinations(data, 2):
        area = (1 + max(abs(pos2[0] - pos1[0]), 1)) * (1 + max(abs(pos2[1] - pos1[1]), 1))
        if area <= biggest:
            continue

        rectangle = box(min(pos1[0], pos2[0]), min(pos1[1], pos2[1]),
                        max(pos1[0], pos2[0]), max(pos1[1], pos2[1]))

        if polygon.contains(rectangle):
            biggest = area

    return biggest


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
