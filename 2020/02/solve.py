#!/usr/bin/python3
# import itertools
# import functools
import re

day = "--- Day 2 - 2020 ---"


def check_pw_policy1(d):
    valid = 0
    for l in d:
        rule_min, rule_max, rule_char, pw = int(l[0]), int(l[1]), l[2], l[3]
        count = pw.count(rule_char)
        if count >= rule_min and count <= rule_max:
            valid += 1
    return valid


def check_pw_policy2(d):
    valid = 0
    for l in d:
        p1, p2, rule_char, pw = int(l[0]) - 1, int(l[1]) - 1, l[2], l[3]
        count = [pw[p1], pw[p2]].count(rule_char)
        if count == 1:
            valid += 1
    return valid


def solve1(data):
    return check_pw_policy1(data)


def solve2(data):
    return check_pw_policy2(data)


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [re.match(r'^\s*(\d+)-(\d+)\s+(\w):\s+(\w+)', line.strip()).groups() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
