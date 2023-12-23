from os.path import dirname, join
from collections import Counter


def get_gammarate(input: list) -> str:
    gammarate = ''
    for element in input:
        c = Counter(element)
        gammarate += max(c, key=c.get)

    return gammarate


def invert_bin(input: str) -> str:
    return ''.join('1' if i == '0' else '0' for i in input)


def part1(input: list) -> str:
    gamma = get_gammarate(zip(*lines))
    epsilon = invert_bin(gamma)
    return str(int(gamma, 2) * int(epsilon, 2))


def get_rate(input: list, o2: str, co2: str) -> int:
    mylist = input.copy()
    for i in range(len(input[0])):
        column_counter = [sum(list(map(int, column))) for column in zip(*mylist)]
        if column_counter[i] >= len(mylist) / 2:
            mylist = [x for x in mylist if x[i] == o2]
        else:
            mylist = [x for x in mylist if x[i] == co2]

        if len(mylist) <= 1:
            break
    return int(mylist[0], 2)


def part2(input: list) -> str:
    return str(get_rate(input, "1", "0") * get_rate(input, "0", "1"))


if __name__ == '__main__':
    content = open(join(dirname(__file__), "day3input.txt"), 'r').read()
    # content = open(join(dirname(__file__), "day7test.txt"), 'r').read()
    lines = content.split("\n")

    print("Part 1: " + part1(lines))
    lines = list(lines)
    print("Part 2: " + part2(lines))

