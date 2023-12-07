#!/usr/bin/env python3

import sys
import time

# from tqdm import trange
#       for seed in trange(start, stop, unit_scale=True):
# SLOW part2, tuples faster than ranges, pypy faster than python
#   python3.11 with ranges            175K it/s
#   python3.11 with tuples            196K it/s
#   python3.10 with tuples            164K it/s
#   pypy3.10   with tuples            1.25M it/s

input_file = 'input' if len(sys.argv) == 1 else sys.argv[1]


def do_mapping(src, ranges):
    for r, dst in ranges:
        if src in r:
            return dst + (src - r.start)
    return src


def do_mapping_tuples(src, ranges):
    for start, end, dst in ranges:
        if start <= src <= end:
            return dst + (src - start)
    return src


def load_maps(data):
    maps = {}
    for line in data:
        if 'seeds:' in line:
            _, seeds_str = line.strip().split(":")
            seeds = [int(x) for x in seeds_str.strip().split()]
        elif 'map:' in line:
            name, _ = line.strip().split()
            maps[name] = list()
            cur_map = name
        elif len(line) > 2:
            ranges = [int(x) for x in line.strip().split()]
            dst, src, length = ranges
            # maps[cur_map].append((range(src, src + length), dst))
            maps[cur_map].append((src, src + length, dst))
    return maps, seeds


def part1(maps, seeds):
    locations = []
    for seed in seeds:
        soil_n = do_mapping_tuples(seed,   maps['seed-to-soil'])
        fert_n = do_mapping_tuples(soil_n, maps['soil-to-fertilizer'])
        watr_n = do_mapping_tuples(fert_n, maps['fertilizer-to-water'])
        ligh_n = do_mapping_tuples(watr_n, maps['water-to-light'])
        temp_n = do_mapping_tuples(ligh_n, maps['light-to-temperature'])
        humd_n = do_mapping_tuples(temp_n, maps['temperature-to-humidity'])
        loc_n  = do_mapping_tuples(humd_n, maps['humidity-to-location'])
        locations.append(loc_n)

    print(f" min location = {min(locations)}")


def part2(maps, seeds):
    locations = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        stop = seeds[i] + seeds[i + 1] + 1
        now = time.time()
        for seed in range(start, stop):
            soil_n = do_mapping_tuples(seed,   maps['seed-to-soil'])
            fert_n = do_mapping_tuples(soil_n, maps['soil-to-fertilizer'])
            watr_n = do_mapping_tuples(fert_n, maps['fertilizer-to-water'])
            ligh_n = do_mapping_tuples(watr_n, maps['water-to-light'])
            temp_n = do_mapping_tuples(ligh_n, maps['light-to-temperature'])
            humd_n = do_mapping_tuples(temp_n, maps['temperature-to-humidity'])
            loc_n  = do_mapping_tuples(humd_n, maps['humidity-to-location'])
            if loc_n < min(locations, default=2**31):
                locations.append(loc_n)

        print(f"   {start} min location = {min(locations)}, length = {len(locations)} \t elapsed {time.time() - now}")

    print(f" min location = {min(locations)}")


# part 1
data = list(open(input_file).read().strip().split('\n'))

maps, seeds = load_maps(data)
# part1(maps, seeds)
# print(f" part1 total = {visible}")


# part 2
part2(maps, seeds)
# print(f" part2  = {MAX}")
