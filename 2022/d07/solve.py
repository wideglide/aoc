#!/usr/bin/env python3

import os
import sys

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


class dr:
    def __init__(self, parent, name):
        self.name = name
        self.path = f"{parent}/{name}"
        self.files = {}
        self.dirs = {}

    def add_f(self, name, size):
        # add file
        self.files[name] = size

    def add_d(self, name):
        # add directory
        if name in self.dirs:
            return self.dirs[name]
        new_d = dr(self.path, name)
        self.dirs[name] = new_d
        return new_d

    def size(self):
        f_size = sum(fz for fz in self.files.values())
        d_size = sum(d.size() for d in self.dirs.values())
        return f_size + d_size


# part 1
data = list(open(input_file).read().strip().split('\n'))
PWD = "/"   # working directory
CUR = dr("", "/")  # Current directory
ALL = {PWD: CUR}
for _line in data:
    line = _line.strip()
    if '$ cd /' == line:
        PWD = "/"
        CUR = ALL[PWD]
    elif '$ cd ..' == line:
        PWD = os.path.dirname(PWD)
        CUR = ALL[PWD]
    elif '$ cd' in line:
        OWD = PWD
        PWD = os.path.join(PWD,  line.split(' ')[2])
        if PWD in ALL:
            CUR = ALL[PWD]
        else:
            CUR = dr(OWD, line[5:])
            ALL[PWD] = CUR
    elif '$ ls' in line:
        pass
    elif 'dir ' == line[:4]:
        name = line[4:]
        new_d = CUR.add_d(name)
        new_path = os.path.join(PWD, name)
        ALL[new_path] = new_d
    else:
        try:
            sz, name = line.split(' ')
        except ValueError:
            print(line)
            quit()
        CUR.add_f(name, int(sz, 10))

print(f"   number of directories = {len(ALL)}")
total = 0
for path in ALL:
    CUR = ALL[path]
    cur_size = CUR.size()
    if cur_size <= 100000:
        total += cur_size

print(f" part1 total = {total}")


# part 2
min_dir = 70000000
ROOT_SZ = ALL["/"].size()
NEED = 30000000 - (min_dir - ROOT_SZ)
for path in ALL:
    CUR = ALL[path]
    cur_size = CUR.size()
    if cur_size >= NEED:
        if cur_size < min_dir:
            min_dir = cur_size

print(f" part2 min dir size = {min_dir}")
