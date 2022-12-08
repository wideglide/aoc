
f = [ l.strip() for l in open('input').readlines() ]

count = 0
count2 = 0
for l in f:
    flag = 0
    found = 0
    for i in range(len(l)-3):
        if l[i] == "[" and l.find("]",i+1) > 0:
            flag = 1
        if l[i] == "]" and flag == 1:
            flag = 0
        if l[i] == l[i+3] and l[i] != l[i+1] and l[i+1] == l[i+2]:
            if flag == 1: 
                found = 0
                break
            found = 1
    count += found
for l in f:
    flag = 0
    found2 = 0
    aba = list()
    for i in range(len(l)-2):
        if l[i] == "[" and l.find("]",i+1) > 0:
            flag = 1
        if l[i] == "]" and flag == 1:
            flag = 0
        if l[i] == l[i+2] and l[i] != l[i+1]:
            bab = l[i+1]+l[i]+l[i+1]
            if bab in l:
                aba.append((l[i:i+3],flag))
            else:
                continue    
            if (bab,(flag ^ 1)) in aba:
                found2 = 1
    count2 += found2
print count, count2
