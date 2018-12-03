#!/usr/bin/python3

import re
from collections import defaultdict

day = "--- Day 1: Chronal Calibration ---"


def solve(start, data):
    f_list = [int(d) for d in data]
    final_freq = start + sum(f_list)
    freq = start
    previous = defaultdict(int)
    while True:
        for f in f_list:
            freq += f
            previous[freq] += 1
            if previous[freq] == 2:
                return [str(final_freq), str(freq)]


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
