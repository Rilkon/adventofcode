# What.. no file input today?!
day15input      = [2,0,1,7,4,14,18]
day15testinput  = [0, 3, 6]

def get_x_spoken_number(limit, input) -> int:
    
    spoken_numbers = dict()
    
    # starting set
    for x in range(0, len(input) - 1):
        start = input[x]
        spoken_numbers[start] = x
        last = input[-1]
    
    # continuation
    for y in range(len(input) -1, limit):
        cur = last
        
        if last in spoken_numbers:
            last = y - spoken_numbers[last]
        else:
            last = 0
        spoken_numbers[cur] = y
    #print(spoken_numbers)
    return cur

print("Part 1:", get_x_spoken_number(2020, day15input))
print("Part 2:", get_x_spoken_number(30000000, day15input))