#!/usr/bin/python3
# import itertools
# import functools
# import re
# from collections import Counter
from collections import defaultdict

day = "--- Day 15 - 2020 ---"


def last_spoken(d, times):
    spoken = defaultdict(lambda: [])
    turn = 0
    for x in d:
        turn += 1
        spoken[x].append(turn)
    last = d[-1]
    while turn < times:
        turn += 1
        if len(spoken[last]) < 2:
            x = 0
        else:
            x = turn - 1 - spoken[last][-2]
        spoken[x].append(turn)
        last = x
    return last


def solve1(data):
    return last_spoken(data, 2020)


def solve2(data):
    return last_spoken(data, 30000000)


def solve(data):
    a1 = solve1(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    a2 = solve2(data.copy())
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [[int(x) for x in line.strip().split(",")] for line in fh]
    data = data[0]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
