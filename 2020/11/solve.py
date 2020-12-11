#!/usr/bin/python3
# import itertools
# import functools
# import re
# from collections import Counter
# from collections import defaultdict

day = "--- Day 11 - 2020 ---"
FREE, FLOOR, OCCUPIED = "L", ".", "#"


def part1(d):
    xmax = len(d[0])
    ymax = len(d)
    after = [['.' for _ in range(xmax)] for _ in range(ymax)]
    while True:
        changed = 0
        for y, row in enumerate(d):
            for x, seat in enumerate(row):
                if seat == FLOOR:
                    continue
                adj_seats = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    sx, sy = x + dx, y + dy
                    if sx >= xmax or sx < 0 or sy >= ymax or sy < 0:
                        continue
                    if d[sy][sx] == OCCUPIED:
                        adj_seats += 1
                if seat == FREE and adj_seats == 0:
                    after[y][x] = OCCUPIED
                    changed += 1
                elif seat == OCCUPIED and adj_seats > 3:
                    after[y][x] = FREE
                    changed += 1
                else:
                    after[y][x] = seat
        if changed == 0:
            c = 0
            for row in after:
                for seat in row:
                    if seat == OCCUPIED:
                        c += 1
            return c
        d = after
        after = [['.' for _ in range(xmax)] for _ in range(ymax)]


def part2(d):
    xmax = len(d[0])
    ymax = len(d)
    after = [['.' for _ in range(xmax)] for _ in range(ymax)]
    while True:
        changed = 0
        for y, row in enumerate(d):
            for x, seat in enumerate(row):
                if seat == FLOOR:
                    continue
                adj_seats = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    sx, sy = x, y
                    while True:
                        sx, sy = sx + dx, sy + dy
                        if sx >= xmax or sx < 0 or sy >= ymax or sy < 0:
                            break
                        if d[sy][sx] == OCCUPIED:
                            adj_seats += 1
                            break
                        elif d[sy][sx] == FREE:
                            break
                if seat == FREE and adj_seats == 0:
                    after[y][x] = OCCUPIED
                    changed += 1
                elif seat == OCCUPIED and adj_seats > 4:
                    after[y][x] = FREE
                    changed += 1
                else:
                    after[y][x] = seat
        if changed == 0:
            c = 0
            for row in after:
                for seat in row:
                    if seat == OCCUPIED:
                        c += 1
            return c
        d = after
        after = [['.' for _ in range(xmax)] for _ in range(ymax)]


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
