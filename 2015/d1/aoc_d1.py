
f = 0
i = 1

for c in open('INPUT','rt').read():
  if c == '(': f += 1
  if c == ')': f -= 1
  if f == -1: print(i)
  i += 1

print(f)
