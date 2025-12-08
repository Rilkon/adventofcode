import itertools
import math
import pathlib
import sys
from copy import deepcopy
import networkx as nx


def parse(parsedata):
    nodes = [tuple(map(int, line.split(","))) for line in parsedata.splitlines()]
    edges = sorted([(math.dist(box1, box2), box1, box2) for box1, box2 in itertools.combinations(nodes, 2)])

    G = nx.Graph()
    G.add_nodes_from(nodes)
    return G, edges

def part1(data):

    G, edges = data
    for i, (_, box1, box2) in enumerate(edges):
        G.add_edge(box1, box2)
        if i == 1000:
            return math.prod(sorted(list(map(len, nx.connected_components(G))), reverse=True)[:3])

def part2(data):

    G, edges = data
    for _, box1, box2 in edges:
        G.add_edge(box1, box2)
        if nx.is_connected(G):
            return box1[0] * box2[0]

def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(deepcopy(data))
    solution2 = part2(data)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))