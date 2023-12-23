import pathlib
import sys
from Levenshtein import distance as levenshtein_distance


def parse(parsedata):
    row_patterns = []
    col_patterns = []
    for pattern in parsedata.split("\n\n"):
        row_patterns.append([line for line in pattern.splitlines()])
        col_patterns.append(["".join(c) for c in zip(*pattern.splitlines())])

    return row_patterns, col_patterns


def find_mirror(pattern, smudge=0):
    count = 0
    for i in range(1, len(pattern)):
        flipped = reversed(pattern[:i])
        remaining = pattern[i:]

        dist = 0
        for a, b in zip(remaining, flipped):
            dist += levenshtein_distance(a, b, score_cutoff=1)
            if dist > smudge:
                break

        if dist == smudge:
            count += i

    return count


def part1(data):
    row_patterns, col_patterns = data

    row = sum(find_mirror(pattern) for pattern in row_patterns)
    col = sum(find_mirror(pattern) for pattern in col_patterns)

    return (row * 100) + col


def part2(data):
    row_patterns, col_patterns = data

    row = sum(find_mirror(pattern, 1) for pattern in row_patterns)
    col = sum(find_mirror(pattern, 1) for pattern in col_patterns)

    return (row * 100) + col


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
