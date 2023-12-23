from os.path import dirname, join
import itertools 

content     = open(join(dirname(__file__), "./day11input.txt"), 'r').read()
grid       = content.split("\n")

def countNeighbors(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            for d in range(1, min(len(grid), len(grid[0]))):
                nr = r + d*i
                nc = c + d*j
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    break
                if grid[nr][nc] == '#':
                    count += 1
                if grid[nr][nc] != '.':
                    break
    return count

iter = 0
while True:
    tempgrid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    change = False
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '.':
                continue
            n = countNeighbors(grid, r, c)
            if grid[r][c] == 'L' and n == 0:
                change = True
                tempgrid[r][c] = '#'
            elif grid[r][c] == '#' and n >= 5:
                change = True
                tempgrid[r][c] = 'L'
    iter += 1
    if not change:
        break
    grid = [[tempgrid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]

occ = sum(map(lambda x: x.count('#'), grid))
print("Part 2", occ)