from os.path import dirname, join

content     = open(join(dirname(__file__), "day12input.txt"), 'r').read()
input       = content.split("\n")

directions = {
    "E": (+1, 0),
    "W": (-1, 0),
    "N": (0, +1),
    "S": (0, -1),
}

def get_instructions(lines):
    data = []
    for line in lines:
        action = line[:1]
        value = int(line[1:])
        data.append((action, value))
    return data

def man_dist(position: (int, int)) -> int:
    return abs(position[0]) + abs(position[1])

def rot_right(position: (int, int), degree: int) -> (int, int):
    x, y = position
    if degree % 360 == 0:
        return x, y
    elif degree % 360 == 90:
        return y, -x
    elif degree % 360 == 180:
        return -x, -y
    elif degree % 360 == 270:
        return -y, x

def rot_left(position: (int, int), degree: int) -> (int, int):
    return rot_right(position, 360 - degree)

def solve_part1(instructions) -> int:
    dr = directions["E"]
    coord = (0, 0)

    for action, value in instructions:
        if action == "F":
            coord = (
                coord[0] + dr[0] * value,
                coord[1] + dr[1] * value,
            )
        elif action in directions.keys():
            coord = (
                coord[0] + directions[action][0] * value,
                coord[1] + directions[action][1] * value,
            )
        elif action == "L":
            dr = rot_left(dr, value)
        elif action == "R":
            dr = rot_right(dr, value)
    return man_dist(coord)

def solve_part2(instructions) -> int:
    coord = (0, 0)
    waypoint = (+10, +1)

    for action, value in instructions:
        if action == "F":
            coord = (
                coord[0] + waypoint[0] * value,
                coord[1] + waypoint[1] * value,
            )
        elif action in directions.keys():
            waypoint = (
                waypoint[0] + directions[action][0] * value,
                waypoint[1] + directions[action][1] * value,
            )
        elif action == "L":
            waypoint = rot_left(waypoint, value)
        elif action == "R":
            waypoint = rot_right(waypoint, value)
    return man_dist(coord)



print(solve_part1(get_instructions(input)))
print(solve_part2(get_instructions(input)))