from os.path import dirname, join
from itertools import combinations 
from functools import reduce

content     = open(join(dirname(__file__), "./day9input.txt"), 'r').read()
lines       = content.split("\n")

numbers = list(map(int, lines))

sums = set()
n = len(numbers)

for i, x in enumerate(numbers):
    valid = x in sums or i < 25
    if not valid:
        break
    for j in range(n):
        sums.add(x + numbers[j])

print("Part 1", x)

def solve2(data,num):
    for k in range(2, 50):
        for i in range(0, len(data)-k):
            l = []
            for j in range(0, k):
                l.append(data[i+j])
            if sum(l) == num:
                return min(l)+max(l)


print("Part 2:", solve2(numbers, x))

