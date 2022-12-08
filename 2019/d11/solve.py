#!/usr/bin/env python3

import threading
import queue
import sys

mem = list(map(int, open('input').read().split(',')))
# mem = list(map(int, "1002,4,3,4,33,99".split(',')))
# mem = list(map(int, "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(',')))  # noqa
# mem = list(map(int, "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(',')))  # noqa
# d09test01 = list(map(int, "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(',')))  # noqa


class bcolors:
    white = '\x1b[0m'
    whitebg = '\33[47m'
    end = '\033[0m'


class ampThread(threading.Thread):
    def __init__(self, amp, program, in_q=None, out_q=None):
        threading.Thread.__init__(self)
        self.name = amp
        self.iq = queue.Queue() if in_q is None else in_q
        self.oq = queue.Queue() if out_q is None else out_q
        self.d = program.copy()
        self.d.extend([0 for i in range(1000)])

    def get_v(self, p):
        try:
            addr = self.d[self.i+p]
            if self.m[p] == 1:
                return addr
            if self.m[p] == 2:
                return self.d[addr+self.rb]
            return self.d[addr]
        except IndexError:
            print(f"IndexError: p={p}, m={self.m[p]}, rb={self.rb}, o={self.o}")  # noqa
            sys.exit(1)

    def set_v(self, p, v):
        addr = self.d[self.i+p]
        if self.m[p] == 1:
            self.d[self.i+p] = v
        elif self.m[p] == 2:
            self.d[addr+self.rb] = v
        else:
            self.d[addr] = v

    def fetch(self):
        v = self.d[self.i]
        self.o = v % 100
        self.m = [(v // di) % 10 for di in [10**5, 100, 1000, 10000]]

    def run(z):
        z.i = 0
        z.rb = 0
        z.fetch()

        while (z.o != 99):
            v1 = z.get_v(1)
            if z.o == 1:
                r = v1 + z.get_v(2)
                z.set_v(3, r)
                z.i += 4
            elif z.o == 2:
                r = v1 * z.get_v(2)
                z.set_v(3, r)
                z.i += 4
            elif z.o == 3:
                z.set_v(1, z.iq.get())
                z.i += 2
            elif z.o == 4:
                z.oq.put(v1)
                z.i += 2
            elif z.o == 5:
                if v1 != 0:
                    z.i = z.get_v(2)
                else:
                    z.i += 3
            elif z.o == 6:
                if v1 == 0:
                    z.i = z.get_v(2)
                else:
                    z.i += 3
            elif z.o == 7:
                r = 1 if v1 < z.get_v(2) else 0
                z.set_v(3, r)
                z.i += 4
            elif z.o == 8:
                r = 1 if v1 == z.get_v(2) else 0
                z.set_v(3, r)
                z.i += 4
            elif z.o == 9:
                z.rb += v1
                z.i += 2
            else:
                print(f"[-] Invalid opcode: {z.o} aborting")
                sys.exit(1)
            z.fetch()
        z.oq.put(99)
        return


def new_pos(x, y, d, v):
    nd = "NWSE"
    if v == 0:
        d = nd[(nd.index(d) - 1) % 4]
    elif v == 1:
        d = nd[(nd.index(d) + 1) % 4]

    if d == 'N':
        y -= 1
    if d == 'W':
        x += 1
    if d == 'S':
        y += 1
    elif d == 'E':
        x -= 1
    return x, y, d


def write_msg(pnl, x, y):
    wblock = bcolors.whitebg + ' ' + bcolors.end
    print()
    minx = min(i for j in range(y) for i in range(x) if pnl[j][i] == 1)
    maxx = max(i for j in range(y) for i in range(x) if pnl[j][i] == 1)
    for j in range(y):
        if all(v == 0 for v in pnl[j]):
            continue
        line = []
        for i in range(minx, maxx):
            if pnl[j][i] == 1:
                line.append(wblock)
            else:
                line.append(" ")
        print(''.join(line))
    print()


def runProgram(name, code, _input=[]):
    N = 400
    F = 'N'
    P = [[0 for i in range(N)] for j in range(N)]
    x = y = N // 2
    P[y][x] = _input[0]
    painted = set()
    th = ampThread(name, code)
    th.start()
    while True:
        v = P[y][x]
        th.iq.put(v)
        nc = th.oq.get()
        if nc == 99:
            break
        P[y][x] = nc
        painted.add((x, y))
        tr = th.oq.get()
        x, y, F = new_pos(x, y, F, tr)
    th.join()
    write_msg(P, N, N)
    print(f"  # painted = {len(painted)}")


print("[*] part 1 =========== ")
runProgram('A', mem, [0])
print("[*] part 2 =========== ")
runProgram('B', mem, [1])
