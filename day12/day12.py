import itertools
import pathlib
import sys


def parse(parsedata):
    springs = []

    for line in parsedata.splitlines():
        groups = [int(x) for x in line.split(" ")[1].split(",")]
        temp = [line.split(" ")[0], groups]
        springs.append(temp)

    return springs


def get_grouping(springs):
    groups = []
    for value in springs.split("."):
        if (c := value.count("#")) >= 1:
            groups.append(c)
    return groups


def get_combinations(springs):
    replacements = [".", "#"]
    combinations = []

    for combination in itertools.product(replacements, repeat=springs.count("?")):
        temp = iter(combination)
        result = ''.join(char if char != "?" else next(temp) for char in springs)
        combinations.append(result)

    return combinations


def unfold_data(data):
    result = []

    for springs, groups in data:
        result.append([springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs, groups * 5])

    return result


def part1(data):
    count = 0
    for springs, groups in data:
        for combi in get_combinations(springs):
            if get_grouping(combi) == groups:
                count += 1

    return count


def part2(data):
    return part1(unfold_data(data))


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
