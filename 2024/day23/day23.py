import pathlib
import sys
from copy import deepcopy
import networkx as nx


def parse(parsedata):
    return nx.Graph([line.split("-") for line in parsedata.splitlines()])


def part1(g):
    cliques = nx.enumerate_all_cliques(g)
    return len([x for x in cliques if len(x) == 3 and any(node.startswith("t") for node in x)])


def part2(g):
    cliques = nx.find_cliques(g)
    return ",".join(sorted(max(cliques, key=len)))


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
