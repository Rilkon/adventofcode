from os.path import dirname, join
import statistics


def part1(input: list) -> str:
    return str(sum([abs(x - statistics.median(input)) for x in input]))


def weight(x: int, y: int):
    return abs(x-y) * (abs(x-y)+1)/2


def part2(input: list) -> str:

    results = []
    for i in range(0, max(input) + 1):
        results.append(sum([weight(x, i) for x in input]))
    return min(results)


if __name__ == '__main__':
    content = open(join(dirname(__file__), "day7input.txt"), 'r').read()
    lines = list(map(int, content.split(",")))
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))
