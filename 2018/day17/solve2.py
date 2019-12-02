#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "---  ---"

CLAY, SAND, WATER, FLOW = '#', '.', '~', '|'
DOWN, LEFT, RIGHT, UP = range(1, 5)
SOURCE = (500, 0)
DIRECTION = {
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0),
    UP: (0, -1),
}
DEBUG = False


class Ground(object):
    def __init__(self):
        self.gmap = {}
        self.xmin, self.xmax, self.ymin, self.ymax = [None] * 4

    def set(self, pos, v):
        self.gmap[pos] = v
        (x, y) = pos
        if v == CLAY:
            self.xmin = x if self.xmin is None or x < self.xmin else self.xmin
            self.xmax = x if self.xmax is None or x > self.xmax else self.xmax
            self.ymin = y if self.ymin is None or y < self.ymin else self.ymin
            self.ymax = y if self.ymax is None or y > self.ymax else self.ymax

    def v(self, pos):
        return self.gmap[pos] if pos in self.gmap else SAND

    def mark_water(self, pos):
        # go left till we hit clay
        pos_list = []
        for dx in [-1, 1]:
            x, y = pos
            while self.v((x, y)) != CLAY:
                if (x, y) not in self.gmap:
                    raise RuntimeError("mark_water: (%d, %d) should be in map" % (x, y))
                if self.gmap[(x, y)] not in [FLOW, WATER]:
                    raise RuntimeError("mark_water: (%d, %d) should be in water or flow (%d)" % (x, y, self.map[(x, y)]))
                pos_list.append((x, y))
                x += dx
        for pos in pos_list:
            self.gmap[pos] = WATER

    def line_complete(self, pos):
        for dx in [-1, 1]:
            x, y = pos
            # go until we hit clay or the flow falls down
            while True:
                if self.v((x, y)) == CLAY:
                    break
                if self.v((x, y)) == FLOW and self.v((x, y + 1)) == FLOW:
                    break
                if self.v((x, y)) in [WATER, SAND]:
                    return False
                x += dx
        return True

    def print_map(self, start=1, end=0):
        line = 0
        for y in range(self.ymin - 1, self.ymax + 1):
            line += 1
            row = ''
            for x in range(self.xmin - 1, self.xmax + 1):
                row += self.v((x, y))
            if line >= start:
                print(row, y)
            if line == end:
                break
        print()

    def count_v(self, v):
        return len([1 for y in range(self.ymin, self.ymax + 1) for x in range(self.xmin, self.xmax + 1) if (x, y) in self.gmap and self.gmap[(x, y)] in v])


class Flow(object):
    def __init__(self, pos, direction, parent=False):
        self.pos = pos
        self.direction = direction
        self.x, self.y = self.pos
        self.parent = parent
        self.pause = False
        self.children = []
        if parent is not False:
            parent.children.append(self)

    def stop(self):
        if self.parent:  # if we have a parent
            # print([(c.pos, c.direction) for c in self.parent.children])
            self.parent.children.remove(self)  # remove ourself from the parent childs list

    def move(self, direction=None):
        self.pos = self.next_pos(direction)
        self.x, self.y = self.pos
        return self

    def next_pos(self, direction=None):
        if direction is None:
            direction = self.direction
        return (self.x + DIRECTION[direction][0], self.y + DIRECTION[direction][1])

    def __str__(self):
        children = [(c.pos, c.direction) for c in self.children]
        parent = self.parent if self.parent is False else (self.parent.pos, self.parent.direction, len(self.parent.children))
        return 'pos: %r,  direction: %d,  pause: %r,  parent: %r,  children: %r' % (self.pos, self.direction, self.pause, parent, children)


def solve(data):
    ground = Ground()
    yymax = 0
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
    flows = [Flow((500, ground.ymin - 1), DOWN)]  # list of water flows
    # for tel in range(100):
    flowing = 0
    while len(flows) > 0:  # as long as there is a flow
        flows2 = []
        for flow in flows:
            # mark the flow
            ground.set(flow.pos, FLOW)
            next_pos = flow.next_pos()  # next position
            v = ground.v(next_pos)  # what do we find on the next position
            flow_pause = False
            if DEBUG:
                print(next_pos, v, flow)
            # if the flow goes offscreen, stop following it
            if flow.y > ground.ymax:
                if DEBUG:
                    print("  --> off screen")
                continue
            # let the water flow
            if flow.direction in [LEFT, RIGHT]:
                if v in [CLAY, FLOW, WATER]:
                    flow.stop()
                    # if we dont have children left, we can mark the water
                    fp = flow.parent
                    if len(fp.children) == 0:
                        try:
                            ground.mark_water(fp.pos)
                        except RuntimeError:
                            flow_pause = True
                            # we still have to wait for another flow
                        fp.move(UP)
                        if DEBUG:
                            print("  ", flow.direction, "--> parent ", fp)
                        while fp.parent and len(fp.children) == 0 and fp.y == fp.parent.y:
                            # if we go to parent, check if we have unfished business left or RIGHT
                            if ground.v(fp.next_pos(LEFT)) == SAND:
                                fp.direction = LEFT
                                break
                            if ground.v(fp.next_pos(RIGHT)) == SAND:
                                fp.direction = RIGHT
                                break
                            fp.close()
                            fp = fp.parent
                            if DEBUG:
                                print("  parent --> parent ", fp)
                        fp.pause = flow_pause
                        flows2 += [fp]
                elif v in [SAND]:
                    flow.move()
                    pos = flow.next_pos(DOWN)
                    if ground.v(pos) == SAND:
                        flow.direction = DOWN
                    flows2 += [flow]
                    if DEBUG:
                        print("  move ", flow.direction)
                else:
                    raise RuntimeError("Left, right unforseen condition (%s)" % str(flow))
            elif flow.direction == DOWN:
                if flow.pause and v == FLOW:  # wait until line beneath us is complete
                    flows2 += [flow]
                    continue
                else:
                    flow.pause = False
                if v in [CLAY, WATER]:  # flow splits in 2 flows
                    fl = Flow(flow.pos, LEFT, parent=flow)
                    fr = Flow(flow.pos, RIGHT, parent=flow)
                    if DEBUG:
                        print('  fork left ', fl)
                        print('  fork right', fr)
                    flows2 += [fl, fr]
                elif v in [SAND]:
                    flow.move()
                    flows2 += [flow]
                    if DEBUG:
                        print("  move ", flow.direction)
                elif v in [FLOW]:
                    # we have reached another flow, so pause it until line is complete
                    flow.pause = True
                    flows2 += [flow]
                else:
                    raise RuntimeError("DOWN unforseen condition (%s)" % str(flow))
        flows = flows2
        flowing += 1
        if len(flows) > 0:
            yymax = max([f.y for f in flows] + [yymax])
            if flowing % 1000 == 1:
                a1 = ground.count_v([WATER, FLOW])
            print(ground.ymax, yymax, len(flows), flowing, a1)
            if flowing < 2000:
                ground.print_map(yymax - 60, yymax + 5)
        # else:
        #     ground.print_map()

    ground.print_map()
    a1 = ground.count_v([WATER, FLOW])
    return [a1, 'a']


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input_test.txt', 'r')
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))

# 263023 too high
# 33490 too low
# part1 33610
# part2 25669

if __name__ == '__main__':
    main()
