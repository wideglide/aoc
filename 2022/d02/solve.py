#!/usr/bin/env python3

import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]

# part 1
d = list(open(input_file).read().strip().split('\n'))

WIN = {'A Y', 'B Z', 'C X'}
TIE = {'A X', 'B Y', 'C Z'}
LOSE = {'A Z', 'B X', 'C Y'}
VAL1 = {x: 6 for x in WIN}
VAL1.update({x: 3 for x in TIE})
VAL1.update({x: 0 for x in LOSE})
VAL = {'X': 1, 'Y': 2, 'Z': 3}


def score(line):
    return VAL1[line] + VAL[line.split(' ')[1]]


scores = [score(line) for line in d]
games = [sum(scores[i:i+3]) for i in range(0, len(scores), 3)]
print(f" part1 = {sum(scores)}")


# part 2

def choose(line):
    choices = {'X': LOSE, 'Y': TIE, 'Z': WIN}
    p1, p2 = line.split(' ')
    choice = [x for x in choices[p2] if p1 in x][0]
    val = score(choice)
    return val


sample = ['A Y', 'B X', 'C Z']
scores = [choose(line) for line in d]
print(f" part2 = {sum(scores)}")
