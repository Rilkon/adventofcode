import pathlib
import sys
import numpy as np
import pandas as pd


def parse(parsedata):
    oasishistory = [[np.nan] + [int(x) for x in line.split(" ")] + [np.nan] for line in parsedata.splitlines()]
    df = pd.DataFrame(oasishistory)
    df = df.interpolate(method="barycentric", order=1, axis=1, limit_direction="both").round()
    return df


def part1(data):
    return int(sum(data[len(data.columns) - 1].tolist()))


def part2(data):
    return int(sum(data[0].tolist()))


def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
