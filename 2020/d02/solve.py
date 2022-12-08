#!/usr/bin/env python3

import re

from collections import Counter

# part 1
d = list(open('input').read().strip().split('\n'))

pattern = re.compile('([0-9]+)-([0-9]+) (\w+): (\w+)')

def check_password(l, part=1):
    m = pattern.search(l)
    c = Counter(m.group(4))
    low = int(m.group(1))
    hi = int(m.group(2))
    pol = m.group(3)
    passwd = m.group(4)
    if part == 1:
        if c[pol] < low or c[pol] > hi:
            return False
        return True
    if (passwd[low-1] == pol) != (passwd[hi-1] == pol):
        return True
    return False




print(sum(check_password(l) for l in d))

# part 2

print(sum(check_password(l, 2) for l in d))

