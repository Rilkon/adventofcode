from itertools import batched
import pathlib
import sys
from copy import deepcopy
import re


def parse(parsedata):
    match = re.findall(r"\d+", parsedata)
    a, b, c, *instructions = map(int, match)
    return a, b, c, instructions


class ChronospacialComputer:
    def __init__(self, a, b, c, instructions):
        self.a = a
        self.b = b
        self.c = c
        self.instructions = instructions
        self.ip = 0
        self.result = ""
        self.commandset = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz,
                           4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}

    def combo(self, op):
        match op:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                return op

    def adv(self, op):
        self.a = self.a >> self.combo(op)

    def bdv(self, op):
        self.b = self.a >> self.combo(op)

    def cdv(self, op):
        self.c = self.a >> self.combo(op)

    def bxc(self, op):
        self.b = self.b ^ self.c

    def bxl(self, op):
        self.b = self.b ^ op

    def bst(self, op):
        self.b = self.combo(op) % 8

    def out(self, op):
        self.result += str(self.combo(op) % 8) + ","

    def jnz(self, op):
        if self.a != 0:
            self.ip = op - 2

    def run(self):
        while self.ip < len(self.instructions):
            for opcode, op in batched(self.instructions, 2):
                command = getattr(self, self.commandset[opcode].__name__)
                command(op)
                self.ip += 2

        return self.result


def part1(data):
    computer = ChronospacialComputer(*data)
    return computer.run()


def part2(data):
    return ""


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
