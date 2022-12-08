import string

s = ""
total = 0
with open('input','rt') as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if c in string.digits+'-':
      s += c;
    elif len(s) > 0:
      total += int(s)
      s = ""

print(total)
