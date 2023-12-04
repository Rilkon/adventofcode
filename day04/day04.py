import pathlib
import sys

import regex as re


def parse(parsedata):
    cards = []
    for line in parsedata.splitlines():
        splitstring = line.split(": ")
        card = re.findall(r"\d+", splitstring[0])[0]
        splitnums = splitstring[1].split("|")
        win_nums = {int(x) for x in re.findall(r"\d+", splitnums[0])}
        you_nums = {int(x) for x in re.findall(r"\d+", splitnums[1])}

        matches = you_nums.intersection(win_nums)
        cards.append([card, win_nums, you_nums, matches, len(matches)])

    return cards


def part1(data):
    points = 0
    for card in data:
        if card[3]:
            points += 2 ** (card[4] - 1)

    return points


def part2(data):
    card_count = [1] * len(data)
    for i, card in enumerate(data):
        for j in range(1, card[4] + 1):
            card_count[i + j] += card_count[i]

    return sum(card_count)


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
