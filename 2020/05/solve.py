#!/usr/bin/python3
# import itertools
# import functools
# import re

day = "--- Day 5 - 2020 ---"


def p_2_number(p):
    n = 0
    for i in p:
        n = n << 1
        if i in ["B", "R"]:
            n += 1
    return n


def find_seat(d, part):
    seats = []
    for partition in d:
        row = p_2_number(partition[:7])
        col = p_2_number(partition[7:])
        seats.append(row * 8 + col)
    if part == 1:
        return max(seats)
    if part == 2:
        seats.sort()
        for i in range(min(seats) + 1, max(seats)):
            if i not in seats:
                return i
        return None


def solve1(data):
    return find_seat(data, 1)


def solve2(data):
    return find_seat(data, 2)


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
