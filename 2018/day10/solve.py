#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 10: The Stars Align ---"


class Point(object):
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]
        self.vx = p[2]
        self.vy = p[3]

    def move(self, reverse=False):
        if reverse:
            self.x -= self.vx
            self.y -= self.vy
        else:
            self.x += self.vx
            self.y += self.vy


def print_message(points):
    msg = '\n'
    ys = [p.y for p in points]
    ymin = min(ys)
    ymax = max(ys)
    xs = [p.x for p in points]
    xmin = min(xs)
    xmax = max(xs)
    pxy = {}
    for p in points:
        pxy[(p.x, p.y)] = 1
    for y in range(ymin, ymax + 1):
        l = ''
        for x in range(xmin, xmax + 1):
            l += '#' if (x, y) in pxy else '.'
        msg += l + "\n"
    return msg


def solve(data):
    # position=< 10280,  40611> velocity=<-1, -4>
    points = []
    sec = 0  # part2
    for d in data:
        m = re.match(r'position=<\s*([-\d]+),\s*([-\d]+)> velocity=<\s*([-\d]+),\s*([-\d]+)>', d)
        points.append(Point(*[list(map(int, m.groups()))]))
    lowest = 9999999
    while True:
        # move
        [p.move() for p in points]
        # calculate the height; we print the message at lowest height
        ys = [p.x for p in points]
        ymin = min(ys)
        ymax = max(ys)
        height = ymax - ymin
        if height < lowest:
            lowest = height
        else:
            # we have reached the lowest; move 1 back to get back at the lowest and print message
            [p.move(reverse=True) for p in points]
            a1 = print_message(points)
            break
        sec += 1
    return [a1, sec]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %s" % a[0])
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
