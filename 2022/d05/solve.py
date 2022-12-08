#!/usr/bin/env python3

import re
import sys
from collections import defaultdict

RE_C = re.compile(r"move (\d+) from (\d+) to (\d+)")

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


def read_header(data):
    stacks = defaultdict(list)
    num_cols = (len(data[0]) + 1) // 4 + 1
    for line in data:
        if ' 1' in line:
            break
        for stk in range(1, num_cols):
            idx = (stk - 1) * 4 + 1
            if line[idx] != ' ':
                stacks[stk].append(line[idx])

    for stack in range(1, num_cols):
        stacks[stack].reverse()
    return stacks


def print_stacks(stacks):
    print("\n ================================ ")
    for stack in sorted(stacks):
        print(stack, stacks[stack])
    top = ""
    for stack in sorted(stacks):
        top += stacks[stack][-1]

    print(f" ========== TOP: {top:12} ========= ")


# part 1
data = list(open(input_file).read().split('\n'))
stacks = read_header(data)
print_stacks(stacks)

for line in data:
    match = RE_C.search(line)
    if match is None:
        continue
    num, src, dst = list(map(int, match.groups()))
    for i in range(num):
        v = stacks[src].pop()
        stacks[dst].append(v)

print_stacks(stacks)
# print(f" part1 = {top}")


# part 2
stacks = read_header(data)

for line in data:
    match = RE_C.search(line)
    if match is None:
        continue
    num, src, dst = list(map(int, match.groups()))
    stacks[dst].extend(stacks[src][-num:])
    for i in range(num):
        v = stacks[src].pop()

print_stacks(stacks)
# print(f" part2 = {top}")
