#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 25: Four-Dimensional Adventure ---"


def md(p1, p2):
    return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])


class Constellation(object):
    def __init__(self, p):
        self.points = [p]
        p.linked = self

    def join(self, newp):
        for p in self.points:
            if md(p.p, newp.p) <= 3:
                self.points.append(newp)
                newp.linked = self
                return 1
        return 0


class Point(object):
    def __init__(self, p):
        self.p = p
        self.linked = False


def solve(data):
    points = []
    constellations = []
    for d in data:
        p = Point(tuple(map(int, d.split(','))))
        points.append(p)
    # add a first random point to a Constellation
    found = 0
    unlinked = [p for p in points if not p.linked]
    while len(unlinked) > 0:
        if found == 0:
            # if not found a matching constellation, we will create a new
            p = unlinked[0]
            c = Constellation(unlinked[0])
            constellations.append(c)
            found = 1
        else:
            found = 0
            # we found a point we could add, loop again over the unlinked
            for p in unlinked:
                found += c.join(p)
        unlinked = [p for p in points if not p.linked]

    a1 = len(constellations)
    return [a1, None]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
