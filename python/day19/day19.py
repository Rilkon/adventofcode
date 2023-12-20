import math
import pathlib
import re
import sys
from collections import defaultdict
from copy import copy


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


def process_wf(wf, x, m, a, s):
    _key = "in"
    i = 0

    while _key not in {"A", "R"}:
        rule, _next = wf[_key][i]

        if rule is None:
            _key, i = _next, 0
            continue

        result = eval(rule)

        if result:
            _key, i = _next, 0
        else:
            i += 1

    return x + m + a + s if _key == "A" else 0


def process_wf2(_key, wf, ranges):
    if _key == "R":
        return 0

    if _key == "A":
        return math.prod(upper - lower + 1 for lower, upper in ranges.values())

    total = 0
    for rule, _next in wf[_key]:
        temp_ranges = ranges.copy()

        if rule is None:
            total += process_wf2(_next, wf, ranges)
        else:
            k, op, value = rule[0], rule[1], int(rule[2:])

            if op == ">" and ranges[k] is not None and value < ranges[k][1]:
                temp_ranges[k] = (max(value + 1, ranges[k][0]), ranges[k][1])
                total += process_wf2(_next, wf, temp_ranges)
                ranges[k] = (ranges[k][0], value) if ranges[k][0] <= value else None

            elif op == "<" and ranges[k] is not None and value > ranges[k][0]:
                temp_ranges[k] = (ranges[k][0], min(value - 1, ranges[k][1]))
                total += process_wf2(_next, wf, temp_ranges)
                ranges[k] = (value, ranges[k][1]) if value <= ranges[k][1] else None

    return total


def part1(data):
    wf, part_ratings = data
    result = 0

    for part in part_ratings:
        x, m, a, s = [int(x) for x in re.findall(r"\d+", part)]
        result += process_wf(wf, x, m, a, s)

    return result


def part2(data):
    wf, _ = data
    ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    return process_wf2("in", wf, ranges)


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
