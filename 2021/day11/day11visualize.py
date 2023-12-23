from os.path import dirname, join
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



class Day11:
    neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    def __init__(self, filename):
        content = open(join(dirname(__file__), filename), "r").read()
        lines = content.split("\n")

        self.energylevels = [list(map(int, line)) for line in lines]
        self.rowlen = len(lines)
        self.collen = len(lines[0])
        self.totalflashes = 0
        self.stepcount = 0
        self.filecounter = 0
        self.maxvalue = 0
        self.visualize_and_save()

    def is_out(self, x: int, y: int) -> bool:
        return not (0 <= x < self.rowlen and 0 <= y < self.collen)

    def add1all(self) -> list:
        self.energylevels = [[x + 1 for x in y] for y in self.energylevels]

    def add1adjacent(self, x: int, y: int) -> list:
        coords = []
        for dx, dy in self.neighbours:
            if not self.is_out(x + dx, y + dy):
                self.energylevels[x + dx][y + dy] += 1
                if self.maxvalue < self.energylevels[x + dx][y + dy]:
                    self.maxvalue = self.energylevels[x + dx][y + dy]
                coords.append((x + dx, y + dy))
        #self.visualize_and_save()
        return coords

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

    def perform_step(self) -> int:
        self.stepcount += 1
        # First add 1 to everyone
        self.add1all()
        self.visualize_and_save()
        # prepare initial data for recursion
        hasflashed = []
        needsflashed = []
        for x in range(self.rowlen):
            for y in range(self.collen):
                if self.energylevels[x][y] > 9:
                    needsflashed.append((x, y))

        # call flash and let the crazy stuff happen
        self.flash(hasflashed, needsflashed)
        # count flashes and reset flashed entries to 0
        count = 0
        for x in range(self.rowlen):
            for y in range(self.collen):
                if self.energylevels[x][y] > 9:
                    count += 1
                    self.energylevels[x][y] = 0
        self.totalflashes += count

        self.visualize_and_save()
        # part 1
        if self.stepcount % 10 == 0:
            print(self.stepcount)
        if self.stepcount == 100:
             print("Part 1: ", self.totalflashes)
        # part 2
        if count == self.rowlen * self.collen:
            print("Everyone flashed at step: ", self.stepcount)
            return count


    def visualize_and_save(self):

        self.filecounter += 1

        if self.filecounter <= 356:
            return

        data = np.array(self.energylevels)
        values, positions = np.unique(data, return_inverse=True)
        positions = positions.reshape(data.shape)

        fig, ax = plt.subplots(figsize=(10, 10), rasterized=True)
        colors = sns.color_palette('tab20', 10)
        N = len(values)
        colors = sns.color_palette('tab20', 10)
        # or you can give your own list: colors = ['red', 'green', ....][:N]
        ax.set_aspect('equal', 'box')
        sns.heatmap(data=positions,
                    #cmap=sns.color_palette(colors, as_cmap=True),
                    #cmap="binary",
                    cmap=sns.dark_palette("#69d", reverse=True, as_cmap=True),
                    vmin=0,
                    vmax=10,
                    annot=data, fmt='.0f', annot_kws={'size': 15},
                    linewidths=0,
                    cbar=False,
                    cbar_kws={'ticks': 10}, ax=ax)



        plt.savefig('gif/' + str(self.filecounter).zfill(4) + '.png', dpi=50)
        plt.close()



#multiprocessing.freeze_support()
#num_proc = 12
#p = multiprocessing.Pool(num_proc)
plt.rcParams['backend'] = 'agg'
solveday11 = Day11("day11.txt")
while solveday11.perform_step() is None:
    pass

solveday11.visualize_and_save()
print("Max Value: ", solveday11.maxvalue)



