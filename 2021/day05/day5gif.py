from os.path import dirname, join
import numpy as np
import matplotlib.pyplot as plt
import imageio



def build_initial_grid(size: int) -> list:

    return [[0 for x in range(size)] for y in range(size)]


def is_vertical(x1: int, y1: int, x2: int, y2: int) -> bool:

    if x1 != x2 and y1 != y2 and (max(x1, x2) - min(x1, x2)) == (max(y1, y2) - min(y1, y2)):
        return True
    else:
        return False


def get_step_value(a:int, b: int):
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0


def write_lines_to_matrix(input: list, size: int, part2: bool) -> list:

    matrix = build_initial_grid(size)
    gifcounter = 0
    for line in input:

        x1 = int(line.split(" -> ")[0].split(",")[0])
        y1 = int(line.split(" -> ")[0].split(",")[1])
        x2 = int(line.split(" -> ")[1].split(",")[0])
        y2 = int(line.split(" -> ")[1].split(",")[1])

        if is_vertical(x1, y1, x2, y2) and part2:
            matrix[x1][y1] += 1
            xstep = get_step_value(x1, x2)
            ystep = get_step_value(y1, y2)
            while x1 != x2 or y1 != y2:
                x1 += xstep
                y1 += ystep
                matrix[x1][y1] += 1

        elif x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                matrix[x1][i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                matrix[i][y1] += 1

        data = np.array(matrix)
        cmap = plt.get_cmap('magma', data.max())
        plt.imshow(data, cmap=cmap, interpolation='nearest')
        plt.gca().set_aspect('auto')
        plt.savefig('gif'+str(gifcounter)+'.png', dpi=200)
        gifcounter += 1



    return matrix

def part1(input: list, size: int) -> str:

    return str(sum([sum(x > 1 for x in row) for row in write_lines_to_matrix(input.copy(), size, False)]))


def part2(input: list, size: int) -> str:
    return str(sum([sum(x > 1 for x in row) for row in write_lines_to_matrix(input.copy(), size, True)]))



content = open(join(dirname(__file__), "day5input.txt"), 'r').read()
#content = open(join(dirname(__file__), "day5test.txt"), 'r').read()
lines = content.split("\n")
#print("Part 1: " + part1(lines.copy(), 1000))
print("Part 2: " + part2(lines.copy(), 1000))


# Build GIF
print('creating gif\n')
with imageio.get_writer('plot.gif', mode='I') as writer:
    for i in range(0, 499, 1):
        image = imageio.imread('gif'+str(i)+'.png')
        writer.append_data(image)
print('gif complete\n')

