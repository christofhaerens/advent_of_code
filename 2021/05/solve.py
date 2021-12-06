#!/usr/bin/python3
from collections import Counter

day = "--- Day 5 - 2021 ---"


def map_lines(data):
    ver_hor_points = []
    all_points = []

    for line in data:
        x1, y1 = [int(p) for p in line[0].split(",")]
        x2, y2 = [int(p) for p in line[2].split(",")]
        dx = x2 - x1
        dx = 0 if dx == 0 else dx // abs(dx)
        dy = y2 - y1
        dy = 0 if dy == 0 else dy // abs(dy)
        while True:
            all_points.append((x1, y1))
            if dx == 0 or dy == 0:
                ver_hor_points.append((x1, y1))
            if (x1, y1) == (x2, y2):
                break
            x1 += dx
            y1 += dy

    ver_hor_points = Counter(ver_hor_points)
    all_points = Counter(all_points)
    return sum([1 if ver_hor_points[k] > 1 else 0 for k in ver_hor_points]), sum([1 if all_points[k] > 1 else 0 for k in all_points])


def solve1(data):
    return map_lines(data)


def solve2(data):
    return 0


def solve(data):
    a1, a2 = solve1(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    data = []
    with open('./input.txt', 'r') as fh:
        data = [line.strip().split() for line in fh]
    solve(data)


if __name__ == '__main__':
    main()
