#!/usr/bin/python3
# import itertools
# import functools
# import re
import math
# from collections import Counter
# from collections import defaultdict

day = "--- Day 13 - 2020 ---"


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part1(d):
    depart = int(d[0])
    r = []
    busses = [int(x) if x != 'x' else None for x in d[1].split(",")]
    for b in busses:
        if b is None:
            r.append(depart)
        else:
            r.append(b - (depart % b))
    shortest = min(r)
    bus = busses[r.index(shortest)]
    return bus * shortest


# alt solution for part2 is with Chinese Remainder Thereom https://en.wikipedia.org/wiki/Chinese_remainder_theorem
def part2(d):
    t = 0
    step = 1
    busses = d[1].split(",")
    for b in busses:
        if b != 'x':
            b = int(b)
            while (t % b) != 0:
                t += step
            step *= b
        t += 1
    return t - len(busses)


def solve1(data):
    return part1(data)


def solve2(data):
    return part2(data)


def solve(data):
    a1 = solve1(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    a2 = solve2(data.copy())
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
