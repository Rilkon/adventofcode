import pathlib
import sys
from collections import defaultdict
from copy import deepcopy
from itertools import combinations

max_value = 0

def parse(parsedata):
    grid = defaultdict(str)
    antennas = {}
    global max_value

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            grid[(x, y)] = value

    max_value = x

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            if value != ".":
                if value in antennas:
                    antennas[value] += [(x,y)]
                else:
                    antennas[value] = [(x,y)]

    return [grid, antennas]


def get_antinodes(point1, point2):

    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]

    new_point1 = point1[0] - dx, point1[1] - dy
    new_point2 = point2[0] + dx, point2[1] + dy

    return new_point1, new_point2



def get_harmonic_antinodes(point1, point2):
    global max_value

    x1, y1 = point1
    x2, y2 = point2

    points = []

    dx = x2 - x1
    dy = y2 - y1

    while 0 <= x1 <= max_value and 0 <= y1 <= max_value:
        points.append((x1, y1))
        x1 -= dx
        y1 -= dy

    while 0 <= x2 <= max_value and 0 <= y2 <= max_value:
        points.append((x2, y2))
        x2 += dx
        y2 += dy

    return points

def both_parts(data, p2 = False):
    grid, antennas = data
    antinodes = set()
    for key, values in antennas.items():

        for prod in combinations(values, 2):

            if p2:
                new_points = get_harmonic_antinodes(prod[0], prod[1])
            else:
                new_points = get_antinodes(prod[0], prod[1])

            for point in new_points:
                if point in grid:
                    antinodes.add(point)

    return antinodes

def part1(data):
    return len(both_parts(data))


def part2(data):
    return len(both_parts(data, True))


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
