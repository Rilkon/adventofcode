from os.path import dirname, join
import itertools 
import copy

content     = open(join(dirname(__file__), "./day11input.txt"), 'r').read()
#content     = open(join(dirname(__file__), "./day11test.txt"), 'r').read()
lines       = content.split("\n")

grid = list()

for line in lines:
    grid.append(list(line))

def getAllAdjacentSeats(x, y, suchraum) -> list:
    returnlist = list()
    neighbors = (-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)
    for pair in neighbors:
        try:
            if x + pair[0] >= 0 and y + pair[1] >= 0:
                returnlist.append(suchraum[x+pair[0]][y+pair[1]])
        except IndexError:
            continue

    return returnlist

def willBeOccupied(seats) -> bool:
    if "#" in seats:
        return False
    else:
        return True

def willBeEmpty(seats) -> bool:
    count = 0
    for value in seats:
        if value == "#":
            count+= 1
    
    if count >= 4: 
        return True 
    else:
        return False 

def getNewStateOfSeats(currentSeats) -> list:
    returnSeats = copy.deepcopy(currentSeats)

    for x in range(0, len(currentSeats)):
        for y in range(0, len(currentSeats[x])):
            #print(x, y)
            #print(currentSeats[x][y])
            if currentSeats[x][y] == "L" and willBeOccupied(getAllAdjacentSeats(x, y, currentSeats)) is True:
                returnSeats[x][y] = "#"

            if currentSeats[x][y] == "#" and willBeEmpty(getAllAdjacentSeats(x, y, currentSeats)) is True:
                returnSeats[x][y] = "L"

    return returnSeats

def countOccupiedSeats(currentSeats) -> int:
    count = 0
    for line in currentSeats:
        for seat in line:
            if seat == "#":
                count+= 1
    
    return count

newgrid = []
oldgrid = grid

loopcount = 0
while(True):

    print("Loopcount: ", loopcount)
    newgrid = getNewStateOfSeats(oldgrid)

    if newgrid == oldgrid:
        break

    oldgrid = newgrid
    loopcount+= 1


print(newgrid)
print(countOccupiedSeats(newgrid))




