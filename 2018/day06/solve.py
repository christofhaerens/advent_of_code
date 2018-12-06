#!/usr/bin/python3

import re
from collections import defaultdict, Counter, OrderedDict
from operator import itemgetter, attrgetter


day = "--- Day 6: Chronal Coordinates ---"


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve(data):
    # to store the points in (x, y) coord format
    points = [tuple(map(int, d.split(', '))) for d in data]
    # get the min and max
    xmin = min([p[0] for p in points])
    xmax = max([p[0] for p in points])
    ymin = min([p[1] for p in points])
    ymax = max([p[1] for p in points])
    # build the map
    area_per_idx = defaultdict(int)
    excluded = {}
    region = 0
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            # calculate distances to all points. We want only the shortes distance for part1
            # if only 1 point has the shortest, we mark it with the idx of the point, otherwise it's overlapping and we ignore
            distances = [manhattan(p, (x, y)) for p in points]
            shortest = min(distances)
            indexes = [idx for idx, d in enumerate(distances) if d == shortest]
            if len(indexes) == 1:
                area_per_idx[indexes[0]] += 1
                # if it is on the edge of our map then it will be infinite and we must exclude it for the area
                if x in (xmin, xmax) or y in (ymin, ymax):
                    excluded[indexes[0]] = 1
            # part2
            if sum(distances) < 10000:
                region += 1
    # our map is complte, now find the largest area with the excluded
    for idx in excluded:
        area_per_idx[idx] = 0
    w = Counter(area_per_idx)
    return [w.most_common(1)[0][1], region]


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
