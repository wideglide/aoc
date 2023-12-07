#!/usr/bin/env python3

import math
import sys


input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

races = [
    (40, 233),
    (82, 1011),
    (84, 1110),
    (92, 1487)
    ]

sample = [
    (7, 9),
    (15, 40),
    (30, 200)
    ]

sample_single = [
    (71530, 940200)
    ]

single = [
    (40828492, 233101111101487)
    ]


def comp_dist(t, limit):
    return t * (limit - t)


def part1(races):
    ways = []
    for time, dist in races:
        wins = []
        for i in range(time + 1):
            out = comp_dist(i, time)
            if out > dist:
                wins.append(i)
        ways.append(len(wins))
    return math.prod(ways)


# part 1
data = list(open(input_file).read().strip().split('\n'))

print(part1(sample))

total = part1(races)
print(f" part1 total = {total}")


# part 2
print(part1(sample_single))

total = part1(single)
print(f" part2 total = {total}")
