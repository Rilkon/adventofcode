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


def get_arrangement_nums(spring, groups, known):

    if spring == "" and len(groups) != 0:
        return 0
    if spring == "" and len(groups) == 0:
        return 1


    if spring[0] == ".":
        return get_arrangement_nums(spring[1:], groups, known)
    elif spring[0] == "?":
        temp1 = "." + spring[1:]
        temp2 = "#" + spring[1:]
        return get_arrangement_nums(temp1, groups, known) + get_arrangement_nums(temp2, groups, known)
    elif spring[0] == "#":

        if len(groups) == 0:
            return 0
        if groups[0] <= len(spring.split(".")[0]):
            temp = spring[groups[0]:]
            groups = groups[1:]
            return get_arrangement_nums(temp, groups, known)

    return 0



def unfold_data(data):
    result = []

    for springs, groups in data:
        result.append(["?".join([springs]*5), groups * 5])

    return result


def part1(data):
    count = 0
    for springs, groups in data:
        for combi in get_combinations(springs):
            if get_grouping(combi) == groups:
                count += 1

    return count


def part2(data):

    result = []
    for springs, groups in unfold_data(data):
        result.append(get_arrangement_nums(springs, groups, ""))

    print(result)
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
