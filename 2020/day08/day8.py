from os.path import dirname, join

content     = open(join(dirname(__file__), "./day8input.txt"), 'r').read()
lines       = content.split("\n")

def get_the_number(line) -> int:
    for i in line.split():
        try:
            return int(i)
        except ValueError:
            pass

def calculate_acc(program) -> int:

    acc = 0
    visited = set()
    x = 0

    while(x < len(program)):
        if x in visited:
            break
        if program[x].startswith("acc"):
            acc+= get_the_number(program[x])
            visited.add(x)
            x+= 1
        elif program[x].startswith("jmp"):
            visited.add(x)
            x+= get_the_number(program[x])
        else:
            x+=1
    return acc

print("Part 1:", calculate_acc(lines))