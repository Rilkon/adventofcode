from os.path import dirname, join


class Day11:
    neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    def __init__(self, filename):
        content = open(join(dirname(__file__), filename), "r").read()
        lines = content.split("\n")

        self.energylevels = [list(map(int, line)) for line in lines]
        self.rowlen = len(lines)
        self.collen = len(lines[0])
        self.totalflashes = 0

    def is_out(self, x: int, y: int) -> bool:
        return not (0 <= x < self.rowlen and 0 <= y < self.collen)


    def add1all(self) -> list:
        self.energylevels = [[x + 1 for x in y] for y in self.energylevels]


    def add1adjacent(self, x: int, y: int) -> list:
        coords = []
        for dx, dy in self.neighbours:
            if not self.is_out(x + dx, y + dy):
                self.energylevels[x + dx][y + dy] += 1
                coords.append((x+dx, y+dy))

        return coords


    def printasgrid(self):
        for line in self.energylevels:
            print(line)
        print("")

    def tests(self):

        self.printasgrid()
        self.add1all()
        self.printasgrid()
        self.add1adjacent(1, 1)
        self.printasgrid()


    def flash(self, hasflashed, needsflash):
        if len(needsflash) == 0:
            return
        for coords in needsflash:
            needsflash.remove(coords)
            if self.energylevels[coords[0]][coords[1]] > 9:
                if coords not in hasflashed:
                    newcoords = self.add1adjacent(coords[0], coords[1])
                    hasflashed.append((coords[0], coords[1]))
                    for i, j in newcoords:
                        needsflash.append((i, j))

        return self.flash(hasflashed, needsflash)

    def perform_step(self):

        self.add1all()
        hasflashed = []
        needsflashed = []
        # prepare initial data for recursion
        for x in range(self.rowlen):
            for y in range(self.collen):
                if self.energylevels[x][y] > 9:
                    needsflashed.append((x, y))

        # call flash and let the crazy stuff happen
        self.flash(hasflashed, needsflashed)

        count = 0
        for x in range(self.rowlen):
            for y in range(self.collen):
                if self.energylevels[x][y] > 9:
                    count += 1
                    self.energylevels[x][y] = 0
        self.totalflashes += count





if __name__ == "__main__":

    solveday11 = Day11("day11.txt")
    # solveday11 = Day11("reallysmalltest.txt")

    for _ in range(100):
        solveday11.perform_step()

    print("Part 1: ", solveday11.totalflashes)
