#!/usr/bin/env python3

mem = list(map(int, open('input').read().split(',')))
# mem = list(map(int, "1002,4,3,4,33,99".split(',')))
# mem = list(map(int, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(',')))  # noqa


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


def operate(a, b):
    d = mem.copy()
    i = 0
    o, m = get_modes(d[i])

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
            set_v(d, p1, m[1], i+1, a)
            i += 2
        if o == 4:
            print(f"    i={i} p1={p1}  value= {v1}")
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
operate(1, 1)
print("[*] part 2 =========== ")
operate(5, 1)
# operate(8, 1)
# operate(9, 1)
