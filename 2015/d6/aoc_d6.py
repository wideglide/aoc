import re
from collections import Counter

d = dict()

def part1():
    for cmd in open('input','rt').readlines():
      p = re.compile('(on|off|toggle)')
      action = p.findall(cmd)[0]
      p = re.compile('\d+')
      l = list(map(lambda x: int(x), p.findall(cmd)))
      for x in range(l[0],l[2]+1):
        for y in range(l[1],l[3]+1):
          if action == 'on': d[(x,y)] = 1
          if action == 'off': d[(x,y)] = 0
          if action == 'toggle':
            if (x,y) in d:
              v = d[(x,y)]
              d[(x,y)] = v ^ 1
            else:
              d[(x,y)] = 1

    print(len([v for k,v in d.items() if v == 1]))

def part2():
    d = Counter()
    p = re.compile('\d+')
    for x in range(1000):
      for y in range(1000):
        d[(x,y)]=0
    for cmd in open('input','rt').readlines():
      action = cmd[:7]
      l = list(map(lambda x: int(x), p.findall(cmd)))
      for x in range(l[0],l[2]+1):
        for y in range(l[1],l[3]+1):
          v = d[(x,y)]
          if action == 'turn on': d[(x,y)] = v+1
          if action == 'turn of': d[(x,y)] = max(0, v-1)
          if action == 'toggle ': d[(x,y)] = v+2

    print(sum(d.values()))

part1()
part2()
