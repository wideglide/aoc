#!/usr/bin/env python3

import threading
import time
import os
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
    red = '\x1b[31m'
    blue = '\x1b[34m'
    green = '\x1b[32m'
    greenbg = '\x1b[42m'
    end = '\033[0m'


class ampThread(threading.Thread):
    def __init__(self, amp, program, in_q=None, out_q=None):
        threading.Thread.__init__(self)
        self.name = amp
        self.iq = queue.Queue() if in_q is None else in_q
        self.oq = queue.Queue() if out_q is None else out_q
        self.d = program.copy()
        self.d.extend([0 for i in range(1000)])
        self.d[0] = 2  # 2 quarters to play for free

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


def write_msg(pnl, x, y):
    time.sleep(0.1)
    wblock = bcolors.whitebg + ' ' + bcolors.end
    wball = bcolors.red + 'O' + bcolors.end
    wpaddle = bcolors.greenbg + '_' + bcolors.end
    wdest = bcolors.green + 'X' + bcolors.end
    print("\33[2J")
    os.system('clear')
    for j in range(y):
        line = []
        for i in range(x):
            if pnl[j][i] == 2:
                line.append(wblock)
            elif pnl[j][i] == 4:
                line.append(wball)
            elif pnl[j][i] == 3:
                line.append(wpaddle)
            elif pnl[j][i] == 5:
                line.append(wdest)
                pnl[j][i] = 0
            else:
                line.append(" ")
        print(''.join(line))
    print()


class Pong:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.dest = 20

    def new(s, x, y):
        if x != s.x:
            s.vx = 1 if x > s.x else -1
        if y != s.y:
            s.vy = 1 if y < s.y else -1
        if s.vy == -1:
            s.dest = x + s.vx * (22 - y)
        else:
            s.dest = x + s.vx
        s.x = x
        s.y = y

    def p(self):
        return (self.x, self.vy, self.y)


def runProgram(name, code, _input=[]):
    def movePaddle(t, p, b):
        if t.iq.qsize() > 0:
            return
        if p.x < b.dest:
            t.iq.put(1)
        elif p.x > b.dest:
            t.iq.put(-1)
        else:
            t.iq.put(0)

    N = 80
    P = [[0 for i in range(N)] for j in range(N)]
    x = y = N // 2
    blk_tiles = set()
    tiles = set()
    ball = Pong(x, y)
    pd = Pong(x, y)
    score = 0
    th = ampThread(name, code)
    th.start()
    while True:
        x = th.oq.get()
        if x == 99:
            break
        y = th.oq.get()
        v = th.oq.get()
        P[y][x] = v
        if x == -1 and y == 0:
            score = v
        if v == 4:
            ball.new(x, y)
            P[24][ball.dest] = 5
            # write_msg(P, 34, 25)
            # sys.stdout.write(f"\r\r current score: {score}  Q{th.iq.qsize()}") # noqa
            movePaddle(th, pd, ball)
        if v == 3:
            pd.new(x, y)
            # write_msg(P, 34, 25)
            # sys.stdout.write(f"\r\r current score: {score}  Q{th.iq.qsize()}") # noqa
        if v == 2:
            blk_tiles.add((x, y))
        if v == 0 and (x, y) in blk_tiles:
            blk_tiles.remove((x, y))
        tiles.add((x, y))
        P[24][ball.dest % 34] = 5
    th.join()
    mx = max(t[0] for t in tiles)
    my = max(t[1] for t in tiles)
    print(f"\n  board = {mx} x {my} ball=({ball.p()}) paddle=({pd.p()})")
    print(f"  # blk_tiles = {len(blk_tiles)}")
    print(f"  final score = {score}")


print("[*] part 1 =========== ")
runProgram('A', mem, [0])
print("[*] part 2 =========== ")
# runProgram('B', mem, [1])
