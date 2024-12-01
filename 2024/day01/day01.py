import pathlib
import sys
from copy import deepcopy


def parse(parsedata):

    leftlist = []
    rightlist = []

    for line in parsedata.splitlines():
        left, right = line.split("   ")
        leftlist.append(int(left))
        rightlist.append(int(right))

    return sorted(leftlist), sorted(rightlist)


def part1(data):
    leftlist, rightlist = data
    totaldistance = 0

    for i in range(len(data[0])):
        diff = abs(rightlist.pop() - leftlist.pop())
        totaldistance += diff

    return totaldistance


def part2(data):
    leftlist, rightlist = data
    similarityscore = 0

    for i in range(len(data[0])):
        value = leftlist.pop()
        c = rightlist.count(value)
        inc = c * value
        similarityscore += inc

    return similarityscore


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
