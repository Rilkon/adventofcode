import pathlib
import sys
from collections import Counter

cardvalues = {"2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "T": 10,
              "J": 11,
              "Q": 12,
              "K": 13,
              "A": 14}

handvalues = {"fivekind": 100,
              "fourkind": 75,
              "fullhouse": 50,
              "threekind": 25,
              "twopair": 10,
              "onepair": 5,
              "highcard": 1}


class CamelCardHand():

    def __init__(self, cards, bid, ispart2=False):
        self.cardlist = list(cards)
        self.bid = int(bid)
        self.hand = ""
        c = Counter(self.cardlist)

        if ispart2:
            cardvalues["J"] = 1

        max_count = max(c.values())
        second_most = c.most_common(2)[-1][1]
        if max_count == 5:
            self.hand = "fivekind"
        elif max_count == 4:
            self.hand = "fourkind" if not ispart2 or c["J"] == 0 else "fivekind"
        elif max_count == 3:
            if second_most == 2:
                self.hand = "fullhouse" if not ispart2 or c["J"] == 0 else "fivekind"
            else:
                self.hand = "threekind" if not ispart2 or c["J"] == 0 else "fourkind"
        elif max_count == 2:
            if second_most == 2:
                self.hand = "twopair" if not ispart2 or c["J"] != 1 else "fullhouse"
                self.hand = "fourkind" if ispart2 and c["J"] == 2 else self.hand
            else:
                self.hand = "onepair" if not ispart2 or c["J"] == 0 else "threekind"
        else:
            self.hand = "highcard" if not ispart2 or c["J"] == 0 else "onepair"

    def __lt__(self, other):
        handresult = handvalues[self.hand] - handvalues[other.hand]
        if handresult < 0:
            return True
        elif handresult > 0:
            return False

        for i in range(0, len(self.cardlist)):
            cardresult = cardvalues[self.cardlist[i]] - cardvalues[other.cardlist[i]]
            if cardresult < 0:
                return True
            elif cardresult > 0:
                return False

        return False


def parse(parsedata, ispart2=False):
    deck = []
    for line in parsedata.splitlines():
        cards, bid = line.split(" ")
        deck.append(CamelCardHand(cards, bid, ispart2))
    return deck


def part1(data):
    return sum([(i + 1) * camelhand.bid for i, camelhand in enumerate(sorted(data))])


def part2(data):
    return sum([(i + 1) * camelhand.bid for i, camelhand in enumerate(sorted(data))])


def solve(puzzle_data):
    data1 = parse(puzzle_data)
    solution1 = part1(data1)
    data2 = parse(puzzle_data, True)
    solution2 = part2(data2)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
