#!/usr/bin/python3
import itertools
import functools

day = "--- Day 1 - 2020 ---"


def find_sum(expenses, required_sum, count):
    for c in itertools.combinations(expenses, count):
        if sum(c) == required_sum:
            return functools.reduce(lambda x, y: x * y, c)
    raise Exception("Sorry, required sum not found")


def solve1(data, value):
    return find_sum(data, value, 2)


def solve2(data, value):
    return find_sum(data, value, 3)


def solve(data):
    a1 = solve1(data.copy(), 2020)
    a2 = solve2(data.copy(), 2020)
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
