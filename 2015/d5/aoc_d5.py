import time

start = time.time()
part1 = 0
part2 = 0
for s in open('input','rt').read().split():
  if 'ab' in s: continue
  if 'cd' in s: continue
  if 'pq' in s: continue
  if 'xy' in s: continue
  if s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u') < 3: continue
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      part1 += 1
      break

end1 = time.time()
for s in open('input','rt').read().split():
  a = b = False
  c = ''
  d = ''
  for i in range(len(s)-2):
    if s[i] == s[i+2]:
      b = True
      d = s[i]
    if s[i+2:].count(s[i:i+2]) > 0:
      a = True
      c = s[i:i+2]

  if a and b:
    part2 += 1
    print(part2, s, c, d)

end2 = time.time()
print(part1, end1-start)
print(part2, end2-end1)
