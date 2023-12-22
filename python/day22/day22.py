import pathlib
import sys


class Brick:
    def __init__(self, start, end, brick_id):
        self.x1, self.y1, self.z1 = start
        self.x2, self.y2, self.z2 = end
        self.id = brick_id

    def lower_by_one(self):
        self.z1 -= 1
        self.z2 -= 1

    def get_below_coordinates(self):
        result = []
        z = max(1, self.z1 - 1)
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                result.append((x, y, z))
        return None if z == self.z1 else result

    def get_coordinates(self):
        return [(x, y, z) for x in range(self.x1, self.x2 + 1)
                for y in range(self.y1, self.y2 + 1)
                for z in range(self.z1, self.z2 + 1)]


class Grid:
    def __init__(self, max_x, max_y, max_z):
        self.grid = {}
        self.bricks = {}
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z

    def add_brick(self, brick):
        self.bricks[brick.id] = brick

    def build_grid(self):
        for x in range(self.max_x):
            for y in range(self.max_y):
                for z in range(self.max_z):
                    self.grid[(x, y, z)] = "."
        for brick in self.bricks.values():
            for coords in brick.get_coordinates():
                self.grid[coords] = brick.id

    def fall_down(self, brick):
        current = brick.get_coordinates()
        below = brick.get_below_coordinates()
        if not below:
            return False
        fell_down = all(self.grid[coords] == "." for coords in below)
        if fell_down:
            for coords in current:
                self.grid[coords] = "."
            brick.lower_by_one()
            for coords in brick.get_coordinates():
                self.grid[coords] = brick.id
        return fell_down

    def all_fall_down(self):
        for brick in sorted(self.bricks.values(), key=lambda s: s.z1):
            while self.fall_down(brick):
                continue

    def disintegrate(self):
        result = 0
        for brick in self.bricks.values():
            removable = True
            for below_brick in self.bricks.values():
                below = below_brick.get_below_coordinates()
                if not below:
                    continue
                vals = {self.grid[coords] for coords in below if self.grid[coords] != "."}
                if brick.id in vals and len(vals) == 1:
                    removable = False
                    break
            if removable:
                result += 1
        return result

    def chain_rection(self):
        belows = {
            brick.id: {self.grid[coords] for coords in brick.get_below_coordinates() if self.grid[coords] != "."}
            for brick in self.bricks.values() if brick.get_below_coordinates()}
        result = 0
        for brick_id in self.bricks.keys():
            removed = {brick_id}
            while True:
                changed = False
                for _key, values in belows.items():
                    if _key not in removed and values.issubset(removed):
                        changed = True
                        removed.add(_key)
                if not changed:
                    break
            result += len(removed) - 1
        return result


def parse(parsedata):
    grid = Grid(10, 10, 1000)

    for i, line in enumerate(parsedata.splitlines()):
        left, right = line.split("~")
        start = map(int, left.split(","))
        end = map(int, right.split(","))

        grid.add_brick(Brick(start, end, i))

    return grid


def part1and2(grid):
    grid.build_grid()
    grid.all_fall_down()
    return grid.disintegrate(), grid.chain_rection()


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1and2(data)
    return solution1


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
