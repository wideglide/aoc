#!/usr/bin/env python3

from collections import defaultdict

# part 1
d = list(open('input').read().strip().split('\n'))


def _decode(txt, lo_tup, hi_tup):
    lo, upper = lo_tup
    hi, lower = hi_tup
    for c in txt:
        if c == upper:
            lo = (hi - lo + 1) / 2 + lo
        if c == lower:
            hi = hi - (hi - lo + 1) / 2
    if c == lower:
        return lo
    return hi


def decode_row(txt):
    return _decode(txt, (0, 'B'), (127, 'F'))


def decode_col(txt):
    return _decode(txt, (0, 'R'), (7, 'L'))


seat_list = defaultdict(dict)


def decode(line, verbose=False):
    row = decode_row(line[:7])
    col = decode_col(line[7:])

    sid = row * 8 + col
    s = f" row {row}, column {col}, seat ID {sid}"
    if verbose:
        print(s)
    seat_list[row].update({col: sid})

    return sid


examples = [
        'FBFBBFFRLR',
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL']

print(max(decode(e, verbose=True) for e in examples))

print(max(decode(line) for line in d))

for k, row in seat_list.items():
    if len(row.keys()) != 8:
        print(k, row, sorted(row.values()))


def fix(s):
    return ''.join('0' if c in 'FL' else '1' for c in s)


bnums = {int(fix(s), 2) for s in d}

print(max(bnums))
print((set(range(min(bnums), max(bnums)+1)) - bnums).pop())
