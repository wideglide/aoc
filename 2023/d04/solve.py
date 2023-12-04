#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


def load_cards(data):
    cards = {idx: 1 for idx in range(1, len(data) + 1)}
    values = []
    for idx, line in enumerate(data):
        card_num, all_numbers = line.strip().split(":")
        card_id = int(card_num.split()[1])
        winning, mine = all_numbers.strip().split("|")
        winning = winning.strip().split()
        mine = mine.strip().split()
        matches = sum([x in winning for x in mine])
        if matches > 0:
            values.append(2**(matches - 1))
            num_cards = cards[card_id]
            for i in range(card_id + 1, card_id + 1 + matches):
                cards[i] += 1 * num_cards
    return sum(values), sum(cards.values())


# part 1
data = list(open(input_file).read().strip().split('\n'))

total_p1, total_p2 = load_cards(data)
print(f" part1 total = {total_p1}")


# part 2

print(f" part2  = {total_p2}")
