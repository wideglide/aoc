#!/usr/bin/env python

d = [l.strip() for l in open('input','rb').readlines()]
l = d[0]

total = sum([ int(l[i]) for i in xrange(len(l)) if l[i] == l[(i+1) % len(l)] ])
print total 
h = len(l) / 2
total = sum([ int(l[i]) for i in xrange(len(l)) if l[i] == l[(i+h) % len(l)] ])
print total 
