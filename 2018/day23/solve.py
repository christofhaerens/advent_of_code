#!/usr/bin/python3

import re
from collections import defaultdict, Counter
from operator import itemgetter, attrgetter


day = "--- Day 23: Experimental Emergency Teleportation ---"


class Bot(object):
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.xmin, self.xmax = x - r, x + r
        self.ymin, self.ymax = y - r, y + r
        self.zmin, self.zmax = z - r, z + r

    def distance(self, b1, b2=None):
        b2 = self if b2 is None else b2
        return abs(b1.x - b2.x) + abs(b1.y - b2.y) + abs(b1.z - b2.z)

    def has_in_r(self, other):
        return True if self.distance(other) <= self.r else False

    def bot_in_r(self, bot):
        return True if self.r + bot.r >= abs(self.x - bot.x) + abs(self.y - bot.y) + abs(self.z - bot.z) else False

    def __str__(self):
        return "r=%d (%d, %d, %d)" % (self.r, self.x, self.y, self.z)


def solve(data):
    bots = []
    for d in data:
        # pos=<88479540,-9444790,-13848267>, r=96310986
        m = re.match(r'pos=<([-\d]+),\s*([-\d]+),\s*([-\d]+)>,\s*r=([-\d]+)', d)
        bots.append(Bot(*map(int, m.groups())))
    bots.sort(key=lambda b: b.r)
    largest_r = bots[-1]
    a1 = sum([1 for bot in bots if largest_r.has_in_r(bot)])
    # part2
    # the idea for this solution I got from reddit day 23 (next to lots op people using z3)
    # create bots with large r, count how many in range and make the r smaller until it's 1 in size
    #
    # first, find the max gap
    xs = [b.x for b in bots]
    ys = [b.y for b in bots]
    zs = [b.z for b in bots]
    center = Bot(0, 0, 0, 0)

    maxgap = max([max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)])
    # since we ant to end with gap = 1, we make gap always divisable by 2
    gap = 1
    while gap < maxgap:
        gap *= 2

    while True:
        best = 0
        bestbot = None
        gap = gap // 2
        for z in range(min(zs), max(zs) + 1, gap):
            for y in range(min(ys), max(ys) + 1, gap):
                for x in range(min(xs), max(xs) + 1, gap):
                    r = 0 if gap == 1 else gap // 2
                    ourbot = Bot(x, y, z, r)
                    bots_in_range = sum([1 for b in bots if ourbot.bot_in_r(b)])
                    # print(ourbot, bots_in_range)
                    if bots_in_range > best:
                        best = bots_in_range
                        bestbot = ourbot
                    elif bestbot is None:
                        bestbot = ourbot
                    elif bots_in_range == best:
                        # if we have a tie, keep the bot closest to pos (0,0,0)
                        if ourbot.distance(center) < bestbot.distance(center):
                            bestbot = ourbot
        if gap == 1:
            break
        xs = [bestbot.xmin, bestbot.xmax]
        ys = [bestbot.ymin, bestbot.ymax]
        zs = [bestbot.zmin, bestbot.zmax]
    return [a1, bestbot.distance(center)]


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

# not 498
