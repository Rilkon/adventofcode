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


def compare_cards(card1, card2):
    if cardvalues[card1] == cardvalues[card2]:
        return 0
    elif cardvalues[card1] > cardvalues[card2]:
        return 1
    else:
        return -1


def compare_hands(hand1, hand2):
    if handvalues[hand1] == handvalues[hand2]:
        return 0
    elif handvalues[hand1] > handvalues[hand2]:
        return 1
    else:
        return -1


class CamelCardHand():

    def __init__(self, cards, bid, ispart2=False):
        self.cards = cards
        self.cardlist = list(cards)
        self.bid = int(bid)
        self.hand = ""
        c = Counter(self.cardlist)
        match max(c.values()):
            case 5:
                self.hand = "fivekind"
            case 4:
                self.hand = "fourkind"
            case 3:
                if c.most_common(2)[-1][1] == 2:
                    self.hand = "fullhouse"
                else:
                    self.hand = "threekind"
            case 2:
                if c.most_common(2)[-1][1] == 2:
                    self.hand = "twopair"
                else:
                    self.hand = "onepair"
            case _:
                self.hand = "highcard"

        # hacky part 2
        if ispart2:
            cardvalues["J"] = 1
            if 'J' in c:
                match self.hand:
                    case "highcard":
                        self.hand = "onepair"
                    case "onepair":
                        self.hand = "threekind"
                    case "twopair":
                        if c['J'] == 1:
                            self.hand = "fullhouse"
                        elif c['J'] == 2:
                            self.hand = "fourkind"
                    case "threekind":
                        self.hand = "fourkind"
                    case "fullhouse":
                        self.hand = "fivekind"
                    case "fourkind":
                        self.hand = "fivekind"

    def __lt__(self, other):
        handresult = compare_hands(self.hand, other.hand)
        if handresult < 0:
            return True
        elif handresult > 0:
            return False

        for i in range(0, len(self.cardlist)):
            currentself = self.cardlist[i]
            currentother = other.cardlist[i]

            cardresult = compare_cards(currentself, currentother)
            if cardresult < 0:
                return True
            elif cardresult > 0:
                return False

        return False

    def __str__(self):
        return f"|| Cards: {self.cards}, Bid: {self.bid}, Hand: {self.hand}"

    def __repr__(self):
        return self.__str__()


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
