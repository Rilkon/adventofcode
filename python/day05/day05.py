import pathlib
import sys


def parse(parsedata):
    blocks = parsedata.split("\n\n")
    seeds = []

    for x in blocks[0].split(":")[1].split():
        seeds.append((int(x)))

    almanac = []
    for i in range(1, len(blocks)):
        outer = []
        for s in blocks[i].split("\n")[1:]:
            inner = []
            for x in s.split():
                inner.append(int(x))
            outer.append(inner)
        almanac.append(outer)

    return (seeds, almanac)


def translate_value(value, mappings):
    for mapping in mappings:
        if mapping[1] <= value <= mapping[1] + mapping[2]:
            new_value = abs(value - mapping[1]) + mapping[0]
            return new_value
        else:
            new_value = value

    return new_value


def traverse_mapping(seed, almanac):
    for mappings in almanac:
        seed = translate_value(seed, mappings)

    return seed


def part1(data):
    result = []
    for seed in data[0]:
        result.append(traverse_mapping(seed, data[1]))

    return min(result)


def part2(data):
    # For part 2, run via pypy
    result = 999999999999
    for a, b in zip(data[0][::2], data[0][1::2]):
        for i in range(a, a+b):
            result = min(result, traverse_mapping(i, data[1]))

    return result


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
