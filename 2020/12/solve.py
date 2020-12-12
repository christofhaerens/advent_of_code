#!/usr/bin/python3
# import itertools
# import functools
# import re
# from collections import Counter
# from collections import defaultdict

day = "--- Day 11 - 2020 ---"


def part1(d):
    move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    f = "E"  # started headed east
    directions = 'NESW'
    move['F'] = move[f]
    x, y = 0, 0
    for nav in d:
        action, count = nav[0], int(nav[1:])
        if action in 'FNESW':
            x, y = x + (count * move[action][0]), y + (count * move[action][1])
        elif action in 'LR':
            d = directions.index(f)
            count = count // 90
            if action == 'R':
                f = directions[(d + count) % 4]
            else:
                f = directions[(d - count) % 4]
            move['F'] = move[f]
    return abs(x) + abs(y)


def part2(d):
    move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    wx, wy = 10, 1
    x, y = 0, 0
    for nav in d:
        action, count = nav[0], int(nav[1:])
        if action in 'NESW':
            wx, wy = wx + (count * move[action][0]), wy + (count * move[action][1])
        elif action == 'F':
            x, y = x + (count * wx), y + (count * wy)
        elif action in 'LR':
            count = (count // 90) % 4
            if action == 'R':
                for _ in range(count):
                    wx, wy = wy, -wx
            else:
                for _ in range(count):
                    wx, wy = -wy, wx
    return abs(x) + abs(y)


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
