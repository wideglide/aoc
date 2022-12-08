#!/usr/bin/env python3

from collections import Counter
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n\n'))

total = 0

for group in d:
    people = group.split()
    c = Counter(''.join(people))
    total += len(c)
total = sum(len(set(group)) for group in d)

print(f"[*] P1: total = {total}")

total = 0
for i, group in enumerate(d):
    people = group.split()
    c = Counter(''.join(people))
    n_people = len(people)
    total += sum(n_people == v for k, v in c.items())

print(f"[*] P1: total = {total}")
