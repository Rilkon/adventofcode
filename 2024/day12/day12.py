import pathlib
import sys
from collections import defaultdict
from copy import deepcopy
from shapely.geometry.geo import box
from shapely.geometry.multipolygon import MultiPolygon
from shapely.set_operations import union, unary_union


def parse(parsedata):


    regions = defaultdict(MultiPolygon)
    for x, line in enumerate(parsedata.splitlines()):
        for y, value in enumerate(line):
            new_region =  box(x, y, x + 1, y + 1 )
            regions[value] = union(regions[value], new_region)

    return regions

def calc_price(poly):
    return poly.area * poly.length


def calc_bulk_price(poly):
    p = unary_union(poly).normalize().simplify(0.1)
    sides = len(p.exterior.coords) - 1
    for interior in p.interiors:
        sides += len(interior.coords) - 1
    return p.area * sides

def part1(data):
    result = 0
    for poly in data.values():
        if poly.geom_type == "Polygon":
            result += calc_price(poly)
        else:
            for p in poly.geoms:
                result += calc_price(p)

    return result



def part2(data):
    result = 0
    for poly in data.values():
        if poly.geom_type == "Polygon":
            result += calc_bulk_price(poly)
        else:
            result += sum(calc_bulk_price(subpoly) for subpoly in poly.geoms)

    return result

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