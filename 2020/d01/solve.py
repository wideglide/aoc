#!/usr/bin/env python3

from itertools import combinations

# part 1
d = list(map(int, open('input').read().strip().split('\n')))
e = list()

for (i, j) in combinations(d, 2):
    if i + j == 2020:
        print(f" P1(c): {i} + {j} = 2020; {i} * {j} = {i * j}")

for (i, j, k) in combinations(d, 3):
    if i + j + k == 2020:
        print(f" P2(c): {i} + {j} = 2020; {i} * {j} = {i * j * k}")


for i in d:
    for j in d:
        if i + j == 2020:
            print(f" {i} + {j} = 2020; {i} * {j} = {i * j}")
        if (i + j) < 2020:
            e.append((i, j))
for i in d:
    for j in e:
        if i + sum(j) == 2020:
            print(f"P2 {j[0]} * {j[1]} * {i} = {j[0] * j[1] * i}")
