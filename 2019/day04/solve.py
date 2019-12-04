#!/usr/bin/python3

import re
from collections import defaultdict

day = "--- Day 4 - 2019 ---"


def valid_pw(pw, part=1):
    dd = '0'
    equal = defaultdict(int)
    for d in pw:
        if d < dd:
            return False
        equal[d] += 1
        dd = d
    if part == 1:
        return True if max(equal.values()) > 1 else False
    else:
        return True if 2 in equal.values() else False


def find_pw(start, stop, part=1):
    valid = 0
    for i in range(start, stop + 1):
        if valid_pw(str(i), part):
            valid += 1
    return valid


def solve1():
    return find_pw(197487, 673251)


def solve2():
    return find_pw(197487, 673251, part=2)


def solve():
    print("\n%s" % day)
    print("part1 = %r" % solve1())
    print("part2 = %r" % solve2())
    print()


def main():
    solve()


if __name__ == '__main__':
    main()
