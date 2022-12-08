from collections import Counter

f = [l.strip() for l in open('input').readlines() ]

data = [None] * len(f[0])
print data
for l in f:
    for i in range(len(l)):
        if data[i] == None: data[i] = Counter()
        data[i][l[i]] +=1
print [Counter(l).most_common(1)[0][0] for l in data]
print ''.join([Counter(l).most_common(1)[0][0] for l in data])
print ''.join([Counter(l).most_common()[-1][0] for l in data])
