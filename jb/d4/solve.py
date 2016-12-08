from collections import Counter
import operator
import string
f = [l.strip() for l in open('input').readlines() ]

count = 0
for l in f:
    ltrs = Counter()
    pt = ""
    sid = int(l[l.rfind("-")+1:l.find("[")])
    rot = sid % 26
    cksum = l[l.find("[")+1:l.find("]")]
    for c in l:
        if c in string.lowercase: 
            ltrs[c] += 1
            i = string.lowercase.find(c)
            pt += string.lowercase[(i+rot) % 26]
        if c == "-": pt += " "
    mc = Counter(ltrs).most_common(5)
#   mc-sort = sorted(mc, key=operator.itemgetter(2,1))
    mc =  sorted(mc, key=lambda x: x[0])
    mc = sorted(mc, key=lambda x: x[1], reverse=True)
    if cksum == ''.join([x[0] for x in mc]):
        count += sid
    if "north" in pt: print pt, sid
    
print count
