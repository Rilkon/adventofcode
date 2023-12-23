from os.path import dirname, join

current_dir = dirname(__file__)
file_path   = join(current_dir, "./day3input.txt")
f           = open(file_path, 'r')
content     = f.read()
lines       = content.split("\n")

moves  = [(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)]
m      = len(lines)
n      = len(lines[0])
result = 1

for dirx, diry in moves:
    count = 0
    x     = 0
    y     = 0
    
    while x < m:
        if (lines[x][y] == '#'): 
            count += 1
        x += dirx
        y += diry
        y %= n

    result *= count
    print(result)
