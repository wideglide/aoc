#!/usr/bin/env python3

from collections import defaultdict
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n'))

rules = defaultdict(set)
rules2 = defaultdict(set)
counts = defaultdict(int)

for line in d:
    line = line.replace(' bags', '').replace(' bag', '').replace('.', '')
    outer, inner = line.split(' contain ')
    if 'no other' in inner:
        continue
    for bag in inner.split(','):
        b_num, b_color = bag.strip().split(' ', 1)
        rules[b_color].add(outer.strip())
        counts[outer] += int(b_num)
        rules2[outer].add((int(b_num), b_color))


part1 = set()


def check_bag(color, d=0):
    if color not in rules.keys():
        return

    for c in rules[color]:
        check_bag(c, d+1)
        part1.add(c)


check_bag('shiny gold')

print(f"P1 = {len(part1)}")


def check_contents(color, d=0):
    if d > 18:
        return 0
    if color not in rules2.keys():
        return 1

    total = 0
    for tup in rules2[color]:
        num, c = tup
        sub = check_contents(c, d + 1)
        total += num * sub
    return total + 1


print(" ===   PART 2    ==== ")
part2 = check_contents('shiny gold') - 1
print(f"P2 = {part2}")
