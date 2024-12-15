import pathlib
import sys
from collections import defaultdict
from copy import deepcopy

max_x = 0
max_y = 0

DIRECTIONS = {"^": (-1, 0),
              ">": (0, 1),
              "<": (0, -1),
              "v": (1, 0)}


def parse(parsedata):
    global max_x, max_y, start

    warehouse = defaultdict(str)
    walls = set()
    boxes = set()
    start = (0, 0)

    grid, instructions = parsedata.split("\n\n")

    for x, line in enumerate(grid.splitlines()):
        for y, value in enumerate(line):
            warehouse[(x, y)] = value
            if value == "#":
                walls.add((x, y))
            elif value == "@":
                start = (x, y)
            elif value == "O":
                boxes.add((x, y))

    max_x = x
    max_y = y

    instructions = "".join(line for line in instructions.splitlines())

    return instructions, warehouse, walls, boxes, start


def build_and_display_grid(boxes, walls, position):
    for x in range(max_x):
        for y in range(max_y):
            if (x, y) in boxes:
                print("O", end="")
            elif (x, y) in walls:
                print("#", end="")
            elif (x, y) == position:
                print("@", end="")
            else:
                print(".", end="")
        print()
    print("--------------------------")


def move_and_push(instr, pos, walls, boxes):
    dxy = DIRECTIONS[instr]
    dx, dy = dxy

    x, y = pos
    new_pos = (x + dx, y + dy)

    # wall
    if new_pos in walls:
        # print(f"New position in wall: {pos, boxes}")
        return pos, boxes

    # normal movement
    if new_pos not in boxes and new_pos not in walls:
        # print(f"Normal movement: {new_pos, boxes}")
        return new_pos, boxes

    # box
    if new_pos in boxes:
        # print(f"New position would be a box")
        next_box = new_pos
        while next_box in boxes:
            next_box = (next_box[0] + dx, next_box[1] + dy)
        if next_box in walls:
            return pos, boxes
        boxes.remove(new_pos)
        boxes.add(next_box)

    return new_pos, boxes


def lanternfish_gps(a):
    return a[1] + (100 * a[0])


def part1(data):
    instructions, warehouse, walls, boxes, start = data

    pos = start

    build_and_display_grid(boxes, walls, pos)

    for instruction in instructions:
        pos, boxes = move_and_push(instruction, pos, walls, boxes)

        #build_and_display_grid(boxes, walls, pos)

    return sum(lanternfish_gps(coord) for coord in boxes)


def part2(data):
    return ""


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
