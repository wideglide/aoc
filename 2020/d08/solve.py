#!/usr/bin/env python3

from collections import defaultdict
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n'))
d.append('exit 0')

jmps = set()
nops = set()


def run(alter=None):
    visited = set()
    pc = 0
    reg = 0
    while pc not in visited:
        ins, val = d[pc].split()
        val = int(val)
        visited.add(pc)
        if pc == alter:
            ins = {'nop': 'jmp', 'jmp': 'nop'}[ins]
        if ins == 'jmp':
            jmps.add(pc)
            if pc > len(d) - 3:
                print(f"  {pc} possible {d[pc]} => {pc + val}")
            pc += val
        if ins == 'acc':
            reg += val
            pc += 1
        if ins == 'nop':
            nops.add(pc)
            if pc + val > len(d) - 12:
                print(f"  {pc} possible {d[pc]} => {pc + val}")
            pc += 1
        if ins == 'exit':
            print(f"P2: pc={alter}, accumulator = {reg}")
            return reg
    return reg


acc = run()
print(f"P1: accumulator is {acc}")

nop_list = list(nops)
jmp_list = list(jmps)

for nop in nop_list:
    acc = run(nop)


for jmp in jmp_list:
    try:
        acc = run(jmp)
    except IndexError as e:
        print(f"P2: pc={jmp}, accumulator = {acc}")
        print(e)
        break
