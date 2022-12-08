#!/usr/bin/env python3

import math

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

# part 1
d = list(open('input').read().strip().split('\n'))

height = len(d)
width = len(d[0])
print(f"   puzzle is {width} wide and {height} high.")


def check_slope(xd, yd):
    def move(p):
        return Point(p.x+xd, p.y+yd)

    p = Point(0, 0)
    trees = 0

    while p.y < height:
        x1 = p.x % width
        if d[p.y][x1] == '#':
            trees += 1
        p = move(p)
    print(f"[*] for slope Right {xd}, down {yd} = {trees} trees")
    return trees

s = math.prod(check_slope(i,j) for i,j in [(1,1), (3,1), (5,1), (7,1), (1,2)])  # noqa

print(f"P2: product of all trees = {s}")
