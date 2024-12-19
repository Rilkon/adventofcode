import functools
import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    patterns, designs = parsedata.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()
    return patterns, designs


@functools.cache
def count_patterns(design, patterns):
    if len(patterns) == 0:
        return 0
    if len(design) == 0:
        return 1
    return sum(count_patterns(design[len(towel):], patterns) for towel in patterns if design.startswith(towel))


def part1(data):
    patterns, designs = data
    return sum(1 for design in designs if count_patterns(design, frozenset(patterns)) > 0)


def part2(data):
    patterns, designs = data
    return sum(count_patterns(design, frozenset(patterns)) for design in designs)


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
