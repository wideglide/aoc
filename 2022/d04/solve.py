#!/usr/bin/env python3

import re
import sys

RE_C = re.compile(r"(\d+)\-(\d+),(\d+)\-(\d+)")

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
data = list(open(input_file).read().strip().split('\n'))
overlap = 0
for pair in data:
    p1, p2 = pair.split(',')
    a, b = list(map(int, p1.split('-')))
    c, d = list(map(int, p2.split('-')))
    if (a >= c and b <= d) or (c >= a and d <= b):
        overlap += 1

print(f" part1 = {overlap}")

overlap = 0
for pair in data:
    a, b, c, d = list(map(int, RE_C.search(pair).groups()))
    if (a >= c and b <= d) or (c >= a and d <= b):
        overlap += 1

print(f" part1 = {overlap}")

# part 2
overlap = 0
ranges = []
for pair in data:
    a, b, c, d = list(map(int, RE_C.search(pair).groups()))
    ranges.extend([b-a, d-c])
    if (a >= c and a <= d) or (b >= c and b <= d) or \
       (c >= a and c <= b) or (d >= a and d <= b):
        overlap += 1

print(f" part2 = {overlap}")
print(f"   MAX range {max(ranges)}")
