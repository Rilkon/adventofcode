from os.path import dirname, join
import re
import math
from functools import reduce
from typing import Tuple

content     = open(join(dirname(__file__), "day13input.txt"), 'r').read()
input       = content.split("\n")

earliest_depart = int(input[0])
buslines        = list(map(int, re.findall(r'\d+', input[1])))

busline, time = min([(bus, bus * math.ceil(earliest_depart / bus)) for bus in buslines], key=lambda tup: tup[1])
wait = time - earliest_depart

print("Part 1:", wait * busline)

# copied these two methods 1-1 from a python implementation of chinese remainder theorem
# Extended Euclid
def extended_euclid(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

# Uses ExtendedEuclid to find inverses
def chinese_remainder_theorem(n1: int, r1: int, n2: int, r2: int) -> int:
    (x, y) = extended_euclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m

# fill above methods with prepared data
def part2(buses):
    n = chinese_remainder_theorem(buses[0][0], buses[0][1], buses[1][0], buses[1][1])
    prod = buses[1][0] * buses[0][0]
    for i in range(2, len(buses)):
        n = chinese_remainder_theorem(buses[i][0], buses[i][1], prod, n)
        prod *= buses[i][0]
    return (prod - n) 

# bring the data into a format that it can be solved by above methods
buses = []
for x, i in enumerate(input[1].split(",")):
        if i != "x":
            buses.append((int(i), x))

print("Part 2:", part2(buses))