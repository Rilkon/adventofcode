from os.path import dirname, join
import logging, sys
from time import perf_counter as pc
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


def is_out(matrix, x: int, y: int) -> bool:
    return not (0 <= x < len(matrix) and 0 <= y < len(matrix))


def expandgrid(grid, amount):
    newgrid = []
    for x in range(amount):
        temp = []
        for y in range(amount):
            temp.append((grid + x + y - 1) % 9 + 1)
        newgrid.append(temp)
    return np.block(newgrid)


class Day15:

    def __init__(self, filename):
        # debug, info, warning, error, critical.
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        # read file
        self.content = open(join(dirname(__file__), filename), "r").read()
        self.neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.weightmatrix = np.array([[int(x) for x in list(row)] for row in self.content.splitlines()])
        logging.debug(f"{self.weightmatrix=}")
        self.mlen = len(self.weightmatrix)
        self.nx_graph = nx.grid_2d_graph

    def set_weightmatrix(self, newmatrix):
        self.weightmatrix = newmatrix
        self.mlen = len(newmatrix)

    def build_nx_graph(self):
        self.nx_graph = nx.grid_2d_graph(self.mlen, self.mlen, create_using=nx.DiGraph)
        for x in range(self.mlen):
            for y in range(self.mlen):
                for dx, dy in self.neighbours:
                    if not is_out(self.weightmatrix, x + dx, y + dy):
                        self.nx_graph.add_edge((x + dx, y + dy), (x, y), weight=self.weightmatrix[x][y])
        logging.debug(f"{self.nx_graph=}")

    def draw_graph(self):
        G = self.nx_graph
        # This seems to be the layout most gridlike
        plt.figure(1, figsize=(14, 14), dpi=180)
        pos = nx.spectral_layout(G)
        options = {
            #'node_color': 'blue',
            'node_size': 300,
            'width': 2,
            'arrowstyle': '-|>',
            'arrowsize': 8,
            'font_size': 8,
            'font_weight': "bold"
        }

        nx.draw(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        nx.draw_networkx_labels(G, pos, font_size=6, font_family='sans-serif', font_weight='bold')
        plt.show()



    def part1(self):
        self.build_nx_graph()
        # Only uncomment for small datasets
        #self.draw_graph()
        return nx.shortest_path_length(self.nx_graph, source=(0, 0),
                                       target=(self.mlen - 1, self.mlen - 1), weight="weight")

    def part2(self):
        self.set_weightmatrix(expandgrid(self.weightmatrix, 5))
        self.build_nx_graph()
        # graph is too much even for test of part2
        #self.draw_graph()
        return nx.shortest_path_length(self.nx_graph, source=(0, 0),
                                       target=(self.mlen - 1, self.mlen - 1), weight="weight")


def main():
    filename = "day15.txt"
    day15 = Day15(filename)
    time1 = pc()
    print(f"Part 1: ", day15.part1())
    print(f"Part 2: ", day15.part2())
    print("Execution Time: ", (pc() - time1) * 1000, "ms")


if __name__ == "__main__":
    main()
