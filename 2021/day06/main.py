import time
from os.path import dirname, join


def solve(input: list, days: int) -> int:
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for element in input:
        fish[element] += 1

    for x in range(1, days + 1):
        old_fish = fish.copy()
        for i in range(0, 9):
            if i == 6:
                fish[6] = old_fish[0] + old_fish[7]
            elif i == 8:
                fish[8] = old_fish[0]
            else:
                fish[i] = old_fish[i+1]
        if x == 80:
            print("Part 1: ", sum(fish.values()))
    return sum(fish.values())


if __name__ == '__main__':
    timestart = time.time()
    content = open(join(dirname(__file__), "day6input.txt"), 'r').read()
    lines = list(map(int, content.split(",")))
    print("Part 2: ", solve(lines, 256))
    print("Time of Execution ", time.time() - timestart)
