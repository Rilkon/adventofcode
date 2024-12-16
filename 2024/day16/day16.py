import pathlib
import sys
from collections import defaultdict
from copy import deepcopy
import networkx as nx

# 0, 1, 2, 3
# N, E, S, W
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def parse(parsedata):
    G = nx.DiGraph()
    start = (0, 0)
    end = (0, 0)

    for x, line in enumerate(parsedata.splitlines()):
        for y, value in enumerate(line):
            if value == "#":
                continue

            for direction in range(4):
                G.add_node(((x, y), direction))

            if value == "S":
                start = (x, y)
            elif value == "E":
                end = (x, y)

    for node, direction in G.nodes:
        new_pos = (node[0] + DIRS[direction][0], node[1] + DIRS[direction][1])
        if (new_pos, direction) in G.nodes:
            G.add_edge((node, direction), (new_pos, direction), weight=1)

        for new_dir in range(4):
            G.add_edge((node, direction), (node, new_dir), weight=1000)

    for direction in range(4):
        G.add_edge((end, direction), "end", weight=0)

    return G, start


def part1(data):
    graph, start = data
    return nx.shortest_path_length(graph, (start, 1), "end", weight="weight")


def part2(data):
    graph, start = data
    best_paths = nx.all_shortest_paths(graph, (start, 1), "end", weight="weight")
    return len(set(node[0] for p in best_paths for node in p if node != "end"))


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
