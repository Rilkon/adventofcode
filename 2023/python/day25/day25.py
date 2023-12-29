import sys
import pathlib
import math
import networkx as nwx
import scipy


def parse(parsedata):

    allcomponents = set()
    connections = {}

    for line in parsedata.splitlines():
        left, right = line.split(": ")

        allcomponents.add(left)
        right = set(right.split(" "))
        connections[left] = right

    return connections


def part1(data):
    g = nwx.Graph()

    for node, edges in data.items():
        g.add_node(node)
        for edge in edges:
            g.add_node(edge)
            g.add_edge(node, edge)

    cut = nwx.minimum_edge_cut(g)
    g.remove_edges_from(cut)
    components = nwx.connected_components(g)

    return math.prod([len(c) for c in components])

def solve(puzzle_data):
    data = parse(puzzle_data)
    solution1 = part1(data)
    return solution1, ""


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
