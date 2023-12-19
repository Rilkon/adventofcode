import pathlib
import re
import sys
from collections import defaultdict


def parse(parsedata):

    first, second = parsedata.split("\n\n")

    first = first.split("\n")
    part_ratings = second.split("\n")

    wf = defaultdict(list)

    for line in first:
        name, remaining = line[:-1].split("{")
        rules = remaining.split(",")
        for rule in rules:
            if ":" in rule:
                wf[name].append(tuple(rule.split(":")))
            else:
                wf[name].append((None, rule))

    return wf, part_ratings


def process_workflow(wf, x, m, a, s):
    _key = 'in'
    i = 0

    while _key not in {"A", "R"}:
        rule, next_state = wf[_key][i]

        if rule is None:
            _key, i = next_state, 0
            continue

        result = eval(rule)

        if result:
            _key, i = next_state, 0
        else:
            i += 1

    return x + m + a + s if _key == "A" else 0


def part1(data):

    wf, part_ratings = data
    result = 0

    for part in part_ratings:
        x,m,a,s = [int(x) for x in re.findall(r"\d+", part)]
        result += process_workflow(wf, x,m,a,s)

    return result


def part2(data):

    ranges = {z: [0, 4000] for z in "xmas"}
    return ""


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
