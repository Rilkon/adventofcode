from os.path import dirname, join
import re

content     = open(join(dirname(__file__), "./day14input.txt"), 'r').read()
#content     = open(join(dirname(__file__), "./day14test.txt"), 'r').read()
lines       = content.split("\n")

def parse_mask(mask, b):
    return sum(1 << 35-i for i, c in enumerate(mask) if c == b)

memory = dict()
for line in lines:
    if line.startswith("mask"):
        mask  = line.split()[-1]
        mask0 = parse_mask(mask, "0")
        mask1 = parse_mask(mask, "1")
    else:
        address, value  = map(int, re.findall(r"\d+", line))
        memory[address] = value & ~mask0 | mask1

print(sum(memory.values()))