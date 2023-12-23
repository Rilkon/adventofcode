from os.path import dirname, join
import time


def get_wrong_closings(input: list):
    queue = []
    for letter in input:
        if letter in OPEN:
            queue.append(MAPPING[letter])
        elif letter in CLOSED:
            if not queue or letter != queue.pop():
                return letter


def solve(input: list):

    incomplete_lines = []
    wrong_brackets = []
    for line in input:
        temp = get_wrong_closings(line)
        if temp is not None:
            wrong_brackets.append(temp)
        else:
            incomplete_lines.append(line)
    print("Part 1: ", sum(SCORES[bracket] for bracket in wrong_brackets))

    all_queues = []
    for line in incomplete_lines:
        queue = []
        for letter in line:
            if letter in OPEN:
                queue.append(MAPPING[letter])
            elif letter in CLOSED:
                queue.pop()
        all_queues.append(list(reversed(queue)))

    print("Part 2: ", part2scoring(all_queues))


def part2scoring(input: list) -> str:

    new_scores = {")": 1,
                  "]": 2,
                  "}": 3,
                  ">": 4}
    scores = []
    for line in input:
        score = 0
        for element in line:
            score = (score * 5) + int(new_scores[element])
        scores.append(score)

    return str(sorted(scores)[len(scores) // 2])


if __name__ == "__main__":
    CLOSED = [")", "]", "}", ">"]
    OPEN = ["(", "[", "{", "<"]
    MAPPING = dict(zip(OPEN, CLOSED))
    SCORES = {")": 3,
              "]": 57,
              "}": 1197,
              ">": 25137}

    filename = "day10.txt"
    content = open(join(dirname(__file__), filename), "r").read()
    lines = content.split("\n")
    solve(lines)
