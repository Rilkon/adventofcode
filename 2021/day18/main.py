import os
from functools import reduce
from math import floor, ceil
from time import perf_counter as pc


def add_snail(x, y) -> int:
    return reduce_snail([x, y])


def reduce_snail(x) -> int:
    """To reduce a snailfish number,
    you must repeatedly do the first action in this list
    that applies to the snailfish number:"""
    """
    If any pair is nested inside four pairs, the leftmost such pair explodes.
    If any regular number is 10 or greater, the leftmost such regular number splits.

    Once no action in the above list applies, the snailfish number is reduced."""
    while True:
        boom, x, _, _ = explode_snail(x)
        if not boom:
            old_x = x
            x = split_snail(x)
            if x == old_x:
                break
    return x


def explode_snail(x, n=0) -> [bool, int, int, int]:
    """ n = nesting
    If any pair is nested inside four pairs, the leftmost such pair explodes.

    To explode a pair, the pair's left value is added to the first regular number
    to the left of the exploding pair (if any), and the pair's right value is added to
    the first regular number to the right of the exploding pair (if any).
    Exploding pairs will always consist of two regular numbers.
    Then, the entire exploding pair is replaced with the regular number 0."""

    if isinstance(x, int):
        # if x is already int, just return it as such and signal to end loop
        return False, x, 0, 0
    if n < 4:
        # nesting level still below 4
        # explode left side
        boom, next_x, left, right = explode_snail(x[0], n + 1)
        if boom:
            x = [next_x, add_to("left", x[1], right)]
            return True, x, left, 0
        # explode right side
        boom, next_x, left, right = explode_snail(x[1], n + 1)
        if boom:
            x = [add_to("right", x[0], left), next_x]
            return True, x, 0, right
        return False, x, 0, 0
    else:
        return True, 0, x[0], x[1]


def split_snail(x) -> list:
    """
    If any regular number is 10 or greater, the leftmost such regular number splits.

    To split a regular number, replace it with a pair; the left element
    of the pair should be the regular number divided by two and rounded down,
    while the right element of the pair should be the regular number divided by
    two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on."""
    if isinstance(x, int):
        if x >= 10:
            return [floor(x / 2), ceil(x / 2)]
        else:
            return x

    left = split_snail(x[0])
    if left != x[0]:
        return [left, x[1]]
    right = split_snail(x[1])
    return [x[0], right]


def add_to(side, x, y) -> list:
    if isinstance(x, int):
        return x + y
    else:
        if side == "left":
            return [add_to("left", x[0], y), x[1]]
        else:
            return [x[0], add_to("right", x[1], y)]


def magnitude(x) -> int:
    if isinstance(x, int):
        return x
    else:
        return magnitude(x[0]) * 3 + magnitude(x[1]) * 2


def part1(input) -> str:
    result = reduce(add_snail, input)
    return str(magnitude(result))

def part2(input) -> str:

    currentmax = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if i != j:
                result = add_snail(input[i], input[j])
                newsum = magnitude(result)
                if newsum > currentmax:
                    currentmax = newsum
    return str(currentmax)



def main():
    time1 = pc()
    filename = "day18.txt"

    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        data = [eval(line) for line in f.readlines()]


    print("Part1: ", part1(data.copy()))
    print("Part2: ", part2(data.copy()))
    print("Excution Time: ", pc() - time1)


if __name__ == "__main__":
    main()
