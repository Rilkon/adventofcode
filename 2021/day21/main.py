import os
from itertools import product, permutations
from time import perf_counter as pc

class DiracDice:

    def __init__(self, p1start, p2start, scorelimit):

        self.dice = 1000
        self.boardlength = 10
        self.p1position = p1start
        self.p2position = p2start
        self.p1score = 0
        self.p2score = 0
        self.dicerolls = 0
        self.scorelimit = scorelimit

    def __repr__(self):
        mystring = ' , '.join("%s: %s" % item for item in vars(self).items())
        return str(self.__class__.__name__) + " [" + mystring + " ]"

    def play(self):

        rounds = 1
        deterdice = 1
        while True:
            p1dicesum = 3 * deterdice + 3
            deterdice += 3
            p2dicesum = 3 * deterdice + 3
            deterdice += 3
            result = self.one_round(p1dicesum, p2dicesum)
            if result > 0:
                return result
            rounds += 1
            #print(self)




    def one_round(self, p1dicesum, p2dicesum):

        # p1
        self.dicerolls += 3
        self.p1position = self.get_new_position(self.p1position, p1dicesum)
        self.p1score += self.p1position
        if self.p1score >= self.scorelimit:
            return self.dicerolls * self.p2score

        # p2
        self.dicerolls += 3
        self.p2position = self.get_new_position(self.p2position, p2dicesum)
        self.p2score += self.p2position

        if self.p2score >= self.scorelimit:
            return self.dicerolls * self.p1score


        return 0


    def get_new_position(self, currentpos, dicesum):
        return  (currentpos + dicesum-1) % 10 + 1

    def multi_dimensional_dirac(self, pos1, pos2, score1=0, score2=0, cur_player=0, memo={}):

        if (pos1, pos2, score1, score2, cur_player) in memo:
            return memo[(pos1, pos2, score1, score2, cur_player)]

        wins = [0, 0]
        dice_sums = [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]

        for roll in dice_sums:
            cur_positions = [pos1, pos2]
            cur_scores = [score1, score2]

            cur_positions[cur_player] = (cur_positions[cur_player] + roll - 1) % 10 + 1
            cur_scores[cur_player] += cur_positions[cur_player]

            if cur_scores[cur_player] >= self.scorelimit:
                wins[cur_player] += 1
            else:
                win1, win2 = self.multi_dimensional_dirac(
                    cur_positions[0], cur_positions[1], cur_scores[0], cur_scores[1], not cur_player)

                wins[0] += win1
                wins[1] += win2

        memo[(pos1, pos2, score1, score2, cur_player)] = wins

        return wins

    def part2(self):
        return max(self.multi_dimensional_dirac(self.p1position, self.p2position))


def main():
    time1 = pc()

    part1 = DiracDice(6,2, 1000)
    part2 = DiracDice(6,2, 21)

    print("Part 1: ", part1.play())
    print("Part 2: ", part2.part2())
    print("Excution Time: ", pc() - time1)


if __name__ == "__main__":
    main()
