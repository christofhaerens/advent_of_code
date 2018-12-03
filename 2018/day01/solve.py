#!/usr/bin/python3

import re

day = "--- Day 1: Chronal Calibration ---"


def solve(start, data):
    som = start
    a1 = 0
    seen = {}
    twice = False
    loop = 0
    while twice is False:
        loop += 1
        for p in data:
            m = re.match(r'^([-+])(\d+)', p)
            if m.group(1) == '-':
                som -= int(m.group(2))
            else:
                som += int(m.group(2))
            if twice is False and som in seen.keys():
                twice = som
            else:
                seen[som] = 1
        if loop == 1:
            a1 = som

    return [str(a1), str(twice)]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %s" % a[0])
    print("part2 = %s" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(0, data))


if __name__ == '__main__':
    main()
