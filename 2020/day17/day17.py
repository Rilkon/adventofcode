from os.path import dirname, join
from collections import Counter
from itertools import product
from operator import add

content     = open(join(dirname(__file__), "./day17input.txt"), 'r').read()
input_data  = content.split("\n")

def build_plane(lines, dimensions):
    plane = set()
    for row, line in enumerate(lines):
        for col, elem in enumerate(line):
            if elem == '#':
                cell = dimensions * [0,]
                cell[0], cell[1] = col, row
                plane.add(tuple(cell))
    return plane

def count_neighbors(plane, dimensions):
    neigh_counter = Counter()
    for cell in plane:
        for delta in product(range(-1, 2), repeat=dimensions):
            if delta != dimensions * (0,):
               neigh_counter[tuple(map(add, cell, delta))] += 1
    return neigh_counter

def extend_plane(plane,cycles, dimensions):
    new_plane = set()
    for _ in range(cycles):
        new_plane = set()
        neigh_counter = count_neighbors(plane, dimensions)

        for cell, count in neigh_counter.items():
            if count == 3 or (cell in plane and count == 2):
                new_plane.add(cell)
        plane = new_plane
    return new_plane

def perform_cycles(lines, cycles, dimensions):
    plane = build_plane(lines, dimensions)
    plane = extend_plane(plane, cycles, dimensions)
    return len(plane)


print("Part 1:", perform_cycles(input_data, 6, 3))
print("Part 2:", perform_cycles(input_data, 6, 4))