import sys

mem = list(map(int, open('input.txt').read().split(',')))


def operate(a, b):
    d = mem.copy()
    i = 0
    o = d[i]
    d[1] = a
    d[2] = b

    while (o != 99):
        o = d[i]
        p1 = d[i+1]
        p2 = d[i+2]
        p3 = d[i+3]
        if o == 1:
            r = d[p1] + d[p2]
            d[p3] = r
        if o == 2:
            r = d[p1] * d[p2]
            d[p3] = r
        i += 4
    return d[0]


print("part 1 == {} ".format(operate(12, 1)))
match = 19690720

for i in range(100, 0, -1):
    for j in range(100, 0, -1):
        if (operate(i, j) == match):
            print("[*] part 2 100 * {} + {} = {} ".format(i, j, 100*i+j))
            sys.exit(0)
