#!/usr/bin/env python3

import math
import sys

fd = 'input'
if len(sys.argv) == 2:
    fd = sys.argv[1]

data = [line.strip() for line in open(fd).readlines()]

m = {}
for j, l in enumerate(data):
    for i, p in enumerate(l):
        if p == '#':
            m[(i, j)] = set()
print(f" - num asteroids = {len(m)}")


def get_delta(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return ((x2-x1), (y1-y2))


def get_distance(pt1, pt2):
    return math.hypot(*get_delta(pt1, pt2))


def get_angle(pt1, pt2):
    r = math.atan2(*get_delta(pt1, pt2))
    return math.degrees(r) % 360


def get_vector(pt1, pt2):
    d = get_distance(pt1, pt2)
    a = get_angle(pt1, pt2)
    return (a, d)


for k in m.keys():
    for a in m.keys():
        if a == k:
            continue
        m[k].add(get_angle(k, a))

print(" part 1 ==============")
max_vis = max(len(v) for v in m.values())
print("max visible = {}".format(max_vis))

print(" part 2 ==============")
for k, v in m.items():
    if len(v) == max_vis:
        laser = k
m200 = sorted(m[laser])[199]
print(f"laser at {laser}, 200th @ {m200}")
for k, v in m.items():
    if m200 == get_angle(laser, k):
        print("200th {}  (x*100+y)= {}, distance={:0.2f}, angle={:0.2f}".format(k, k[0]*100+k[1], get_distance(laser, k), m200)) # noqa
