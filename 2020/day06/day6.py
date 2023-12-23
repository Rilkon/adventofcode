from os.path import dirname, join

content     = open(join(dirname(__file__), "./day6input.txt"), 'r').read()
lines       = content.split("\n\n")

print("Part 1:", sum(len(a) for a in list(set.union       (*map(set, y))    for y in [x.split("\n") for x in lines])))
print("Part 2:", sum(len(a) for a in list(set.intersection(*map(set, y))    for y in [x.split("\n") for x in lines])))