#!/usr/bin/env python3

# part 1
d = list(open('input').read().strip().split('\n\n'))


def is_hex(s):
    chars = '0123456789abcdef'
    return all(c in chars for c in s)


def check_valid(p, part_one=False):
    valid = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    if len(valid.intersection(p.keys())) != 7:
        return False
    if part_one:
        return True
    if not 1920 <= int(p['byr']) <= 2002:
        return False
    if not 2010 <= int(p['iyr']) <= 2020:
        return False
    if not 2020 <= int(p['eyr']) <= 2030:
        return False
    suffix = p['hgt'][-2:] if len(p['hgt']) > 2 else "NO"
    if suffix not in ['in', 'cm']:
        return False
    height = int(p['hgt'][:-2])
    if suffix == 'cm' and not 150 <= height <= 193:
        return False
    if suffix == 'in' and not 59 <= height <= 76:
        return False
    if len(p['hcl']) != 7 or p['hcl'][0] != '#':
        return False
    if not is_hex(p['hcl'][1:]):
        return False
    v_ecl = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if p['ecl'] not in v_ecl:
        return False
    if len(p['pid']) != 9 or not p['pid'].isdigit():
        return False
    return True


passports = [dict(p.split(':') for p in line.split()) for line in d]

print(f"[*] number of passports = {len(passports)}")

total_valid = sum(check_valid(p, part_one=True) for p in passports)
print(f"[*] P1: total valid passports = {total_valid}")

total_valid = sum(check_valid(p) for p in passports)
print(f"[*] P2: total valid passports = {total_valid}")
