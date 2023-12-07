#!/usr/bin/env python3

from collections import Counter
from operator import itemgetter
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# Translation
TABLE = str.maketrans('TJQKA', 'abcde')


# part 1
data = list(open(input_file).read().strip().split('\n'))


def score_hand(h):
    c = Counter(h)
    max_kind = max(c.values())
    if max_kind == 5:
        return 50
    elif max_kind == 4:
        return 40
    elif len(c) == 2:
        # full house
        return 35
    elif max_kind == 3:
        # three of a kind
        return 30
    elif len(c) == 3:
        # two pair
        return 20
    elif max_kind == 2:
        # one pair
        return 10
    return 1


def load_cards(data, scoring_func):
    hands = list()
    for line in data:
        hand, bid = line.strip().split()
        bid = int(bid)
        value = scoring_func(hand)
        alt = hand.translate(TABLE)
        hands.append((hand, bid, value, alt))
    sorted_hands = sorted(hands, key=itemgetter(3), reverse=False)
    sorted_value = sorted(sorted_hands, key=itemgetter(2), reverse=False)

    total = 0
    for i, row in enumerate(sorted_value, start=1):
        value = i * row[1]
        total += value
        # print(i, value, row)
    return total


total = load_cards(data, score_hand)
print(f" part1 total = {total}")


# part 2

# Translation
TABLE = str.maketrans('TJQKA', 'a1cde')


def score_hand_p2(h):
    c = Counter(h)
    num_j = c.pop('J', 0)
    max_kind = max(c.values(), default=0)

    if max_kind + num_j == 5:
        # five of a kind
        return 50
    elif max_kind + num_j == 4:
        # four of a kind
        return 40
    elif len(c) == 2:
        # full house
        return 35
    elif max_kind + num_j == 3:
        # three of a kind
        return 30
    elif len(c) == 3:
        # two pair
        return 20
    elif max_kind + num_j == 2:
        # one pair
        return 10
    return 1


total = load_cards(data, score_hand_p2)
print(f" part2 total = {total}")
