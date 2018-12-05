#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 5: Alchemical Reduction ---"


def collapse(polymer):
    u = 'abcdefghijklmnopqrstuvwxyz'
    units = []
    for c in u:
        units += [c + c.upper(), c.upper() + c]
    while True:
        start_len = len(polymer)
        for u in units:
            polymer = polymer.replace(u, '')
        if len(polymer) == start_len:
            return polymer


def solve(data):
    polymer = collapse(data[0])
    a1 = len(polymer)
    u = 'abcdefghijklmnopqrstuvwxyz'
    a2 = []
    for c in u:
        polymer = data[0]
        polymer = polymer.replace(c, '')
        polymer = polymer.replace(c.upper(), '')
        polymer = collapse(polymer)
        a2.append(len(polymer))
    return [str(a1), str(min(a2))]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %s" % a[0])
    print("part2 = %s" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
