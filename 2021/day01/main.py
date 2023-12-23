from os.path import dirname, join


def part1(input: list) -> int:
    count = 0
    for i in range(0, len(input) - 1):
        if int(input[i + 1]) > int(input[i]):
            count += 1
    return count


def part2(input: list) -> int:
    myList = []
    for i in range(0, len(input) - 2):
        myList.append(int(input[i]) + int(input[i + 1]) + int(input[i + 2]))
    return part1(myList)


if __name__ == '__main__':
    content = open(join(dirname(__file__), "day1input.txt"), 'r').read()
    lines = content.split("\n")
    print("Day 1 Part 1: " + str(part1(lines)))
    print("Day 1 Part 2: " + str(part2(lines)))
