import itertools
import pathlib
import sys
import z3


class Hailstone():

    def __init__(self, position, velocity, id):
        self.id = id

        self.px = position[0]
        self.py = position[1]
        self.pz = position[2]

        self.vx = velocity[0]
        self.vy = velocity[1]
        self.vz = velocity[2]

        self.slope = self.vy / self.vx
        self.intercept = self.py - (self.slope * self.px)

    def __repr__(self):
        return "Hailstone({!r})".format(self.__dict__)


def parse(parsedata):
    hailstones = []

    for i, line in enumerate(parsedata.splitlines(), start=1):
        left, right = line.split("@")

        pos = tuple(map(int, left.strip().split(",")))
        vel = tuple(map(int, right.strip().split(",")))

        hailstones.append(Hailstone(pos, vel, i))

    area = [7, 27] if len(hailstones) < 20 else [200_000_000_000_000, 400_000_000_000_000]

    return hailstones, area


def part1(data):
    hailstones, area = data

    count = sum(
        1 for hail, stone in itertools.combinations(hailstones, r=2)
        if hail.slope != stone.slope
        and (x := (stone.intercept - hail.intercept) / (hail.slope - stone.slope))
        and (y := hail.slope * x + hail.intercept)
        and (t1 := (x - hail.px) / hail.vx) >= 0
        and (t2 := (x - stone.px) / stone.vx) >= 0
        and area[0] <= x <= area[1]
        and area[0] <= y <= area[1]
    )
    return count


def part2(data):
    hailstones, _ = data
    x, y, z, dx, dy, dz = map(z3.Real, ["x", "y", "z", "dx", "dy", "dz"])
    solver = z3.Solver()
    for i, stone in enumerate(hailstones):
        t = z3.Real(f"t{i}")
        solver.add(t > 0)
        solver.add(x + t * dx == stone.px + t * stone.vx)
        solver.add(y + t * dy == stone.py + t * stone.vy)
        solver.add(z + t * dz == stone.pz + t * stone.vz)

    solver.check()
    return solver.model().eval(x + y + z)


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
