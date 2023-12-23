from os.path import dirname, join


def part1(input: list) -> str:
    return str(sum(len(word) in (2, 3, 4, 7) for line in input for word in line))


def part2(left, right) -> str:
    result = 0
    for rownumber in range(len(left)):
        digits = {}
        for i in range(10):
            digits[i] = set("abcdefg")
        for config in sorted(left[rownumber], key=len):
            configset = set(config)
            match(len(configset)), len(configset.intersection(digits[4])), len(configset.intersection(digits[7])):
                # will be picked first because they are distinct
                # 1 = length 2 // 4 = length 4 // 7 = length 3 // 8 = length 7
                case (2, _, _):
                    digits[1] = configset
                case (3, _, _):
                    digits[7] = configset
                case (4, _, _):
                    digits[4] = configset
                case (7, _, _):
                    digits[8] = configset
                # arrange rest
                # digit 9 has length 6 and overlaps with digit 4 and digit 7
                case (6, 4, 3):
                    digits[9] = configset
                # digit 0 has length 6 and overlaps with digit 7
                case (6, _, 3):
                    digits[0] = configset
                # digit 3 has length 5 and overlaps with digit 7
                case (5, _, 3):
                    digits[3] = configset
                # digit 5 has length 5 and overlaps with digit 4
                case (5, 3, _):
                    digits[5] = configset
                # remaing length 5 has to be digit 2
                case (5, _, _):
                    digits[2] = configset
                # remaining length 6 has to be digit 6
                case (6, _, _):
                    digits[6] = configset

        resultdigits = []
        for outputdigits in right[rownumber]:
            for item in digits.items():
                if set(outputdigits) == set(item[1]):
                    resultdigits.append(str(item[0]))
        result += int("".join(resultdigits))

    return str(result)


if __name__ == "__main__":
    content = open(join(dirname(__file__), "day8input.txt"), "r").read()
    lines = content.split("\n")
    left_side, rightside = [], []
    for line in lines:
        left_side.append(line.split(" | ", 1)[0].split(" "))
        rightside.append(line.split(" | ", 1)[1].split(" "))

    print("Part 1: ", part1(rightside))
    print("Part 2: ", part2(left_side, rightside))




