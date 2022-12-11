#!/usr/bin/env python3

from operator import mul
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


class cpu:
    def __init__(self):
        self.X = 1
        self.cycle = 0
        self.values = [1]
        self.out = ""

    def fetch(self, line):
        line = line.strip()
        if line[:4] == "noop":
            self.do_noop()
        if line[:4] == "addx":
            _, vstr = line.split(' ')
            val = int(vstr)
            self.do_addx(val)

    def draw(self):
        sprite = {self.X - 1, self.X, self.X + 1}
        if self.cycle % 40 == 0:
            sys.stderr.write("\n")
            self.out = "".join((self.out, "\n"))
        if self.cycle % 40 in sprite:
            sys.stderr.write("#")
            self.out = "".join((self.out, "#"))
        else:
            sys.stderr.write(" ")
            self.out = "".join((self.out, "."))
        self.cycle += 1

    def do_noop(self):
        self.values.append(self.X)
        self.draw()

    def do_addx(self, val):
        self.values.append(self.X)
        self.values.append(self.X)
        self.draw()
        self.draw()
        self.X += val


# part 1
data = list(open(input_file).read().strip().split('\n'))

CPU = cpu()

for i, line in enumerate(data):
    CPU.fetch(line)

interesting = [20, 60, 100, 140, 180, 220]

values = [v for i, v in enumerate(CPU.values) if i in interesting]
total = sum(map(mul, values, interesting))


sys.stderr.write("\n")
print(f" part1 total = {total}")


# part 2

# print(f" part2  = {MAX}")
