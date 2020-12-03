#!/usr/bin/python3
# import itertools
# import functools
# import re

day = "--- Day 3 - 2020 ---"


def count_trees_by_slope(d, dx, dy):
    x, y = dx, dy
    bottom = len(d)
    row = len(d[0])
    trees = 0
    while y < bottom:
        x = x if x < row else x % row
        if d[y][x] == '#':
            trees += 1
        x, y = x + dx, y + dy
    return trees


def solve1(data):
    return count_trees_by_slope(data, 3, 1)


def solve2(data):
    a = 1
    for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        a = a * count_trees_by_slope(data, *slope)
    return a


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
