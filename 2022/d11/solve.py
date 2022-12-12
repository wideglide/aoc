#!/usr/bin/env python3

from math import prod
import re
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

RE_STR = re.compile(
        r"Monkey (\d):\n"
        r"  Starting items: (.*)\n"
        r"  Operation: new = old (.*)\n"
        r"  Test: divisible by (\d+)\n"
        r"    If true: throw to monkey (\d+)\n"
        r"    If false: throw to monkey (\d+)\n",
        re.MULTILINE)


class Monkey:
    def __init__(self, idx, items, opf, modulo, mt, mf, gcm, reduce_worry=False):
        self.idx = idx
        self.items = items
        self.div_by = modulo
        self.monkey_true = mt
        self.monkey_false = mf
        self.operation = opf
        self.count = 0
        self.gcm = gcm
        self.reduce_worry = reduce_worry

    def op(self, i):
        # do operation
        worry = self.operation(self.items[i])
        if self.reduce_worry:
            # reduce worry level
            worry = int(worry / 3.0)
            self.items[i] = worry
        else:
            if worry > self.gcm:
                worry = worry % self.gcm
        self.items[i] = worry

    def test(self, i, reduce=False):
        # inspect item i
        self.op(i)
        self.count += 1
        if self.items[i] % self.div_by == 0:
            return self.monkey_true, self.items[i]
        else:
            return self.monkey_false, self.items[i]

    def __repr__(self):
        return f"Monkey {self.idx}: inspected items {self.count} times,  {self.items}"


def do_round(monkeys):
    for mid, monkey in enumerate(monkeys):
        for idx, _ in enumerate(monkey.items):
            new_m, item = monkey.test(idx)
            monkeys[new_m].items.append(item)
        monkey.items.clear()


def initialize_monkeys(reduce_worry=False):
    matches = RE_STR.findall(open(input_file).read())
    gcm = prod(int(m[3]) for m in matches)

    MONKEYS = list()
    for match in matches:
        M = Monkey(
                idx=int(match[0]),
                items=eval("[{}]".format(match[1])),
                opf=eval(f"lambda old: old {match[2]}"),
                modulo=int(match[3]),
                mt=int(match[4]),
                mf=int(match[5]),
                gcm=gcm,
                reduce_worry=reduce_worry,
                )
        MONKEYS.append(M)
    return MONKEYS


def print_monkeys(monkeys, header):
    print(header)
    for monkey in monkeys:
        print(monkey)


# part 1
# data = list(open(input_file).read().strip().split('\n'))
MONKEYS = initialize_monkeys(reduce_worry=True)

for n in range(20):
    do_round(MONKEYS)

print_monkeys(MONKEYS, "======== part 1 after 20 rounds =======")

monkey_business = prod(sorted([x.count for x in MONKEYS], reverse=True)[:2])

print(f" part1 total = {monkey_business}")


# part 2
MONKEYS = initialize_monkeys(reduce_worry=False)

for n in range(10000):
    if n == 20:
        print_monkeys(MONKEYS, f"======== part 2 after {n} rounds =======")
    do_round(MONKEYS)

print_monkeys(MONKEYS, f"======== part 2 after {n} rounds =======")
monkey_business = prod(sorted([x.count for x in MONKEYS], reverse=True)[:2])

print(f" part2 total = {monkey_business}")
