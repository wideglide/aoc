import sys


def find_fuel(v):
    return v // 3 - 2


def part1():
    s = 0
    with open('input') as f:
        data = list(map(int, f.readlines()))
        for d in data:
            s += find_fuel(d)
    print(s)


def part2():
    s = 0
    with open('input') as f:
        data = list(map(int, f.readlines()))
        for d in data:
            v = d
            r = find_fuel(v)
            while (r > 0):
                v = r
                s += r
                r = find_fuel(v)
    print(s)


part1()

part2()
