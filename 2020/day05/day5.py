from os.path import dirname, join

current_dir = dirname(__file__)
file_path   = join(current_dir, "./day5input.txt")
#file_path   = join(current_dir, "./day5test.txt")
f           = open(file_path, 'r')
content     = f.read()
lines       = content.split("\n")

def bin_search(line):
    # 2^7 = 128 // 2^3 = 8 for first 7 and last 3 letters
    numbers = list(range(2 ** len(line)))
    for letter in line:
        # R and B for upper // L and F for lower
        if letter in ["F", "L"]:
            numbers = numbers[: len(numbers) // 2]
        else:
            numbers = numbers[len(numbers) // 2 :]
    return numbers[0]
    
# part 1
print("Part 1:", max(bin_search(line[:7]) * 8 + bin_search(line[7:10]) for line in lines))

# part 2
ids = set(bin_search(line[:7]) * 8 + bin_search(line[7:10]) for line in lines)
print("Part 2:", list(ids.symmetric_difference(set(range(min(ids), max(ids)))))[0])

