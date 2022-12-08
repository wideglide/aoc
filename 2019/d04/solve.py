from collections import Counter


def check1(v):
    s = str(v)
    n = list(map(int, list(s)))
    if len(set(n)) == 6:
        return False
    for i in range(1, 6):
        if n[i-1] > n[i]:
            return False
    return True


def check(v):
    s = str(v)
    n = list(map(int, list(s)))
    if len(set(n)) == 6:
        return False
    c = Counter(n)
    if 2 not in c.values():
        return False
    for i in range(1, 6):
        if n[i-1] > n[i]:
            return False
    return True


r = list()

for i in range(353096, 843212):
    if check(i):
        r.append(i)

print(f"part2 = {len(r)}")
