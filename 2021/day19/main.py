import math
from copy import deepcopy
from itertools import combinations

import numpy as np


def rotations():
    """Generate all possible rotation functions"""
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)
                yield lambda x: np.matmul(x, np.array([vi, vj, vk]))


def fit(inputscanners, hashes, i, j, v):
    """Find the correct rotation/translation to make the j'th scanner map fit the i'th"""
    s1, s2 = inputscanners[i], inputscanners[j]
    for rot in rotations():
        s2t = rot(s2)
        p = hashes[i][v][0]
        for q in hashes[j][v]:
            diff = s1[p, :] - s2t[q, :]
            if len((b := set(map(tuple, s2t + diff))) & set(map(tuple, s1))) >= 12:
                return diff, b, rot


def map_hash(coords):
    """
    Generate a hashset of sorted absolute coordinate differences
    between pairs of points
    """
    s = {
        tuple(sorted(map(abs, coords[i, :] - coords[j, :]))): (i, j)
        for i, j in combinations(range(len(coords)), 2)
    }
    return s


def match(hashes):
    """Figure out which pairs of scanner aps have sufficient overlap"""
    for i, j in combinations(range(len(hashes)), 2):
        if len(m := set(hashes[i]) & set(hashes[j])) >= math.comb(12, 2):
            yield i, j, next(iter(m))


def solve(inputscanners):
    """Given a list of scanner maps, return list of positions and set of beacons"""
    inputscanners = deepcopy(inputscanners)
    mypositions = {0: (0, 0, 0)}
    hashes = list(map(map_hash, inputscanners))
    mybeacons = set(map(tuple, inputscanners[0]))
    while len(mypositions) < len(inputscanners):
        for i, j, v in match(hashes):
            if not (i in mypositions) ^ (j in mypositions):
                continue
            elif j in mypositions:
                i, j = j, i
            mypositions[j], new_beacons, rot = fit(inputscanners, hashes, i, j, v)
            inputscanners[j] = rot(inputscanners[j]) + mypositions[j]
            mybeacons |= new_beacons
    return [mypositions[i] for i in range(len(inputscanners))], mybeacons


data = open("day19.txt").read()
scanners = data.split("\n\n")
scanners = [x.split("---\n")[-1].split("\n") for x in scanners]
scanners = [np.array([list(map(int, y.split(","))) for y in x]) for x in scanners]
positions, beacons = solve(scanners)
print(len(beacons))
print(max(np.abs(x - y).sum() for x, y in combinations(positions, 2)))
