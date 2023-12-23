import itertools
import math
import pathlib
import sys
import re
from collections import defaultdict


def parse(parsedata):
    instructions = parsedata.splitlines()[0]
    network = defaultdict(list)
    for line in parsedata.splitlines()[2:]:
        m = re.match(r"([A-Za-z0-9]+) = \(([A-Za-z0-9]+), ([A-Za-z0-9]+)\)", line)
        network[m.group(1)] = {"L": m.group(2), "R": m.group(3)}

    return instructions, network


def part1(data):
    instructions, network = data
    current = "AAA"
    for step, el in enumerate(itertools.cycle(instructions), start=1):
        current = network[current][el]
        if current == "ZZZ":
            break

    return step


def part2(data):
    instructions, network = data
    ghosts = [k for k in network.keys() if k.endswith("A")]
    steps = []
    for ghost in ghosts:
        for step, el in enumerate(itertools.cycle(instructions), start=1):
            ghost = network[ghost][el]
            if ghost.endswith("Z"):
                steps.append(step)
                break

    return math.lcm(*steps)


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
