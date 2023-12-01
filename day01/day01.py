import pathlib
import sys
import regex as re

translate = {"one": "1",
             "two": "2",
             "three": "3",
             "four": "4",
             "five": "5",
             "six": "6",
             "seven": "7",
             "eight": "8",
             "nine": "9",
             "1": "1",
             "2": "2",
             "3": "3",
             "4": "4",
             "5": "5",
             "6": "6",
             "7": "7",
             "8": "8",
             "9": "9"}

def parse_part1(parsedata):

    result = []
    for line in parsedata.splitlines():
        numbers = re.findall(r'\d', line)
        if len(numbers) == 1:
            numbers.append(numbers[0])

        result.append(numbers)

    return result

def parse_part2(parsedata):

    result = []
    for line in parsedata.splitlines():
        r = re.compile(r"\d | one | two | three | four | five | six | seven | eight | nine", flags=re.I | re.X)
        numbers = r.findall(line, overlapped=True)
        if len(numbers) == 1:
            numbers.append(numbers[0])

        result.append(numbers)

    return result


def part1and2(data):
    sum_result = 0
    for ar in data:
        l = len(ar)
        firstvalue = translate[ar[0]]
        lastvalue = translate[ar[l - 1]]
        sum_result = int(sum_result) + int(firstvalue + lastvalue)

    return sum_result


def solve(puzzle_data):
    data1 = parse_part1(puzzle_data)
    data2 = parse_part2(puzzle_data)
    solution1 = part1and2(data1)
    solution2 = part1and2(data2)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

