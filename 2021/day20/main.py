import os
from time import perf_counter as pc


def pixel_to_bin(pixel) -> str:
    if pixel == ".":
        return "0"
    if pixel == "#":
        return "1"


class ImageEnhancer:

    def __init__(self, data, count):
        algorithm = data[0]
        self.image = data[2:]
        self.bordersize = count
        self.pixelsquare = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.algodict = {idx: value for (idx, value) in enumerate(algorithm)}
        self.imagearray = [x for x in [line for line in self.image]]

    def put_image_in_border(self, localimage, ):
        """build a nice fancy border of emptiness around our input
        where bordersize == the number of iterations for part 1 // part 2"""

        # total column loength has to be the collength of our image + borders on top and bottom
        targetcollength = len(localimage) + self.bordersize * 2

        # whole row of empty dots for top and bottom
        whole_empty_dot_row = ''.join('.' for _ in range(targetcollength))

        # bordersize-length string of dots to append to rows beginning and end to add "columns of dots"
        borderdots = ''.join('.' for _ in range(self.bordersize))

        newlist = []
        # upper boarder
        [newlist.append(whole_empty_dot_row) for x in range(self.bordersize)]

        # "column borders" with actual data in between
        [newlist.append(borderdots + row + borderdots) for row in localimage]

        # bottom boarder
        [newlist.append(whole_empty_dot_row) for x in range(self.bordersize)]

        return newlist

    def get_output_pixel(self, pixelcoords, image, count) -> str:
        enhancekey = ""
        x, y = pixelcoords
        for dx, dy in self.pixelsquare:
            """When neighbour is inside, concatenate our dictionary key by using those neighbours"""
            if 0 <= x + dx < len(image[0]) and 0 <= y + dy < len(image):
                tempkey = pixel_to_bin(image[x + dx][y + dy])
            else:
                """When a neighbour is outside we have to concatenate 0 for even and 1 for odd iteration counts
                 because of trolling from AoC creator giving us a # for the first rule in the image enhancer sequnce
                 and thereby alternating between # and . for the outside grid """
                if count % 2 == 0:
                    tempkey = 0
                else:
                    tempkey = 1

            enhancekey += str(tempkey)
        """once we built our key we transform it from bin to dec and access our dictionary with it """
        return str(self.algodict[int(enhancekey, 2)])

    def solve(self):

        borderedimage = self.put_image_in_border(self.image)
        for i in range(self.bordersize):
            savedimage = borderedimage.copy()
            for x in range(len(borderedimage[0])):
                for y in range(len(borderedimage)):
                    """Fuck, strings are immutable. Don't want to rebuild my whole data structure
                    so we do this 'beautiful' stuff below to change our pixels"""
                    currentrow = borderedimage[x]
                    templist = list(currentrow)
                    templist[y] = self.get_output_pixel((x, y), savedimage, i)
                    borderedimage[x] = ''.join(templist)

        return sum(row.count('#') for row in borderedimage)


def main():
    time1 = pc()
    filename = "day20.txt"

    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        data = f.read().split("\n")

    part1 = ImageEnhancer(data, 2)
    part2 = ImageEnhancer(data, 50)

    print("Part 1: ", part1.solve())
    print("Part 1: ", part2.solve())
    print("Execution Time: ", pc() - time1)


if __name__ == "__main__":
    main()
