#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


def print_map(VIS):
    for j in range(Y_len):
        for i in range(X_len):
            if (i, j) in VIS:
                print("V", end="")
            else:
                print(" ", end="")
        print("|")


def count_rows(xs, xe, ys, ye, inc, _VIS):
    for j in range(ys, ye):
        MAX = -1
        for i in range(xs, xe, inc):
            if grid[j][i] > MAX:
                _VIS.add((i, j))
                MAX = grid[j][i]


def count_cols(xs, xe, ys, ye, inc, _VIS):
    for i in range(xs, xe):
        MAX = -1
        for j in range(ys, ye, inc):
            if grid[j][i] > MAX:
                _VIS.add((i, j))
                MAX = grid[j][i]


def count_row_T(xs, xe, ys, inc):
    VIS = 0
    MAX = grid[ys][xs]
    for i in range(xs + inc, xe, inc):
        if grid[ys][i] < MAX:
            VIS += 1
        else:
            return VIS + 1
    return VIS


def count_col_T(xs, ys, ye, inc):
    VIS = 0
    MAX = grid[ys][xs]
    for j in range(ys + inc, ye, inc):
        if grid[j][xs] < MAX:
            VIS += 1
        else:
            return VIS + 1
    return VIS


def count_from(x, y):
    left = count_row_T(x, X_len, y, 1)
    right = count_row_T(x, -1, y, -1)
    down = count_col_T(x, y, Y_len, 1)
    up = count_col_T(x, y, -1, -1)
    return left * right * up * down


# part 1
data = list(open(input_file).read().strip().split('\n'))

grid = []
for line in data:
    grid.append(list(map(int, line.strip())))

X_len = len(grid[0])
Y_len = len(grid)
print(f"  GRID loaded {len(grid[0])} X {len(grid)}")

VIS = set()
# count rows, from left
count_rows(0, X_len, 0, Y_len, 1, VIS)
# count rows, from right
count_rows(X_len - 1, 0, 0, Y_len, -1, VIS)
# count cols, from top
count_cols(0, X_len, 0, Y_len, 1, VIS)
# count cols, from bottom
count_cols(0, X_len, Y_len - 1, 0, -1, VIS)

# OUTPUT
visible = len(VIS)
print(f" part1 total = {visible}")


# part 2
MAX = 0
for j in range(1, Y_len - 1):
    for i in range(1, X_len - 1):
        val = count_from(i, j)
        if val > MAX:
            MAX = val

print(f" part2  = {MAX}")
