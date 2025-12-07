import pathlib
import sys
from collections import defaultdict
from copy import deepcopy


def parse(parsedata):
    splitter = []
    start = (0, 0)

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            if value == "S":
                start = (x, y)
            elif value == "^":
                splitter.append((x, y))

    y_length = y
    return start, y_length, splitter


def part1and2(data):
    return tachyon_manifold(*data)


def tachyon_manifold(start, y_length, splitter):
    tachyonbeams = defaultdict(int)
    tachyonbeams[start] = 1
    splitcount = 0

    for _ in range(y_length):
        beams = defaultdict(int)
        for (x, y), beamcount in tachyonbeams.items():
            if (x, y + 1) in splitter:
                splitcount += 1
                beams[(x + 1, y + 1)] += beamcount
                beams[(x - 1, y + 1)] += beamcount
            else:
                beams[(x, y + 1)] += beamcount
        tachyonbeams = beams

    return splitcount, sum(tachyonbeams.values())



def solve(puzzle_data):
    data = parse(puzzle_data)
    solution = part1and2(deepcopy(data))
    return solution


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))