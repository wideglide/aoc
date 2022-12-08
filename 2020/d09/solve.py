#!/usr/bin/env python3

from itertools import combinations
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n'))
d = list(map(int, d))


for i in range(25, len(d)):
    if d[i] not in list(map(sum, combinations(d[i-25: i], 2))):
        print(f"P1: no solution for {i} {d[i]}")
        val = d[i]
        break

print("val", val)
for i in range(len(d)):
    j = i+1
    s = d[i]
    while s < val and j < len(d):
        s += d[j]
        if s == val:
            v1 = min(d[i:j+1])
            v2 = max(d[i:j+1])
            print(f"P2: ({i}, {j}) sum = {v1 + v2}")
            break
        j += 1


