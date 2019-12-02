#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "---  ---"

CLAY, SAMD, WATER, FLOW = '#', '.', '~', '|'
DOWN, LEFT, RIGHT, UP = range(1, 5)
SOURCE = (500, 0)
DIRECTION = {
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0),
    UP: (0, -1),
}


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
        return self.gmap[pos] if pos in self.gmap else '.'

    def mark_water(self, pos):
        # go left till we hit clay
        pos_list = []
        for dx in [-1, 1]:
            x, y = pos
            while self.v((x, y)) != CLAY:
                if (x, y) not in self.gmap:
                    # raise RuntimeError("mark_water: (%d, %d) should be in map" % (x, y))
                    return  # line is not complete yet
                if self.gmap[(x, y)] not in [FLOW, WATER]:
                    raise RuntimeError("mark_water: (%d, %d) should be in water or flow (%d)" % (x, y, self.map[(x, y)]))
                pos_list.append((x, y))
                x += dx
        for pos in pos_list:
            self.gmap[pos] = WATER

    def print_map(self, start=1, end=0):
        print()
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
        self.__set_xy_from_pos__()
        self.parent = parent
        self.children = []
        if parent is not False:
            parent.children.append(self)

    def stop(self):
        if self.parent:  # if we have a parent
            # print([(c.pos, c.direction) for c in self.parent.children])
            self.parent.children.remove(self)  # remove ourself from the parent childs list
        return len(self.parent.children)  # return how many other children are left

    def __set_pos_from_xy__(self):
        self.pos = (self.x, self.y)

    def __set_xy_from_pos__(self):
        self.x = self.pos[0]
        self.y = self.pos[1]

    def move(self, direction=None):
        self.pos = self.next_pos(direction)
        self.__set_xy_from_pos__()
        return self

    def next_pos(self, direction=None):
        if direction is None:
            direction = self.direction
        return (self.x + DIRECTION[direction][0], self.y + DIRECTION[direction][1])

    def __str__(self):
        children = [(c.pos, c.direction) for c in self.children]
        parent = self.parent if self.parent is False else (self.parent.pos, self.parent.direction, len(self.parent.children))
        return 'pos: %r,  direction: %d,  parent: %r,  children: %r' % (self.pos, self.direction, parent, children)


def solve(data):
    ground = Ground()
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
    while len(flows) > 0:  # as long as there is a flow
        flows2 = []
        for flow in flows:
            # mark the flow
            ground.set(flow.pos, FLOW)
            next_pos = flow.next_pos()  # next position
            print(next_pos, flow)
            # if the next_pos would bring us below the lowest point, stop the flow
            if next_pos[1] > ground.ymax:
                continue
            # if we have a parent and we are higher the our parent, stop and switch to the parent
            if flow.parent and flow.y < flow.parent.y:
                if flow.stop() == 0:
                    ground.mark_water(flow.parent.pos)
                    flows2.append(flow.parent.move(UP))
                    continue
            if flow.direction == DOWN:
                if ground.v(next_pos) in [WATER, CLAY]:  # create child flows that go left and right
                    flows2.append(Flow(flow.pos, LEFT, parent=flow))
                    flows2.append(Flow(flow.pos, RIGHT, parent=flow))
                else:  # keep going down
                    flows2.append(flow.move())
            elif flow.direction in [LEFT, RIGHT]:
                if ground.v(next_pos) in [CLAY, WATER, FLOW]:
                    # stop this flow and if no children left, mark as water and switch back to parent a position higher
                    if flow.stop() == 0:  # all children are gone, move the parent up and continue with the parent
                        if flow.parent:
                            ground.mark_water(flow.parent.pos)
                            flows2.append(flow.parent.move(UP))
                else:  # move sideways or drop down
                    pos_down1 = flow.next_pos(DOWN)
                    flow.move()  # move sideways
                    pos_down2 = flow.next_pos(DOWN)
                    print("Move sideways")
                    # if no clay beneath us and there is clay beneath us one step back, go down
                    if ground.v(pos_down1) == CLAY and ground.v(pos_down2) not in [CLAY]:  # if we can go down, switch direction
                        if ground.v(pos_down2) in [FLOW, WATER]:  # we have hit another flow, stop the current
                            flow.stop()
                        else:
                            flow.direction = DOWN
                            print("Change direction DOWN")
                            flows2.append(flow)
                    else:
                        flows2.append(flow)

        flows = flows2
        if len(flows) > 0:
            yymin = min([f.y for f in flows]) - 20
            yymax = max([f.y for f in flows]) + 20
            ground.print_map(yymin, yymax)
        else:
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


if __name__ == '__main__':
    main()
