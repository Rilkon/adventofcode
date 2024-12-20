import pathlib
import sys
from copy import deepcopy


DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]

def parse(parsedata):

    walls = []
    start = (0,0)
    goal = (0,0)

    for y, line in enumerate(parsedata.splitlines()):
        for x, value in enumerate(line):
            if value == "#":
                walls.append((x,y))
            elif value == "S":
                start = (x,y)
            elif value == "E":
                goal = (x,y)

    return start, goal, frozenset(walls)

def man_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def calc_cheats(path, cheat_distance):


    total = 0
    for i in range(0, len(path) - 2):
        for j in range(i + 1, len(path)):
            d = man_dist(path[i], path[j])
            if d <= cheat_distance and j - i - d >= 100:
                total += 1

    return total


def racetrack_cheating(start, goal, walls, cheat_distance):
    path = [start]
    curr = start
    visited = set()

    while curr != goal:
        x, y = curr
        visited.add(curr)

        for dx, dy in DIRECTIONS:
            newpos = (x + dx, y + dy)
            if newpos not in walls and newpos not in visited:
                path.append(newpos)
                curr = newpos


    return calc_cheats(path, cheat_distance)




def part1(data):
    start, goal, walls = data
    return racetrack_cheating(start, goal, walls, cheat_distance=2)

def part2(data):
    start, goal, walls = data
    return racetrack_cheating(start, goal, walls, cheat_distance=20)

def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(deepcopy(data))
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path_taken in sys.argv[1:]:
        print(f"{path_taken}:")
        puzzle_input = pathlib.Path(path_taken).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))