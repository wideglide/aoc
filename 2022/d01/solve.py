#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n\n'))

sums = [sum([int(x, 10) for x in elf.split('\n')]) for elf in d]
print(max(sums))

# part 2

top_3 = sorted(sums, reverse=True)[:3]
print(top_3)
print(sum(top_3))
