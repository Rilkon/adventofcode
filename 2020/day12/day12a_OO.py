
from os.path import dirname, join
import itertools 
import re


content     = open(join(dirname(__file__), "day12input.txt"), 'r').read()
input       = content.split("\n")

class Ship:
    def __init__(self, startingdirection = "E"):
        self.directionhelper    = {90: "E", 180: "S", 270: "W", 0: "N"} 
        self.inv_dir_helper     = {"E": 90, "S": 180, "W": 270, "N": 0}
        self.direction          = startingdirection
        self.directiondegree    = self.inv_dir_helper[startingdirection]
        self.position           = {"N": 0, "S": 0, "E": 0, "W": 0}

    def getManhattanDistance(self) -> int:
        
        return abs(int(self.position["N"]) - int(self.position["S"])) +  abs(int(self.position["W"]) - int(self.position["E"]))

    def setNewDirectionDegree(self, direction, degree):
        tempdegree = 0
        if direction == 'R':
            tempdegree = int(self.directiondegree) + int(degree)
        else:
            tempdegree = int(self.directiondegree) - int(degree)

        if tempdegree >= 360:
            tempdegree = tempdegree - 360
        elif tempdegree < 0:
            tempdegree = tempdegree + 360
        
        self.direction          = self.directionhelper[tempdegree]
        self.directiondegree    = tempdegree

    def __str__(self):
        returnstring = "Ferry Position: " + str(self.position)
        returnstring = returnstring + " | Direction: " + self.direction
        returnstring = returnstring + " | Manhattan Distane: " + str(self.getManhattanDistance())
        return returnstring

    def performInstruction(self, instruction):
        instructionset = re.split(r'(\d+)', instruction)
        
        if instructionset[0] == "F":
            # move ship in current direction
            self.position[self.direction] = int(self.position[self.direction]) + int(instructionset[1])
        elif instructionset[0] == "R" or instructionset[0] == "L":
            #change direction without moving
            self.setNewDirectionDegree(instructionset[0], instructionset[1])
        else:
            # move ship in direction without changing direction
            self.position[instructionset[0]] = int(self.position[instructionset[0]]) + int(instructionset[1])

myFerry = Ship("E")

for instruction in input:
    myFerry.performInstruction(instruction)

print(myFerry)
