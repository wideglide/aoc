#!/usr/bin/env python3


orbits = dict()

for line in open('input').readlines():
    a, b = line.strip().split(')')
    orbits[b] = a


direct = len(orbits)

indirect = 0


def traverse(k, i, path=None):
    r = i
    if orbits.get(k):
        if path:
            path[k] = i
        r = traverse(orbits.get(k), i+1, path=path)
    return r


for k, v in orbits.items():
    indirect += traverse(v, 0)

print(f"[*] part1  D={direct} I={indirect}   value = {direct + indirect}")

you_path = {orbits["YOU"]: 0}
traverse(orbits["YOU"], 0, path=you_path)
print()
san_path = {orbits["SAN"]: 0}
traverse(orbits["SAN"], 0, path=san_path)

print(f" len you {len(you_path)}  length santa {len(san_path)}")
com = set(you_path.keys()).intersection(san_path.keys())
print(com)
distances = [you_path[s] + san_path[s] for s in com]
print(sorted(distances))
print(min(distances))
for s in com:
    if you_path[s] + san_path[s] == 379:
        print(s, you_path[s], san_path[s])
