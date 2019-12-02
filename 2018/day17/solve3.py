#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque


day = "---  ---"

CLAY, SAND, WATER, FLOW = '#', '.', '~', '|'
SOURCE = (500, 0)
# up, up_right, right, down_right, ...
UP, UR, RI, DR, DO, DL, LE, UL = (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)


def new_pos(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])


class Grid(object):
    def __init__(self):
        self.grid = {}
        self.xmin, self.xmax, self.ymin, self.ymax = [None] * 4

    def set(self, pos, v):
        self.grid[pos] = v
        (x, y) = pos
        if v == CLAY:
            self.xmin = x if self.xmin is None or x < self.xmin else self.xmin
            self.xmax = x if self.xmax is None or x > self.xmax else self.xmax
            self.ymin = y if self.ymin is None or y < self.ymin else self.ymin
            self.ymax = y if self.ymax is None or y > self.ymax else self.ymax

    def v(self, pos):
        return self.grid[pos] if pos in self.grid else SAND

    def mark_water(self, pos):
        # go left and riht till we hit clay
        for dx in [LE, RI]:
            p = pos
            while self.v(p) != CLAY:
                if self.v(p) not in [FLOW, WATER]:
                    raise RuntimeError("mark_water: (%r) should be in water or flow (%d)" % (pos, self.map[pos]))
                self.grid[p] = WATER
                p = new_pos(p, dx)

    def print_grid(self, start=1, lines=0):
        l = 0
        for y in range(self.ymin - 1, self.ymax + 1):
            l += 1
            if l >= start:
                print(''.join([self.v((x, y)) for x in range(self.xmin - 1, self.xmax + 1)]), y)
            if l == lines:
                break
        print()

    def count_v(self, v):
        return len([1 for y in range(self.ymin, self.ymax + 1) for x in range(self.xmin - 1, self.xmax + 2) if (x, y) in self.grid and self.grid[(x, y)] in v])


def solve(data):
    ground = Grid()
    for d in data:
        m = re.match(r'(.)=(\d+),\s+.=(\d+)\.\.(\d+)', d)
        if m:
            a, v1, v2, v3 = m.groups()
            for v4 in range(int(v2), int(v3) + 1):
                x, y = (int(v1), v4) if a == 'x' else (v4, int(v1))
                ground.set((x, y), CLAY)
        else:
            raise RuntimeError('Unmatched input %s' % d)
    # init water flows
    flows = deque([SOURCE])
    while len(flows) > 0:  # as long as there is a flow
        p = flows.popleft()
        while ground.v(p) == SAND and p[1] <= ground.ymax:
            ground.set(p, FLOW)
            p = new_pos(p, DO)  # move down
        if p[1] > ground.ymax:  # stop flow beneath our grid
            continue
        if ground.v(p) in [FLOW]:  # stop this flow
            continue
        p = new_pos(p, UP)
        # fill up the bucket
        edge = False
        pos = p
        while not edge:
            for dx in [LE, RI]:
                p = pos
                while ground.v(p) not in [CLAY]:
                    ground.set(p, FLOW)
                    if ground.v(new_pos(p, DO)) in [SAND, FLOW]:  # edge reached
                        edge = True
                        flows.append(new_pos(p, DO))
                        break
                    p = new_pos(p, dx)
            # if both sides are filled, mark the water and move up
            if not edge:
                ground.mark_water(pos)
            pos = new_pos(pos, UP)
        # ground.print_grid(p[1] - 50, 50)

    ground.print_grid()

    a1 = ground.count_v([WATER, FLOW])
    a2 = ground.count_v([WATER])
    return [a1, a2]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    # fh = open('./input_test.txt', 'r')
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))

# 263023 too high 33598
# 33490 too low
# part1 33610  33598 x   33597 x  33490 x
# part2 25669


if __name__ == '__main__':
    main()
