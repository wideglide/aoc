#!/usr/bin/env python3

from collections import Counter
import sys

data = list(map(int, open('input').read().strip()))


class bcolors:
    white = '\x1b[0m'
    whitebg = '\33[47m'
    end = '\033[0m'


def read_image(d, x, y):
    wblock = bcolors.whitebg + ' ' + bcolors.end
    im = [[2 for i in range(x)] for j in range(y)]
    i = 0
    while i < len(d):
        for k in range(y):
            for j in range(x):
                if im[k][j] == 2 and d[i] != 2:
                    im[k][j] = d[i]
                i += 1
    for j in range(y):
        for i in range(x):
            if im[j][i] == 1:
                sys.stdout.write(wblock)
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")
    sys.stdout.write("\n")


def count_pixels(data, x, y):
    layers = []
    c0min = 2**31
    for i in range(0, len(data), x * y):
        layer = Counter(data[i: i + x*y])
        c0 = layer[0]
        layers.append(layer)
        if c0 < c0min:
            c0min = c0
            cmul = layer[1] * layer[2]
            print(f"Layer {len(layers)} , c0={c0} c(1) * c(2) = {cmul}")


count_pixels(data, 25, 6)
read_image(data, 25, 6)
