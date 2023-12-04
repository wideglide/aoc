#!/usr/bin/env python3

import math
import sys
from collections import defaultdict

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


# part 1
data = list(open(input_file).read().strip().split('\n'))


def find_star(data, xs, xe, ys, ye):
    for y in range(ys, ye + 1):
        for x in range(xs, xe + 1):
            if data[y][x] == '*':
                return (x, y)


def check_num(data, x, y, size, mlocs=None):
    if size == 0:
        return False
    width = len(data[0])
    height = len(data)
    adj = []
    xs = max(x - 1, 0)
    xe = min(x + size, width - 1)
    ys = max(y - 1, 0)
    ye = min(y + 1, height)
    if y > 0:
        adj.extend(data[y - 1][xs:xe + 1])
    if y < height - 1:
        adj.extend(data[y + 1][xs:xe + 1])
    if x > 0:
        adj.append(data[y][xs])
    if x + size < width:
        adj.append(data[y][xe])
    res = not all([x == '.' for x in adj])
    if adj.count("*") > 0:
        loc = find_star(data, xs, xe, ys, ye)
        mlocs[loc].append(int(data[y][x:x + size]))
    return res


def read_table(data):
    values = []
    mlocs = defaultdict(list)
    size = 0
    startx = 0
    starty = 0
    for y, line in enumerate(data):
        row = line.replace(",", " ")
        for x, c in enumerate(row):
            if c.isdigit():
                if size == 0:
                    startx = x
                    starty = y
                    size = 1
                else:
                    size += 1
            else:
                res = check_num(data, startx, starty, size, mlocs)
                if res:
                    values.append(int(row[startx: startx + size]))
                size = 0
        res = check_num(data, startx, starty, size, mlocs)
        if res:
            values.append(int(row[startx: startx + size]))
        size = 0
    return mlocs, sum(values)


def sum_locs(mlocs):
    total = 0
    for loc, values in mlocs.items():
        if len(values) == 2:
            total += math.prod(values)
        elif len(values) > 2:
            pass
    return total


locations, total = read_table(data)
print(f" part1 total = {total}")

# part 2
total = sum_locs(locations)

print(f" part2  = {total}")
