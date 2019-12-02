#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 15: Beverage Bandits ---"


def find_targets(map, units):
    # return the targets that are in range
    for u in unit:
        

def find_path(map, unit, targets):


def solve(data):
    map = {}
    elf = []
    gnome = []
    for y, row in enumerate(data):
        for x, m in enumerate(row):
            if m == 'E':
                elf.append((x, y, 200))
            elif m == 'G':
                gnome.append((x, y, 200))
            map[(x, y)] = m if m == '#' else '.'
    print(len(gnome), gnome)
    print(len(elf), elf)
    return ['a', 'a']


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip('\n') for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
