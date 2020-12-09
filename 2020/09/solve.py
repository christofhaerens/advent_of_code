#!/usr/bin/python3
import itertools
# import functools
# import re
# from collections import defaultdict

day = "--- Day 9 - 2020 ---"


def find_sum(numbers, required_sum, count):
    for c in itertools.combinations(numbers, count):
        if sum(c) == required_sum:
            if c[0] != c[1]:
                return True
    return False


def part1(d):
    for i in range(len(d) - 26):
        numbers = d[i:i + 25]
        required_sum = d[i + 25]
        if not find_sum(numbers, required_sum, 2):
            return required_sum
    return 0


def part2(d, required_sum):
    size = len(d)
    set_len = 2
    for set_len in range(2, size):
        for i in range(0, size - set_len):
            current_sum = sum(d[i:i + set_len])
            if current_sum == required_sum:
                return min(d[i:i + set_len]) + max(d[i:i + set_len])


def solve1(data):
    return part1(data)


def solve2(data, a1):
    return part2(data, a1)


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy(), a1)
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [int(line.strip()) for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
