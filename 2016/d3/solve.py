
f =  open('input').readlines() 
f = [ (int(s[:7]),int(s[7:11]),int(s[11:-1])) for s in f ]

count = 0
for t in f:
    if t[0]+t[1]>t[2] and t[1]+t[2]>t[0] and t[2]+t[0]>t[1]: count += 1        
print count

count = 0
for i in range(0,len(f),3):
    for j in range(3):
        t = (f[i][j],f[i+1][j],f[i+2][j])
        if t[0]+t[1]>t[2] and t[1]+t[2]>t[0] and t[2]+t[0]>t[1]: count += 1        
print count
