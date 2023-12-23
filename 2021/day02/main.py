from os.path import dirname, join
import time


def part1(input: list) -> list:
    myPosition = [0, 0]
    for instructions in input:
        instruction = instructions.split(" ")
        direction = instruction[0]
        value = int(instruction[1])

        if direction == "forward":
            myPosition[0] += value
        elif direction == "down":
            myPosition[1] += value
        elif direction == "up":
            myPosition[1] -= value
        else:
            print("well fuck")
            return []
    return myPosition

def part2(input: list) -> list:
    myPosition = [0, 0, 0]

    for instructions in input:
        instruction = instructions.split(" ")
        direction = instruction[0]
        value = int(instruction[1])

        if direction == "forward":
            myPosition[0] += value
            myPosition[1] = myPosition[1] + (value * myPosition[2])
        elif direction == "down":
            myPosition[2] += value
        elif direction == "up":
            myPosition[2] -= value
        else:
            print("well fuck")
            return []

    return myPosition

if __name__ == '__main__':
    start_time = time.time()
    content = open(join(dirname(__file__), "day2input.txt"), 'r').read()
    #content = open(join(dirname(__file__), "day7test.txt"), 'r').read()
    lines = content.split("\n")

    result = part1(lines)
    print("Day 2 Part 1: " + str(result[0] * result[1]))
    result = part2(lines)
    print("Day 2 Part 2: " + str(result[0] * result[1]))
    print("--- %s seconds ---" % (time.time() - start_time))