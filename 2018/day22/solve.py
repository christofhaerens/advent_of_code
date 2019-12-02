#!/usr/bin/python3

import re
from collections import defaultdict, Counter
from operator import itemgetter


day = "---  ---"

ROCKY, WET, NARROW = range(3)
CLIMB, TORCH, NEITHER = TOOLS = range(3)
USAGE = {
    ROCKY: (TORCH, CLIMB),
    WET: (CLIMB, NEITHER),
    NARROW: (TORCH, NEITHER),
}


class Cave(object):
    def __init__(self, depth, target):
        self.region = {}
        self.depth = depth
        self.target = target
        self.xx = 0
        self.yy = 0

    def add_region(self, pos):
        if pos not in self.region:
            self.region[pos] = Region(pos, self)
            self.xx = pos[0] if pos[0] > self.xx else self.xx
            self.yy = pos[1] if pos[1] > self.yy else self.yy
        return self.region[pos].type

    def build_to_target(self):
        risk = 0
        for y in range(self.target[1] + 1):
            for x in range(self.target[0] + 1):
                risk += self.add_region((x, y))
        return risk

    def next_regions(self, pos):
        """ Build the next rows and/or columns """
        x, y = pos
        if x > self.xx or y > self.yy:
            xxstart = self.xx + 1
            yystart = self.yy + 1
            # Build the rows first if needed
            if y > self.yy:
                for yy in range(yystart, y + 1):
                    for xx in range(0, self.xx + 1):
                        self.add_region((xx, yy))
            # Build the columns if needed
            if x > self.xx:
                for yy in range(0, self.yy + 1):
                    for xx in range(xxstart, x + 1):
                        self.add_region((xx, yy))

    def get_neighbours(self, pos):
        """get the neighbours"""
        neighbours = []
        # make sure we have now the neighbour regions
        self.next_regions((pos[0] + 1, pos[1] + 1))
        # find neighbours, first down and right
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            newpos = (pos[0] + d[0], pos[1] + d[1])
            if newpos[0] >= 0 and newpos[1] >= 0 and newpos:
                neighbours.append(self.region[newpos])
        return neighbours

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + (abs(p1[1] - p2[1]))

    def shortest_path(self):
        # start at 0, 0
        pos = (0, 0)
        paths_taken = {}  # keep track of the time travelled to here and the current tool
        time_taken = 0
        distance = 0
        to_follow = [(time_taken, distance, Path(pos, CLIMB)), (time_taken, distance, Path(pos, TORCH))]
        while True:
            # we have to sort on ????
            to_follow.sort(key=itemgetter(0, 1))
            time_taken, distance, path = to_follow.pop()
            # if we have found our target, return
            if path.pos == self.target and path.tool == TORCH:
                print(path.time_taken(), path.steps())
                print(path.trace)
                print("pos: %r   tt: %d   steps: %d   switched: %d" % (path.pos, time_taken, path.steps(), path.tools_switched))
                return path.time_taken()
            # check if we passed this path already
            key = (path.pos, path.tool)
            other_tool = [t for t in USAGE[self.region[path.pos].type] if t != path.tool][0]
            key2 = (path.pos, other_tool)
            if key in paths_taken and time_taken >= paths_taken[key]:
                # did we get slower to this point via our path?
                continue
            # also check if we have been there with a different tool and the time_taken has more then 7 differrence
            if key2 in paths_taken and time_taken >= paths_taken[key2] + 7:
                continue
            # mark we have been here
            paths_taken[key] = time_taken
            print("pos: %r   tt: %d   steps: %d   switched: %d" % (path.pos, time_taken, path.steps(), path.tools_switched))
            # search neighbours for this path
            for nbr in self.get_neighbours(path.pos):  # nbr = neighbour_region
                # check if this region is not in our visited list
                newpaths = []
                if nbr.pos not in path.visited:
                    # if we can use our current tool in the next region, then this is the best option and we dont need to change tools (yet)
                    if path.tool in USAGE[nbr.type]:
                        # we stay on this path
                        newpaths.append(path.fork(nbr.pos, path.tool))
                    else:
                        # we cant use our tool anymore
                        for tool in USAGE[nbr.type]:  # check all tools available
                            # fork our path
                            newpaths.append(path.fork(nbr.pos, tool))
                # check the newpaths if they are our target
                for newpath in newpaths:
                    # if we reached target and the tool is not torch, switch to torch and add 7 min
                    if newpath.pos == self.target and newpath.tool != TORCH:
                        newpath.tool = TORCH
                        newpath.tools_switched += 1
                    to_follow.append((newpath.time_taken(), self.distance(newpath.pos, self.target), newpath))
            # print(len(to_follow))


class Path(object):
    def __init__(self, pos, tool):
        self.pos = pos  # current pos
        self.visited = []
        self.trace = []
        self.tool = tool  # current tool
        self.tools_switched = 0
        self.add_visited()

    def add_visited(self):
        self.visited.append(self.pos)
        self.trace.append((self.pos, self.tool))

    def fork(self, pos, tool):
        new_path = Path(pos, tool)
        new_path.visited = self.visited.copy()
        new_path.trace = self.trace.copy()
        new_path.tools_switched = self.tools_switched + 1 if tool != self.tool else self.tools_switched
        new_path.add_visited()
        return new_path

    def time_taken(self):
        return self.steps() + (self.tools_switched * 7)

    def steps(self):
        return len(self.visited) - 1  # dont count the start point


class Region(object):
    def __init__(self, pos, cave):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        if pos == (0, 0) or pos == cave.target:
            self.geo = 0
        elif self.x == 0:
            self.geo = 48271 * self.y
        elif self.y == 0:
            self.geo = 16807 * self.x
        else:
            self.geo = cave.region[self.x - 1, self.y].erosion * cave.region[self.x, self.y - 1].erosion
        self.erosion = (self.geo + cave.depth) % 20183
        self.type = self.erosion % 3

    def __str__(self):
        return "pos: %r   geo: %d   erosion: %d   type: %d" % (self.pos, self.geo, self.erosion, self.type)

    def __repr__(self):
        return self.__str__()


def solve(data):
    depth = int(data[0][7:])
    target = tuple([int(i) for i in data[1][8:].split(',')])
    cave = Cave(depth, target)
    a1 = cave.build_to_target()
    cave.next_regions((12, 11))
    a2 = cave.shortest_path()
    return [a1, a2]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    fh = open('./input_test.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
