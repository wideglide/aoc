#!/usr/bin/env python

d = [  l.strip() for l in open('input','rb').readlines()] 

registers = dict()

#  hi inc 119 if gf >= -5
rmax = 0
for l in d:
  reg1,op,val1,junk,reg2,cond,val2 = l.split()
  if reg1 not in registers:
    registers[reg1] = 0
  if reg2 not in registers:
    registers[reg2] = 0
  a = registers[reg1]
  b = registers[reg2]  
  cstr = "{} {} {}".format(b, cond, val2)
  if eval(cstr):
    if op == 'inc':
      registers[reg1] += int(val1)
    elif op == 'dec':
      registers[reg1] -= int(val1)
    else:
      print op
  if max(registers.values()) > rmax:
    rmax = max(registers.values())

print max(registers.values())
print rmax
