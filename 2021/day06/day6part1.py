from os.path import dirname, join


def part1(input: list, days: int) -> list:


    for i in range(1, days+1):
        newfish = []

        for x in range(0, len(input)):

            if input[x] == 0:
                newfish.append(8)
                input[x] = 6
            else:
                input[x] = input[x] - 1

        input.extend(newfish)


    return input



content = open(join(dirname(__file__), "day6input.txt"), 'r').read()
lines = list(map(int, content.split(",")))

result1 = str(len(part1(lines.copy(), 80)))

print("Part 1: " + result1)

