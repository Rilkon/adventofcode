import pathlib
import sys
from copy import deepcopy
import re


def parse(parsedata):
    machines = []
    for machine in parsedata.split("\n\n"):
        match = re.findall(r"\d+", machine)
        machines.append(list(map(int, match)))
    return machines


def get_cheapest_price_or_zero(machine):
    '''
    px = ax * a + bx * b
    py = ay * a + by * b

    px = ax * a + bx * b
    px - bx * b = ax * a
    a = (px - bx * b) / ax

    Insert in: py = ay * a + by * b
    py = ay * (px - bx * b) / ax + by * b
    py = (ay * px - ay * bx * b) / ax + by * b
    ax * py = ay * px - ay * bx * b + ax * by * b
    ax * py = ay * px + b * (ax * by - ay * bx)
    ax * py - ay * px = b * (ax * by - ay * bx)
    b = (ax * py - ay * px) / (ax * by - ay * bx)
    '''

    ax, ay, bx, by, prize_x, prize_y = machine
    res = 0

    b = (ax * prize_y - ay * prize_x) / (ax * by - ay * bx)
    a = (prize_x - bx * b) / ax

    if a.is_integer() and b.is_integer():
        res = a * 3 + b

    return int(res)

def part1(machines):
    return sum(get_cheapest_price_or_zero(machine) for machine in machines)

def part2(machines):
    offset = 10_000_000_000_000
    new_machines = [machine[:4] + [machine[4] + offset, machine[5] + offset] + machine[6:] for machine in machines]
    return sum(get_cheapest_price_or_zero(machine) for machine in new_machines)

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