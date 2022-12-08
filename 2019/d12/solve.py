#!/usr/bin/env python3

import sys
from itertools import combinations

# <x=3, y=2, z=-6>
# <x=-13, y=18, z=10>
# <x=-8, y=-1, z=13>
# <x=5, y=10, z=4>


class moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.init = (x, y, z)

    def grav(s, o):
        if (s.x > o.x):
            s.vx -= 1
            o.vx += 1
        if (s.y > o.y):
            s.vy -= 1
            o.vy += 1
        if (s.z > o.z):
            s.vz -= 1
            o.vz += 1
        if (s.x < o.x):
            s.vx += 1
            o.vx -= 1
        if (s.y < o.y):
            s.vy += 1
            o.vy -= 1
        if (s.z < o.z):
            s.vz += 1
            o.vz -= 1

    def vel(s):
        s.x += s.vx
        s.y += s.vy
        s.z += s.vz

    def home(s):
        return s.init == (s.x, s.y, s.z)

    def pe(s):
        return sum((abs(s.x), abs(s.y), abs(s.z)))

    def ke(s):
        return sum((abs(s.vx), abs(s.vy), abs(s.vz)))

    def te(s):
        return s.pe() * s.ke()

    def show(s):
        print(f" ({s.x:3}, {s.y:3}, {s.z:3})  vel=({s.vx:3}, {s.vy:3}, {s.vz:3})")  # noqa


def operate(moons, n):
    for t in range(n):
        for m1, m2 in combinations(range(4), 2):
            moons[m1].grav(moons[m2])
        for m in range(4):
            moons[m].vel()
    print(f"time ({t+1}): ")
    for m in range(4):
        moons[m].show()
    print("total energy = {}".format(sum(m.te() for m in moons)))


def simulate(moons):
    t = 0
    while True:
        if t > 0 and all(m.home() for m in moons):
            break
        for m1, m2 in combinations(range(4), 2):
            moons[m1].grav(moons[m2])
        for m in range(4):
            moons[m].vel()
        t += 1
    print(f"time ({t+1}): ")
    for m in range(4):
        moons[m].show()
    print("total energy = {}".format(sum(m.te() for m in moons)))


def example():
    moons = [moon(x=-1, y=0, z=2),
             moon(x=2, y=-10, z=-7),
             moon(x=4, y=-8, z=8),
             moon(x=3, y=5, z=-1)]
    simulate(moons)


def example2():
    moons = [moon(x=-8, y=-10, z=0),
             moon(x=5, y=5, z=10),
             moon(x=2, y=-7, z=3),
             moon(x=9, y=-8, z=-3)]
    simulate(moons)


def part1():
    operate([moon(x=3, y=2, z=-6),
             moon(x=-13, y=18, z=10),
             moon(x=-8, y=-1, z=13),
             moon(x=5, y=10, z=4)], 1000)


sys.stdout.write("example :: ")
example()
print()

sys.stdout.write("example :: ")
example2()
print()

sys.stdout.write("part 1 :: ")
# part1()
