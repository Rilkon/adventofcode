import math
import pathlib
import sys
from collections import defaultdict
import regex as re

deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def solve_parts(parsedata):

    symbols = set()
    gears = set()
    # easier handling of append/adding later avoiding key error
    gear_ratio_parts = defaultdict(list)

    # build sets of coordinates for symbols and gears - ignore numbers for now
    for x, line in enumerate(parsedata):
        for y, element in enumerate(line):
            if not element.isdigit() and element != ".":
                symbols.add((x, y))
                if element == "*":
                    gears.add((x, y))

    part_sum = 0
    # Second runthrough by line for the numbers
    for x, line in enumerate(parsedata):
        # finditer to allow easier access to start and end indices of the numbers
        for match in re.finditer(r"\d+", line):

            # extract the part number from the match object
            part_number = int(match.group(0))

            # Build a set of neighbors using the range from the match object + delta (8 squares around it)
            neighbors = set()
            for dx, dy in deltas:
                for y in range(match.start(), match.end()):
                    neighbors.add((x + dx, y + dy))

            # overlaps are the intersection of our saved symbols and the calculated neighbors
            overlap = symbols.intersection(neighbors)
            if len(overlap) > 0:
                part_sum += part_number
            # part 2 - Go over the overlaps and if the element overlapping is in gears (*) save it for later
            for el in overlap:
                if el in gears:
                    gear_ratio_parts[el].append(part_number)

    # Calculcate gear ratio for part 2 by using only the saved values with exactly 2 overlaps
    gear_ratio_sum = 0
    for value in gear_ratio_parts.values():
        if len(value) == 2:
            gear_ratio_sum += math.prod(value)

    return part_sum, gear_ratio_sum


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip().splitlines()
        print(solve_parts(puzzle_input))
