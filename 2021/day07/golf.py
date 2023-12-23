import statistics
lines = list(map(int, open("day7input.txt").read().split(",")))
print("Part 1: " + str(sum([abs(x - statistics.median(lines)) for x in lines])))
print("Part 2: " + str(min([sum([abs(x-i) * (abs(x-i)+1)/2 for x in lines]) for i in range(0, max(lines) + 1)])))

