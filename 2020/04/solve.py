#!/usr/bin/python3
# import itertools
# import functools
import re

day = "--- Day 4 - 2020 ---"


class Passport(object):

    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def is_valid(self, strict=False):
        fields = [self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid]
        if None in fields:
            return False
        else:
            if strict is True:
                return False if "" in fields else True
            else:
                return True

    def add_field(self, field):
        k, v = field.split(":")
        if k == "byr":
            v = int(v)
            self.byr = "" if v < 1920 or v > 2002 else v
        elif k == "iyr":
            v = int(v)
            self.iyr = "" if v < 2010 or v > 2020 else v
        elif k == "eyr":
            v = int(v)
            self.eyr = "" if v < 2020 or v > 2030 else v
        elif k == "hgt":
            m = re.match(r'(\d+)(cm|in)', v)
            if m is None:
                self.hgt = ""
            else:
                v, u = m.groups()
                v = int(v)
                if u == "cm":
                    self.hgt = "" if v < 150 or v > 193 else v
                else:
                    self.hgt = "" if v < 59 or v > 76 else v
        elif k == "hcl":
            m = re.search(r'^#[0-9a-f]{6}$', v)
            self.hcl = "" if m is None else m.string
        elif k == "ecl":
            self.ecl = v if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else ""
        elif k == "pid":
            m = re.search(r'^[0-9]{9}$', v)
            self.pid = "" if m is None else m.string
        elif k == "cid":
            self.cid = v


def pp_check(d, strict_mode):
    d.append("")  # append empty line to process the last entry
    valid_pp = 0
    pp = Passport()
    for line in d:
        if line == "":
            if pp.is_valid(strict=strict_mode):
                valid_pp += 1
            pp = Passport()
            continue
        for field in line.split(" "):
            pp.add_field(field)
    return valid_pp


def solve1(data):
    return pp_check(data, strict_mode=False)


def solve2(data):
    return pp_check(data, strict_mode=True)


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
