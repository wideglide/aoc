#!/usr/bin/env python3

from itertools import permutations

mem = list(map(int, open('input').read().split(',')))
# mem = list(map(int, "1002,4,3,4,33,99".split(',')))
# mem = list(map(int, "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(',')))  # noqa


def get_modes(v):
    s = str(v)
    o = int(s[-2:])
    m = [0x00001 & int(v / d) for d in [10000, 100, 1000, 10000]]
    return (o, m)


def get_v(d, p, m):
    if m == 1:
        return p
    return d[p]


def set_v(d, p, m, i, v):
    if m == 1:
        d[i] = v
    else:
        d[p] = v


def operate(a):
    d = mem.copy()
    i = 0
    o, m = get_modes(d[i])
    ai = 0

    while (o != 99):
        p1 = d[i+1]
        v1 = get_v(d, p1, m[1])
        if o == 1:
            p2 = d[i+2]
            p3 = d[i+3]
            r = v1 + get_v(d, p2, m[2])
            set_v(d, p3, m[3], i+3, r)
            i += 4
        if o == 2:
            p2 = d[i+2]
            p3 = d[i+3]
            r = v1 * get_v(d, p2, m[2])
            set_v(d, p3, m[3], i+3, r)
            i += 4
        if o == 3:
            set_v(d, p1, m[1], i+1, a[ai])
            i += 2
            ai += 1
        if o == 4:
            return v1
            i += 2
        if o == 5:
            p2 = d[i+2]
            if v1 != 0:
                i = get_v(d, p2, m[2])
            else:
                i += 3
        if o == 6:
            p2 = d[i+2]
            if v1 == 0:
                i = get_v(d, p2, m[2])
            else:
                i += 3
        if o == 7:
            p2 = d[i+2]
            p3 = d[i+3]
            r = 1 if v1 < get_v(d, p2, m[2]) else 0
            set_v(d, p3, m[3], i+3, r)
            i += 4
        if o == 8:
            p2 = d[i+2]
            p3 = d[i+3]
            r = 1 if v1 == get_v(d, p2, m[2]) else 0
            set_v(d, p3, m[3], i+3, r)
            i += 4
        o, m = get_modes(d[i])
    return


print("[*] part 1 =========== ")
results = {}
phase = [0, 1, 2, 3, 4]
for c in permutations(phase, 5):
    r = 0
    for i in range(0, 5):
        r = operate((c[i], r))
    results[r] = phase
print(max(results.keys()))
print("[*] part 2 =========== ")
phase = [5, 6, 7, 8, 9]
