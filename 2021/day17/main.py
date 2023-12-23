import os
from math import floor, sqrt
from time import perf_counter as pc
import re


def is_in_target(a, b, x1, x2, y1, y2):
    if x1 <= a <= x2 and y1 <= b <= y2:
        return True
    else:
        return False


class Probe:

    def __init__(self, startvel_x, startvel_y, target):
        self.target = target
        self.stepcount = 0
        self.startvel_x = startvel_x
        self.startvel_y = startvel_y
        self.x = 0
        self.y = 0
        self.cur_vel_x = startvel_x
        self.cur_vel_y = startvel_y
        self.max_y = 0
        self.was_hit = False
        self.step_hit = 999999

    def __repr__(self):
        mystring = ' , '.join("%s: %s" % item for item in vars(self).items())
        return str(self.__class__.__name__) + " [" + mystring + " ]"

    def already_missed(self):
        targetx1, targetx2, targety1, targety2 = self.target
        if self.y < targety1:
            return True
        return False

    def hit_target(self):
        if is_in_target(self.x, self.y, *self.target):
            return True
        return False

    def perform_step(self):
        self.stepcount += 1
        # mark if it was in the target zone at any point

        # change x and y pos based on respective velocity
        self.x += self.cur_vel_x
        self.y += self.cur_vel_y

        # adjust drag
        if self.cur_vel_x > 0:
            self.cur_vel_x -= 1
        if self.x < 0:
            self.cur_vel_x += 1
        # adjust gravity
        self.cur_vel_y -= 1

        # save maximum
        if self.y >= self.max_y:
            self.max_y = self.y

        # mark if it was in the target zone at any point
        if self.hit_target():
            self.was_hit = True
            self.step_hit = self.stepcount
            return True
        else:
            # if it already missed (and hasn't hit before) - leave
            if self.stepcount > 0 and self.already_missed():
                return True

        return False


def solve():
    filename = "day17.txt"

    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        data = f.read()

    target = [int(s) for s in re.findall(r'-?\d+?\d*', data)]
    x1, x2, y1, y2 = target
    probecount = 0
    saved_max = -99999

    for x in range(x2+50):
        for y in range(y1, abs(y1)):
            probe = Probe(x, y, target)

            for stepcount in range(300):
                if probe.perform_step():
                    break

            if probe.was_hit:
                if probe.max_y > saved_max:
                    saved_max = probe.max_y
                probecount += 1

    print("Part 1: ", saved_max)
    print("Part 2: ", probecount)


def main():
    time1 = pc()
    solve()
    print("Excution Time: ", pc() - time1)


if __name__ == "__main__":
    main()
