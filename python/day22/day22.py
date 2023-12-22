import pathlib
import sys
from collections import defaultdict


class Brick:

    def __init__(self, beginning, end, brick_id):
        self.x1, self.y1, self.z1 = beginning
        self.x2, self.y2, self.z2 = end
        self.brick_id = brick_id

    def get_xy(self):
        return [(x, y) for x in range(self.x1, self.x2 + 1) for y in range(self.y1, self.y2 + 1)]

    def get_z(self):
        return self.z2 - self.z1 + 1


def parse(parsedata):
    bricks = defaultdict(list)

    for i, line in enumerate(parsedata.splitlines()):
        beginning, end = line.split("~")
        x1, y1, z1 = map(int, beginning.split(","))
        x2, y2, z2 = map(int, end.split(","))

        bricks[z1].append(Brick((x1, y1, z1), (x2, y2, z2), i))

    return bricks


def part1(data):
    bricks = data
    return ""


def part2(data):
    return ""


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
