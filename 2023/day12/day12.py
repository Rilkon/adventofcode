import functools
import pathlib
import sys


def parse(parsedata):
    combined = []

    for line in parsedata.splitlines():
        groups = [int(x) for x in line.split(" ")[1].split(",")]
        temp = [line.split(" ")[0], tuple(groups)]
        combined.append(temp)

    return combined


@functools.cache
def get_valid_arrangements(springs, groups, steps=0):
    if not springs:
        if len(groups) == 1 and groups[0] == steps or len(groups) == 0 and steps == 0:
            return 1
        else:
            return 0

    curr_spring = springs[0]
    new_springs = springs[1:]

    if not groups:
        curr_group = 0
    else:
        curr_group = groups[0]

    new_groups = tuple(groups[1:])

    if curr_spring == ".":
        if steps == 0:
            return get_valid_arrangements(new_springs, groups, 0)
        elif steps == curr_group:
            return get_valid_arrangements(new_springs, new_groups, 0)
        else:
            return 0
    elif curr_spring == '?':
        return (get_valid_arrangements("#" + new_springs, groups, steps)
                + get_valid_arrangements("." + new_springs, groups, steps))
    elif curr_spring == '#':
        if steps > curr_group:
            return 0
        else:
            return get_valid_arrangements(new_springs, groups, steps + 1)

    return 0


def unfold_data(data):
    unfolded = []
    for springs, groups in data:
        unfolded.append(["?".join([springs] * 5), tuple(groups * 5)])
    return unfolded


def part1(data):
    result = []
    for springs, groups in data:
        result.append(get_valid_arrangements(springs, groups))
    return sum(result)


def part2(data):
    result = []
    for springs, groups in unfold_data(data):
        result.append(get_valid_arrangements(springs, groups))

    return sum(result)


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
