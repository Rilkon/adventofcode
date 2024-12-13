import pathlib
import sys
from itertools import repeat

def parse(parsedata):
    file_system = []
    blocks_and_gaps = []
    n = 0

    for i, value in enumerate(parsedata):
        count = int(value)
        if i % 2 == 0:
            file_system.extend(repeat(n, count))
            blocks_and_gaps.append((n, count))
            n += 1
        else:
            file_system.extend(repeat("X", count))
            blocks_and_gaps.append((None, count))

    return file_system, blocks_and_gaps

def part1(file_system):
    front = 0
    back = len(file_system) - 1

    while front < back:
        if file_system[front] == "X":
            while back > front and file_system[back] == "X":
                back -= 1

            if back > front:
                file_system[front], file_system[back] = file_system[back], "X"

        front += 1

    return sum(value * i for i, value in enumerate(file_system) if value != "X")

def part2(blocks_and_gaps):
    file_system = []
    gaps = []
    blocks = []

    for block_id, length in blocks_and_gaps:
        if block_id is not None:
            blocks.append((len(file_system), block_id, length))
            file_system.extend([block_id] * length)
        else:
            gaps.append((length, len(file_system)))
            file_system.extend([None] * length)

    for block in reversed(blocks):
        (pos, block_id, length) = block
        for i, (gap_length, gap_pos) in enumerate(gaps):
            if gap_pos > pos:
                break

            if gap_length >= length:
                for j in range(length):
                    file_system[pos + j] = None
                    file_system[gap_pos + j] = block_id

                diff = gap_length - length
                if diff > 0:
                    gaps[i] = (diff, gap_pos + length)
                else:
                    gaps.pop(i)
                break

    return sum(value * i if value is not None else 0 for i, value in enumerate(file_system))

def solve(puzzle_data):
    data, blocks_and_gaps = parse(puzzle_data)
    solution1 = part1(data)
    solution2 = part2(blocks_and_gaps)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))