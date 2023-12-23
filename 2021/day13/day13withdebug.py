from os.path import dirname, join
import logging, sys
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


class Day13():

    def __init__(self, filename):
        # debug, info, warning, error, critical.
        logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)
        self.content = open(join(dirname(__file__), filename), "r").read()
        self.lines = self.content.split("\n")
        logging.debug(self.lines)
        self.rowlen = 0
        self.collen = 0
        self.coords = []
        self.folds = []

    def parse_input(self):
        for line in self.lines:
            if line.count(",") > 0:
                y,x  = line.split(",")
                self.coords.append((int(x),int(y)))
                if int(x) > self.rowlen:
                    self.rowlen = int(x)
                if int(y) > self.collen:
                    self.collen = int(y)
            if line.count("fold along") > 0:
                left, right = line.split("=")
                self.folds.append((left[-1], right))
        self.rowlen += 1
        self.collen += 1

        logging.debug(f"self.folds {self.folds}")



        logging.debug(self.coords)
        logging.debug(f"self.rowlen {self.rowlen}")
        logging.debug(f"self.collen {self.collen}")

        self.matrix = np.zeros(shape=(self.rowlen, self.collen),dtype=int)
        logging.info(f"Matrix initialized {self.matrix}")


        for x,y in self.coords:
            self.matrix[x][y] = 1

        logging.debug(f"self.matrix after parsing {self.matrix}")

    def solve(self) -> int:
        count = 0
        for axis,index in self.folds:
            count += 1
            self.fold(axis,int(index))
            if count == 1:
                print(f"Part1: {np.sum(self.matrix)}")

        return np.sum(self.matrix)

    def visualize_part2(self):
        data = np.array(self.matrix)
        plt.imshow(data, cmap=sns.dark_palette("#69d", reverse=True, as_cmap=True), interpolation='nearest')
        plt.savefig("AoC2021_Day_13_Part2.png", dpi=100)
        plt.close()

    def fold(self, axis: str, index: int):

        if axis == "x":
            logging.debug(f"fold, {axis}{index}")
            self.collen = self.collen - index - 1
            newarray = self.matrix[:, :self.collen]

            logging.debug(f"newarray after fold + first step")
            logging.debug(newarray)

            fliparray = self.matrix[:,self.collen+1:len(self.matrix[0])]
            logging.debug(f"fliparray after being prepared for flip")
            logging.debug(fliparray)
            fliparray = np.fliplr(fliparray)
            logging.debug(f"fliparray after being flipped")
            logging.debug(fliparray)

        if axis == "y":

            logging.debug(f"fold, {axis}{index}")
            logging.debug(self.matrix)
            self.rowlen= self.rowlen - index - 1

            newarray = self.matrix[:self.rowlen, :]

            logging.debug(f"newarray after fold + first step")
            logging.debug(newarray)

            fliparray = self.matrix[self.rowlen+1:len(self.matrix),:]
            logging.debug(f"fliparray after being prepared for flip")
            logging.debug(fliparray)

            fliparray = np.flipud(fliparray)
            logging.debug(f"fliparray after being flipped")
            logging.debug(fliparray)

        self.matrix = np.clip(newarray + fliparray, a_min=0, a_max=1)
        logging.info(f"Matrix after fold {axis}={index}")
        logging.info(self.matrix)


filename = "day13.txt"
day13 = Day13(filename)
day13.parse_input()
day13.solve()
day13.visualize_part2()


