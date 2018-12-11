#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 11: Chronal Charge ---"


class Cell(object):
    def __init__(self, x, y, serial):
        self.x = x
        self.y = y
        self.serial = serial
        self.rackid = x + 10
        self.power = (((((self.rackid * y) + serial) * self.rackid) // 100) % 10) - 5

    def __str__(self):
        return '(%d, %d) = %d' % (self.x, self.y, self.power)


def solve(data):
    # data = 18
    grid = {}
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = Cell(x, y, data)
    # calculate squares
    squares = defaultdict(int)
    squares2 = defaultdict(int)  # part 2
    for x in range(1, 301 - 3):
        for y in range(1, 301 - 3):
            for dx in range(0, 3):
                for dy in range(0, 3):
                    squares[(x, y)] += grid[(x + dx, y + dy)].power
                    squares2[(x, y, 3)] += grid[(x + dx, y + dy)].power
    w = Counter(squares)
    a1, power = w.most_common(1)[0]
    # for part2 we assume we can start from the 3x3
    # safety: max power value per cell = 9 - 5 = 4
    #         max power for 2x2 square = 4cells * 4 = 16
    #         so if the power value of our 3x3 is larger then the maxvalue of a lower square, our assumption is ok
    if power < 16:
        raise RuntimeError("Error: possible wrong assumption")
    # now calculate larger squares sizes (s)
    for s in range(4, 300):
        for x in range(1, 301 - s):
            for y in range(1, 301 - s):
                # the total power of the square is the power of the smaller square with the sum of it's edges (a->e)
                # x x  ->  x x a
                # x x  ->  x x b
                #      ->  c d e
                squares2[(x, y, s)] = squares2[(x, y, s - 1)]
                for ds in range(0, s - 1):
                    # add a, b
                    squares2[(x, y, s)] += grid[(x + s - 1, y + ds)].power
                    # add c, d
                    squares2[(x, y, s)] += grid[(x + ds, y + s - 1)].power
                # add e
                squares2[(x, y, s)] += grid[(x + s - 1, y + s - 1)].power
    w = Counter(squares2)
    a2, power = w.most_common(1)[0]
    return [",".join(map(str, a1)), ",".join(map(str, a2))]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(int(data[0])))


if __name__ == '__main__':
    main()
