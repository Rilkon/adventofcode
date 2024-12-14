import math
import pathlib
import re
import sys
from collections import defaultdict
from copy import deepcopy

max_x = 101
max_y = 103

def parse(parsedata):

    robots = []
    for robot in parsedata.splitlines():
        pattern = r"[\d-]+"
        matches = re.findall(pattern, robot)
        robots.append((list(map(int, matches))))

    return robots


def move_with_teleport(x, y, vx, vy):
    global max_x, max_y
    x_new = x + vx
    y_new = y + vy

    x_wrapped = (x_new % max_x + max_x) % max_x
    y_wrapped = (y_new % max_y + max_y) % max_y

    return x_wrapped, y_wrapped

def get_quadrants():
    global max_x, max_y

    mid_x = max_x // 2
    mid_y = max_y // 2

    quadrants = [[], [], [], []]

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if x == mid_x or y == mid_y:
                continue  # Skip the middle lines
            if x > mid_x and y > mid_y:
                quadrants[0].append([x, y])
            elif x < mid_x and y > mid_y:
                quadrants[1].append([x, y])
            elif x < mid_x and y < mid_y:
                quadrants[2].append([x, y])
            elif x > mid_x and y < mid_y:
                quadrants[3].append([x, y])

    return quadrants


def move_robots(data):
    robots = data
    print_tree = False
    count = 0
    result = 0


    for i in range(25000):
        temp = []
        for robot in robots:
            x, y, vx, vy = robot
            robot = move_with_teleport(x, y, vx, vy)
            temp.append([robot[0], robot[1], vx, vy])

        robots = temp

        # save part 1 result
        if i == 99:
            result = math.prod(sum([robot[0], robot[1]] in coords for robot in robots) for coords in get_quadrants())

        # part2
        coordinates = defaultdict(str)
        coordinates.update({(robot[0], robot[1]): "X" for robot in robots})

        if len(coordinates) > count:
            print(i + 1)
            count = len(coordinates)
            print_tree = True

        if print_tree:
            with open("out.txt", "w") as f:
                print(f"--------------- Second {i + 1} ----------------", file=f)

                content = [["."] * max_x for _ in range(max_y)]

                grid = coordinates
                for key, value in grid.items():
                    content[key[1]][key[0]] = value

                width = len(str(max(max_x, max_y) - 1))
                contentline = "| values |"

                for row in content:
                    values = " ".join(f"{v:{width}s}" for v in row)
                    line = contentline.replace("values", values)
                    print(line, file=f)

        print_tree = False

    return f"Part1: {result}, Part2: Check 'out.txt' or last printed value before Part 1 solution"

def part1(data):
    return move_robots(data)

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