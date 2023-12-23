from os.path import dirname, join
from operator import mul
from functools import reduce


class Day9:
    neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def __init__(self, filename):
        content = open(join(dirname(__file__), filename), "r").read()
        lines = content.split("\n")

        self.heights = [list(map(int, line)) for line in lines]
        self.rowlen = len(lines)
        self.collen = len(lines[0])

    def is_out(self, x: int, y: int) -> bool:
        return not (0 <= x < self.rowlen and 0 <= y < self.collen)

    def is_local_min(self, x: int, y: int):
        return all((self.is_out(x + dx, y + dy) or self.heights[x][y] < self.heights[x + dx][y + dy])
                   for dx, dy in self.neighbours)

    def get_lows(self) -> list:
        lows = []
        for x in range(self.rowlen):
            for y in range(self.collen):
                if self.is_local_min(x, y):
                    lows.append((x, y))
        return lows

    def part1(self) -> str:
        return str(sum(1 + self.heights[x][y]
                       for x, y in self.get_lows()))

    def get_basin_sizes(self, x, y) -> int:
        if self.is_out(x, y) or self.heights[x][y] == 9:
            return 0

        self.heights[x][y] = 9
        return 1 + sum(self.get_basin_sizes(x + dx, y + dy) for dx, dy in self.neighbours)

    def part2(self) -> str:
        lows = self.get_lows()
        basins = []
        for x, y in lows:
            basins.append(self.get_basin_sizes(x, y))

        return str(reduce(mul, sorted(basins, reverse=True)[:3]))


if __name__ == "__main__":
    day9 = Day9("day9input.txt")
    print("Part 1: ", day9.part1())
    print("Part 2: ", day9.part2())
