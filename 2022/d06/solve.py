#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


# part 1
data = open(input_file).read().strip()
for i in range(3, len(data)):
    if len(set(data[i-4:i])) == 4:
        print(f" part1, characters received = {i}, {data[i-4:i]}")
        break

# part 2
for i in range(13, len(data)):
    if len(set(data[i-14:i])) == 14:
        print(f" part2, characters received = {i}, {data[i-14:i]}")
        break

# print(f" part2 = {top}")
