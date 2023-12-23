from os.path import dirname, join
import itertools 
from collections import Counter

content     = open(join(dirname(__file__), "./day10input.txt"), 'r').read()
lines       = content.split("\n")

numbers = [int(i) for i in lines]
numbers.sort()
# get the jolt number representing the device (final +3)
numbers.append(numbers[len(numbers)-1] + 3)
numbers.sort()

def joltProduct(inputnumbers) -> int:
    oneCounter      = 0
    threeCounter    = 0
    nums = sorted(inputnumbers)
    nums.append(0)
    nums.sort()

    for x in range(len(nums)-1):
        if nums[x+1] - nums[x] == 3:
            threeCounter+= 1
        elif nums[x+1] - nums[x] == 1:
            oneCounter+=1
        else:
            pass
    return oneCounter * threeCounter


def totalArrangement(inputnumbers) ->int:
    values = sorted(inputnumbers)
    cn = Counter()
    cn[0] = 1
    for number in values:
        cn[number] = cn[number - 1 ] + cn[number - 2 ] + cn[number - 3]
    
    return cn[values[-1]]


print("Part 1", joltProduct(numbers))
print("Part 2", totalArrangement(numbers))

