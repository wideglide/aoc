#!/usr/bin/env python3

from itertools import combinations
from collections import Counter
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n'))
d = list(map(int, d))
d.sort()
print(d[:10])

c = Counter()
c[1] += 1
for i in range(1, len(d)):
    pre = d[i - 1]
    cur = d[i]
    dif = cur - pre
    if cur - pre <= 3:
        c[dif] += 1
    else:
        print(f"  Problem at index {i} ({cur} - {pre}) = {dif}")
c[3] += 1

print(c, c[1] * c[3])

m = max(d)
d.append(m + 3)
val = 1
for i in range(1, 5):
    cur = d[i]
    o = sum(d[j] - cur < 4 for j in range(i+1, i+4))
    print([d[j] - cur < 4 for j in range(i+1, i+4)], [d[j] for j in range(i+1, i+4)])
    print(o, d[i:i+3])
    val *= o
print(val)

