import pathlib
import sys
from collections import defaultdict
from copy import deepcopy


def parse(parsedata):
    return list(map(int, parsedata.splitlines()))

def next_secret(secret):
    secret = ((secret * 64) ^ secret ) % 16777216
    secret = ((secret // 32) ^ secret ) % 16777216
    secret = ((secret * 2048) ^ secret ) % 16777216
    return secret

def part1(data):
    for _ in range(2000):
        data = [next_secret(secret) for secret in data ]
    return sum(data)


def part2(data):
    prices = []
    for secret in data:
        price = []
        for _ in range(2000):
            secret = next_secret(secret)
            price.append(secret % 10)
        prices.append(price)

    changes = []
    for price in prices:
        inner_changes = []
        for i in range(len(price) - 1):
            inner_changes.append(price[i + 1] - price[i])
        changes.append(inner_changes)

    amounts = defaultdict(int)
    for buyer, change in enumerate(changes):
        keys = set()
        price = prices[buyer]
        for i in range(len(change) - 3):
            key = tuple(change[i:i + 4])
            if key not in keys:
                keys.add(key)
                amounts[key] += price[i + 4]

    return max(amounts.values())



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