import functools
import pathlib
import sys
from copy import deepcopy
from itertools import product

NUM = {"7": (0, 0), "8": (1, 0), "9": (2, 0),
       "4": (0, 1), "5": (1, 1), "6": (2, 1),
       "1": (0, 2), "2": (1, 2), "3": (2, 2),
       " ": (0, 3), "0": (1, 3), "A": (2, 3)}

DIR = {" ": (0, 0), "^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


def parse(parsedata):
    return parsedata.splitlines()


@functools.cache
def get_paths(keypad):
    if keypad == "NUM":
        button_locations = NUM
    elif keypad == "DIR":
        button_locations = DIR
    else:
        raise Exception("Keypad not supported")

    path_taken = {}
    for a, b in product((button for button in button_locations if button != " "), repeat=2):

            (ax, ay) = button_locations[a]
            (bx, by) = button_locations[b]
            dx = bx - ax
            dy = by - ay

            moves_x = ""
            for _ in range(dx):
                moves_x += ">"
            for _ in range(-dx):
                moves_x += "<"

            moves_y = ""
            for _ in range(dy):
                moves_y += "v"
            for _ in range(-dy):
                moves_y += "^"

            if dx == 0:
                path_taken[a, b] = [moves_y]
            elif dy == 0:
                path_taken[a, b] = [moves_x]
            elif (bx, ay) == button_locations[" "] :
                path_taken[a, b] = [moves_y + moves_x]
            elif (ax, by) == button_locations[" "]:
                path_taken[a, b] = [moves_x + moves_y]
            else:
                path_taken[a, b] = [moves_x + moves_y, moves_y + moves_x]

    return path_taken


@functools.cache
def get_presses(code, d, keypad="NUM"):

    if d == 0:
        return len(code)

    keypaths = get_paths(keypad)

    result = 0
    for pair in zip("A" + code, code):
        min_presses = float("inf")
        for path in keypaths[pair]:
            presses = get_presses(path + "A", d - 1, "DIR")
            if presses < min_presses:
                min_presses = presses
        result += min_presses

    return result


def part1(data):
    return sum(get_presses(code, 2 + 1) * int(code[:-1]) for code in data)


def part2(data):
    return sum(get_presses(code, 25 + 1) * int(code[:-1]) for code in data)


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
