

e1 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72".split(','),
      "U62,R66,U55,R34,D71,R55,D58,R83".split(',')]


with open('input') as f:
    w1 = f.readline().strip().split(',')
    w2 = f.readline().strip().split(',')


def new_pos(pos, ps, d, v):
    x, y = pos
    if d == 'U':
        [ps.add((x, y+i)) for i in range(1, v+1)]
        y += v
    elif d == 'D':
        [ps.add((x, y-i)) for i in range(1, v+1)]
        y -= v
    elif d == 'R':
        [ps.add((x+i, y)) for i in range(1, v+1)]
        x += v
    elif d == 'L':
        [ps.add((x-i, y)) for i in range(1, v+1)]
        x -= v
    else:
        print("[-] bad direction {} {} {}".format((x, y), d, v))
        return
    return (x, y)


def get_positions(w):
    r = set()
    pos = (0, 0)
    for m in w:
        v = int(m[1:])
        pos = new_pos(pos, r, m[0], v)
    return r


def sub(p2, p1):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1) + (y2-y1))


def get_steps(w, dest):
    pos = (0, 0)
    ln = 0
    for m in w:
        v = int(m[1:])
        r = set()
        p1 = new_pos(pos, r, m[0], v)
        if dest in r:
            ln += sub(dest, pos)
            return ln
        pos = p1
        ln += v


def find_min(same):
    print("[*] same locs = {} ".format(same))
    dis = [sum([abs(s[0]), abs(s[1])]) for s in same]
    print("part1 min distance = {} ".format(min(dis)))


def find_steps_min(same, l1, l2):
    r = list()
    for p in same:
        s1 = get_steps(l1, p)
        s2 = get_steps(l2, p)
        r.append(s1+s2)
    print("part2 min steps = {}".format(min(r)))


sameE1 = get_positions(e1[0]).intersection(get_positions(e1[1]))
sameW = get_positions(w1).intersection(get_positions(w2))
find_min(sameW)

find_steps_min(sameE1, e1[0], e1[1])
find_steps_min(sameW, w1, w2)
