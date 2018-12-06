#!/usr/bin/python3

import re
from collections import defaultdict, Counter, OrderedDict


day = "--- Day 6: Chronal Coordinates ---"


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve(data):
    x = {}
    y = {}
    xs = []
    ys = []
    # let's give each point a number
    ps = range(0, len(data))
    for p, d in enumerate(data):
        x[p], y[p] = [int(z) for z in d.split(', ')]
        xs.append(x[p])
        ys.append(y[p])
    xmax = max(xs)
    ymax = max(ys)
    xs = range(1, xmax + 1)
    ys = range(1, ymax + 1)
    # init the positions
    pos = {}  # positions
    pmap = {}  # pos map
    d_map = {}  # distance map
    for i in xs:
        pos[i] = {}
        pmap[i] = {}
        d_map[i] = {}
        for j in ys:
            pos[i][j] = {}
            pmap[i][j] = False
            d_map[i][j] = 0
    # now calculate manhattan for all each point
    for i in xs:
        for j in ys:
            for p in ps:
                ppos = (x[p], y[p])
                distance = manhattan(ppos, (i, j))
                # part1
                if distance in pos[i][j]:
                    pos[i][j][distance].append(p)
                else:
                    pos[i][j][distance] = [p]
                # part2
                d_map[i][j] += distance
    # for each point now check the distances we gathered
    area = defaultdict(int)
    excluded = []
    d_area = 0
    for i in xs:
        for j in ys:
            # check the shortest distance
            d = min(pos[i][j].keys())
            l = len(pos[i][j][d])
            if l == 1:
                p = pos[i][j][d][0]
                pmap[i][j] = str(p)
                area[p] += 1
                if i == 1 or i == xmax or j == 1 or j == ymax:
                    excluded.append(p)
            else:
                pmap[i][j] = '.'
            # part2
            if d_map[i][j] < 10000:
                d_area += 1
    for p in excluded:
        area[p] = 0
    w = Counter(area)
    a1 = w.most_common(1)[0][1]
    return [a1, d_area]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
