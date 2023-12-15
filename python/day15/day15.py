import pathlib
import sys
from collections import OrderedDict, defaultdict


def parse(parsedata):
    assert r_hash("HASH") == 52
    return parsedata.split(",")


def r_hash(line):
    curr = 0
    for el in line:
        curr = ((curr + ord(el)) * 17) % 256
    return curr


def part1(data):
    return sum(r_hash(line) for line in data)


def part2(data):
    hashmap = defaultdict(OrderedDict)

    for label in data:
        if "=" in label:
            _key, focal_length = label.split("=")
            hashmap[r_hash(_key)][_key] = int(focal_length)
        elif "-" in label:
            _key = label.split("-")[0]
            hashmap[r_hash(_key)].pop(_key, None)

    result = 0
    for _key in hashmap:
        for i, focal_length in enumerate(hashmap[_key].values(), start=1):
            print(_key, hashmap[_key].items())
            print(f"curr result {result} + new value {(1 + _key) * i * focal_length}")
            result += (1 + _key) * i * focal_length

    print(hashmap)
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
