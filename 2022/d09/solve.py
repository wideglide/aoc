#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


def closer(x1, x2):
    if x1 > x2:
        x2 += 1
    elif x2 > x1:
        x2 -= 1
    return x1, x2


class bridge:
    def __init__(self, max_x=6, max_y=5, initial=(0, 0), num_knots=1):
        self.H = initial
        self.T = []
        self.tpos = set()
        self.hpos = set()
        self.max_x = max_x
        self.max_y = max_y
        for i in range(num_knots):
            self.T.append(initial)

    def update_max(self):
        x, y = self.H
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)

    def take_step(self, d):
        x, y = self.H
        if d == 'U':
            self.H = (x, y + 1)
        elif d == 'D':
            self.H = (x, y - 1)
        elif d == 'R':
            self.H = (x + 1, y)
        elif d == 'L':
            self.H = (x - 1, y)
        self.hpos.add(self.H)
        self.update_max()

    def move_tails(self, d):
        for i, tail in enumerate(self.T):
            self.move_tail(i, d)

    def move_tail(self, i, d):
        head = self.H if i == 0 else self.T[i - 1]
        hx, hy = head
        tx, ty = self.T[i]
        if abs(hx - tx) > 1:
            hx, tx = closer(hx, tx)
            if hy != ty:
                hy, ty = closer(hy, ty)
        elif abs(hy - ty) > 1:
            hy, ty = closer(hy, ty)
            if hx != tx:
                hx, tx = closer(hx, tx)
        self.T[i] = (tx, ty)
        if i == len(self.T) - 1:
            self.tpos.add(self.T[i])

    def move(self, d, n, verbose=False):
        if verbose:
            sys.stderr.write(f"\n == {d} {n} ==\n")
        for i in range(int(n)):
            self.take_step(d)
            self.move_tails(d)
            if verbose:
                self.show()
                sys.stderr.write("\n")

    def show(self):
        for y in range(self.max_y - 1, -1, -1):
            for x in range(self.max_x):
                if self.H == (x, y):
                    sys.stderr.write("H")
                elif self.T == (x, y):
                    sys.stderr.write("T")
                else:
                    sys.stderr.write(".")
            sys.stderr.write("\n")

    def final(self):
        sys.stderr.write("\n======\n")
        for y in range(self.max_y - 1, -1, -1):
            for x in range(self.max_x):
                if (x, y) in self.tpos:
                    sys.stderr.write("#")
                else:
                    sys.stderr.write(".")
            sys.stderr.write("\n")

    def part1(self):
        return len(self.tpos)


# part 1
data = list(open(input_file).read().strip().split('\n'))

pos = bridge()
for line in data:
    d, n = line.strip().split(' ')
    pos.move(d, n)
# pos.final()
print(f" part1 total = {pos.part1()}")


# part 2
pos = bridge(num_knots=9)
for line in data:
    d, n = line.strip().split(' ')
    pos.move(d, n)

print(f" part2  = {pos.part1()}")
