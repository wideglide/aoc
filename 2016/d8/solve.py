#!/usr/bin/env python

f = [ l.strip() for l in open('input').readlines() ]

def rect(m, x, y):
    return [ [ 1 if i<x and j<y else v for i,v in enumerate(row)] for j,row in enumerate(m) ]

def rot_col(m, col, shift):
    h = len(m)
    sh = shift % h
    return [ [ m[(j-sh) % h][i] if i==col else m[j][i] for i,row in enumerate(row) ] for j,row in enumerate(m) ]

def rot_row(m, row, shift):
    sh = shift % len(m[0])
    m[row] = m[row][-sh:] + m[row][:-sh]

def display(m):
    line = "\t"+''.join([str(i%10) if i%5==0 else " " for i in range(50)])
    print line
    for row in m:
        line = "\t"+''.join(["#" if v==1 else " " for v in row])
        print line
        
m = [ [ 0 for x in range(50) ] for y in range(6) ]
total = 0
for l in f:
    on = sum(map(sum,m))
    op = l.split(" ")
    if op[0] == "rect":
        x,y = map(int,op[1].split('x'))
        total += (x * y)
        m = rect(m, x, y)
    if op[0] == 'rotate':
        rc = int(op[2].split('=')[1])
        shift = int(op[4])
        if op[1] == 'row':
            rot_row(m, rc, shift) 
        if op[1] == 'column':
            m = rot_col(m, rc, shift)

display(m)
print sum(map(sum, m)), total
