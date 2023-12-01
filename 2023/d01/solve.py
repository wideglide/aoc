#!/usr/bin/env python3

import string
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

data = list(open(input_file).read().strip().split('\n'))


# part 1
def do_part1(data):
    numbers = [list(filter(lambda x: x in string.digits, w)) for w in data]
    total = sum(int(x[0] + x[-1]) for x in numbers)
    print(f" part1 total = {total}")


# part 2

rep = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': '4',
    'five': '5e',
    'six': '6',
    'seven': '7n',
    'eight': 'e8t',
    'nine': 'n9e',
}
prefixes = [r[:3] for r in rep]


def filter_num(w):
    word = w
    i = 0
    while i < len(word):
        for nstr in rep.keys():
            length = len(nstr)
            if word[i:i+length] == nstr:
                word = word.replace(nstr, rep[nstr], 1)
        i += 1
    return word


mod_data = [filter_num(w) for w in data]
numbers = [list(filter(lambda x: x in string.digits, w)) for w in mod_data]
values = [int(x[0] + x[-1]) for x in numbers]
total = sum(values)
total = sum(values)
print(f" part 2 total = {total}")
