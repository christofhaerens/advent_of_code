#!/usr/bin/python3
# import itertools
# import functools
# import re
from collections import defaultdict, Counter

day = "--- Day 10 - 2020 ---"


def part1(d):
    j_diff = defaultdict(int)
    j = 0
    for ad in d:
        diff = ad - j
        if diff > 3:
            raise Exception
        j_diff[diff] += 1
        j = ad
    return j_diff[1] * j_diff[3]


def part2(d):
    # part 2 based on hints found on reddit day10
    total = defaultdict(int)
    total[0] = 1
    for i in range(len(d) - 1):
        j = i + 1
        while j < len(d) and d[j] <= d[i] + 3:
            total[j] += total[i]
            j += 1
    return total[len(d) - 1]


# alternative solution part1 & part2 found on https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf9le7q/
def part1_alt(d):
    c = Counter(j - i for i, j in zip(d, d[1:]))
    return c[1] * c[3]


def part2_alt(d):
    # Number of ways to arrange adapters from i to device is memo[i]
    memo = defaultdict(int)
    # Base case, only one way to add the device
    device = d.pop()
    memo[device] = 1
    for i in reversed(d):
        memo[i] = memo[i + 1] + memo[i + 2] + memo[i + 3]
    return memo[0]


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
    data = [int(line.strip()) for line in fh]
    fh.close()
    data.sort()
    data = [0] + data + [data[-1] + 3]
    solve(data)


if __name__ == '__main__':
    main()
