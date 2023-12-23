from os.path import dirname, join
import logging, sys
from collections import Counter
from time import perf_counter as pc


class Day14:

    def __init__(self, filename):
        # debug, info, warning, error, critical.
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        # read file
        self.content = open(join(dirname(__file__), filename), "r").read()
        self.lines = self.content.split("\n")
        # initialize polymer
        self.polymer = self.lines[0]
        self.mapping = {}
        logging.debug(f"{self.polymer=}")
        # build mapping
        for line in self.lines[2:]:
            left, right = line.split(" -> ")
            self.mapping[left] = right

        logging.debug(f"{self.mapping=}")


    def solve(self):
        # counter over whole polymer
        c = Counter(self.polymer)
        # build initial counter for possible pairs from polymer
        temp = []
        for i in range(len(self.polymer) - 1):
            temp.append(self.polymer[i:i + 2])
        logging.debug(f"{temp=}")
        paircounter = Counter(temp)
        logging.debug(f"{paircounter=}")

        for i in range(40):
            # save old counter for summation
            old = paircounter
            paircounter = Counter()
            for key, add in self.mapping.items():
                # get first and second letter from key (= pair) and to be added character as add
                x = key[0]
                y = key[1]
                # Update paircounter
                paircounter[x + add] += old[x + y]
                paircounter[add + y] += old[x + y]
                # Update total counter
                c[add] += old[x + y]

            if i == 9:
                # Part1
                result = (c.most_common()[0][1]) - (c.most_common()[-1][1])
                print(f"Part1: {result}")

            logging.debug(f"{c=}")

        # Part 2
        result = (c.most_common()[0][1]) - (c.most_common()[-1][1])
        print(f"Part2: {result}")


def main():
    filename = "day14.txt"
    day14 = Day14(filename)
    time1 = pc()
    day14.solve()
    print("Execution Time: ", (pc() - time1)*1000, "ms")

if __name__ == "__main__":
    main()
