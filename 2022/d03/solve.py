#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n'))

values = list()
for line in d:
    length = len(line) // 2
    s1, s2 = map(set, (line[:length], line[length:]))
    common = list(s1.intersection(s2))[0]
    v = ord(common) - ord('a') + 1 if common > 'Z' else ord(common) - ord('A') + 27
    values.append(v)
print(f" part1 = {sum(values)}")


# part 2
values = list()
for i in range(0, len(d), 3):
    s1 = set(d[i])
    s2 = set(d[i+1])
    s3 = set(d[i+2])
    common = list(set.intersection(s1, s2, s3))[0]
    v = ord(common) - ord('a') + 1 if common > 'Z' else ord(common) - ord('A') + 27
    values.append(v)
print(f" part2 = {sum(values)}")
