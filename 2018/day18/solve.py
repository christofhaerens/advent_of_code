#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 18: Settlers of The North Pole ---"

TREE, OPEN, LUMBER = "|", '.', "#"
AROUND = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


class Grid(object):
    def __init__(self, size):
        self.grid = {}
        self.size = size
        self.changed_grid = {}
        self.loop = [(x, y) for y in range(0, self.size) for x in range(0, self.size)]

    def set(self, pos, v):
        self.grid[pos] = v

    def in_grid(self, pos):
        x, y = pos
        return True if x >= 0 and x < self.size and y >= 0 and y < self.size else False

    @staticmethod
    def add_pos(pos1, pos2):
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])

    def surrounding(self, pos):
        s = []
        for dpos in AROUND:
            npos = Grid.add_pos(pos, dpos)
            if npos in self.grid:
                s.append(self.grid[npos])
        w = Counter(s)
        s = dict(w)
        for v in (TREE, OPEN, LUMBER):
            if v not in s:
                s[v] = 0
        return s

    def magic(self):
        for pos in self.loop:
            v = self.grid[pos]
            s = self.surrounding(pos)
            if v == TREE:
                self.changed_grid[pos] = LUMBER if s[LUMBER] > 2 else v
            elif v == OPEN:
                self.changed_grid[pos] = TREE if s[TREE] > 2 else v
            elif v == LUMBER:
                self.changed_grid[pos] = LUMBER if s[TREE] > 0 and s[LUMBER] > 0 else OPEN
            else:
                raise RuntimeError("Unexpected magic condition %r" % (pos))
        self.grid = self.changed_grid
        self.changed_grid = {}

    def print_it(self):
        for y in range(0, self.size):
            print(" ".join([self.grid[(x, y)] for x in range(0, self.size)]), y)
        print()
        print()

    def count(self, v):
        return len([1 for pos in self.loop if self.grid[pos] == v])


def solve(data):
    grid = Grid(len(data))
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            grid.set((x, y), v)
    previous = 0
    scores = []
    for i in range(1000):
        grid.magic()
        # keep track of the score and the differences
        s = grid.count(TREE) * grid.count(LUMBER)
        d = s - previous
        previous = s
        scores.append((s, d))
        # print(i, s, s - previous)
    # part1
    a1 = scores[9][0]
    # part 2
    w = Counter(scores)
    # check for a pattern with the most_common duplicate
    most = w.most_common(1)[0]
    # for safety we want at least 10 times the same
    if most[1] < 10:
        a2 = 'Didnt find enough most_common %s' % str(w.most_common(10))
    else:
        # find the gaps
        m = most[0]
        # find m backwards and keep track of the locations
        i_list = [i for i in range(len(scores) - 1, 0, -1) if scores[i] == m]
        # is the gap between the locations the same, for at least the last 10 times
        gap_list = [i_list[i] - i_list[i + 1] for i in range(0, len(i_list) - 1)]
        if len(gap_list) > 10 and [gap_list[0]] * 10 == gap_list[0:10]:
            # winner
            gap = gap_list[0]
            last_i = i_list[0]
            rest = (1000000000 - last_i) % gap
            a2 = scores[last_i - 28 + rest - 1][0]
        else:
            a2 = "Did not find enough matchins gaps %r" % gap_list
    return [a1, a2]


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
