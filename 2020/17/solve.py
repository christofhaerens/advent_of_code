#!/usr/bin/python3
import itertools
# import functools
# import re
# from collections import Counter
from collections import defaultdict

day = "--- Day 17 - 2020 ---"


class Pocket(object):
    def __init__(self, data, dim):
        self.dim = dim  # no of dimensions
        self.grid = defaultdict(int)
        other = tuple((0 for _ in range(dim - 2)))
        for y, row in enumerate(data):
            for x, p in enumerate(row):
                if p == '#':
                    c = (x, y) + other
                    self.grid[c] = 1
        self.neighbours = list(itertools.product((-1, 0, 1), repeat=dim))
        self.neighbours.remove(tuple((0 for _ in range(dim))))

    def count(self):
        return len(self.grid.values())

    def get_neighbours(self, p):
        return [tuple((a + b) for a, b in zip(p, n)) for n in self.neighbours]

    def neighbour_count(self, p):
        return sum([self.grid[n] for n in self.get_neighbours(p)])

    def cycle(self):
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        newgrid = defaultdict(int)
        # considering the rules we only need the check the neighbours of the actives
        checked = set()
        active_points = tuple(self.grid.keys())
        for point in active_points:
            for n in self.get_neighbours(point):
                if n not in checked:
                    checked.add(n)
                    c = self.neighbour_count(n)
                    if (self.grid[n] == 1 and c in [2, 3]) or (self.grid[n] == 0 and c == 3):
                        newgrid[n] = 1
        self.grid = newgrid


def solve1(data):
    pocket = Pocket(data, 3)
    for _ in range(6):
        pocket.cycle()
    return pocket.count()


def solve2(data):
    pocket = Pocket(data, 4)
    for _ in range(6):
        pocket.cycle()
    return pocket.count()


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
