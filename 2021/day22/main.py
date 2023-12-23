import re
from time import perf_counter as pc


def parse_row(row):
    return row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])


def main():
    time1 = pc()

    rawinput = open("day22.txt").read()
    data = re.findall(r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", rawinput)

    cubes = []
    for row in data:
        state, new_lower_x, new_upper_x, new_lower_y, new_upper_y, new_lower_z, new_upper_z = parse_row(row)
        for cubeidx in range(len(cubes)):
            lower_x, upper_x, lower_y, upper_y, lower_z, upper_z = cubes[cubeidx]
            if new_lower_x > upper_x or new_upper_x < lower_x or new_lower_y > upper_y \
                    or new_upper_y < lower_y or new_lower_z > upper_z or new_upper_z < lower_z:
                continue
            cubes[cubeidx] = None
            if new_lower_x > lower_x:
                cubes.append((lower_x, new_lower_x - 1,
                              lower_y, upper_y,
                              lower_z, upper_z))
            if new_upper_x < upper_x:
                cubes.append((new_upper_x + 1, upper_x,
                              lower_y, upper_y,
                              lower_z, upper_z))
            if new_lower_y > lower_y:
                cubes.append((max(lower_x, new_lower_x), min(upper_x, new_upper_x),
                              lower_y, new_lower_y - 1,
                              lower_z, upper_z))
            if new_upper_y < upper_y:
                cubes.append((max(lower_x, new_lower_x), min(upper_x, new_upper_x),
                              new_upper_y + 1, upper_y,
                              lower_z, upper_z))
            if new_lower_z > lower_z:
                cubes.append((max(lower_x, new_lower_x), min(upper_x, new_upper_x),
                              max(lower_y, new_lower_y), min(upper_y, new_upper_y),
                              lower_z, new_lower_z - 1))
            if new_upper_z < upper_z:
                cubes.append((max(lower_x, new_lower_x), min(upper_x, new_upper_x),
                              max(lower_y, new_lower_y), min(upper_y, new_upper_y),
                              new_upper_z + 1, upper_z))
        if state == 'on':
            cubes.append((min(new_lower_x, new_upper_x), max(new_lower_x, new_upper_x), min(new_lower_y, new_upper_y),
                          max(new_lower_y, new_upper_y), min(new_lower_z, new_upper_z), max(new_lower_z, new_upper_z)))
        cubes = [cube for cube in cubes if cube is not None]

    part1_count = 0
    part2_count = 0
    for cube in cubes:
        [x1, x2, y1, y2, z1, z2] = cube
        if abs(x2) <= 50 and abs(x1) <= 50 and abs(y2) <= 50 and abs(y1) <= 50 and abs(z2) <= 50 and abs(z1) <= 50:
            part1_count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
        part2_count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

    print("Part 1: ", part1_count)
    print("Part 2: ", part2_count)
    print("Execution Time: ", pc() - time1)


if __name__ == "__main__":
    main()
