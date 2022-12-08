#!/usr/bin/env python

d = [  l.strip().split(' ') for l in open('input','rb').readlines()] 

print sum([1 for l in d if len(set(l)) == len(l)])

d2 = [ [''.join(sorted(list(w))) for w in l] for l in d]
print sum([1 for l in d2 if len(set(l)) == len(l)])      
