import pathlib
import sys
from copy import deepcopy


def parse(parsedata):
    top, bottom = parsedata.split("\n\n")

    rules = {}
    for rule in top.splitlines():
        left, right = map(int, rule.split("|"))
        if right not in rules:
            rules[right] = [left]
        else:
            rules[right].append(left)

    updates = []
    for line in bottom.splitlines():
        updates.append(list(map(int, line.split(","))))

    return rules, updates


def part1(data):

    rules, updates = data
    result = 0
    for update in updates:
        valid = True
        for i, num in enumerate(update):
            if num in rules:
                pages = rules[num]
                if any(page in update[i + 1:] for page in pages):
                    valid = False
                    break
        if valid:
            result += update[len(update) // 2]

    return result


def part2(data):
    rules, updates = data
    falseUpdates = []
    for update in updates:
        for i, num in enumerate(update):
            if num in rules:
                pages = rules[num]
                if any(page in update[i + 1:] for page in pages):
                    falseUpdates.append(update)
                    break

    result = 0
    for update in falseUpdates:
        for n in range(len(update) - 1, 0, -1):
            swapped = False
            for i in range(n):
                if update[i] in rules and update[i + 1] in rules[update[i]]:
                    update[i], update[i + 1] = update[i + 1], update[i]
                    swapped = True
            if not swapped:
                break

        result += update[len(update) // 2]

    return result


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
