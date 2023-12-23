from os.path import dirname, join

content     = open(join(dirname(__file__), "./day7input.txt"), 'r').read()
#content     = open(join(dirname(__file__), "./day7test.txt"), 'r').read()
#content     = open(join(dirname(__file__), "./day7btest.txt"), 'r').read()
lines       = content.split("\n")

ruleset = [line.strip().split(" ") for line in lines]
rules = {}

colors = []

def find_path(start, end, graph, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_path(node, end, graph, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

for line in ruleset:
    color = line[0] + " " + line[1]
    rules[color] = []
    i = 5
    while i < len(line)-1:
        if "no" in line:
            i += 4
            continue
        for x in range(int(line[i-1])):
            rules[color].append(line[i] + " " + line[i+1]) 
        i += 4
count = 0

for color in rules.keys():
    for path in find_path("shiny gold", color, rules):
        count+= 1

print("Part 2:", count - 1)









