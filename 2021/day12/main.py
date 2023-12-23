from os.path import dirname, join
import logging, sys


class Day12():

    def __init__(self, filename):
        # debug, info, warning, error, critical.
        logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        self.content = open(join(dirname(__file__), filename), "r").read()
        self.lines = self.content.split("\n")
        self.nodes = dict()

    def build_nodes(self):
        for line in self.lines:
            pair = line.split("-")
            logging.debug(pair)
            left = pair[0]
            right = pair[1]
            if left in self.nodes:
                self.nodes[left].append(right)
            else:
                self.nodes[left] = [right]
            if right in self.nodes:
                self.nodes[right].append(left)
            else:
                self.nodes[right] = [left]

        logging.debug(self.nodes)

    def process_node(self, current="start", visited=[], part2=False, specialcave=None):
        paths = []
        visited.append(current)

        for node in self.nodes[current]:
            if node == "end":
                paths.append(["end"])
            elif node == "start":
                # part 2, make sure start is not visited twice
                pass
            elif node.isupper():
                paths = paths + self.process_node(node, visited.copy(), part2, specialcave)
            else:
                if node not in visited:
                    paths = paths + self.process_node(node, visited.copy(), part2, specialcave)
                else:
                    if specialcave is None and part2:
                        paths = paths + self.process_node(node, visited.copy(), part2, node)
        allpaths = []
        for path in paths:
            allpaths.append([current] + path)
        return allpaths


def main():
    filename = "day12.txt"
    day12 = Day12(filename)
    day12.build_nodes()

    paths1 = day12.process_node()
    logging.debug(f"Paths: {paths1}")

    paths2 = day12.process_node(part2=True)
    logging.debug(f"Paths: {paths1}")

    print(f"Part1: {len(paths1)}")
    print(f"Part2: {len(paths2)}")


if __name__ == "__main__":
    main()
