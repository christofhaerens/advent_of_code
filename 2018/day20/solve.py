#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque
from operator import itemgetter


day = "---  ---"

directions = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

DOORH, DOORV, WALL, ROOM, UNK = '-', '|', '#', '.', '?'
DOORS = (DOORH, DOORV)


class Grid(object):
    def __init__(self):
        self.pos = (0, 0)
        self.xx = [0, 0]
        self.yy = [0, 0]
        self.grid = {}
        self.start = self.pos
        self.grid[self.pos] = ROOM

    def get(self, pos):
        return UNK if pos not in self.grid else self.grid[pos]

    def get_print(self, pos):
        v = self.get(pos)
        v = 'P' if pos == self.pos else v
        v = 'X' if pos == self.start else v
        return v

    def set(self, pos, v):
        self.grid[pos] = v
        x, y = pos
        self.xx[0] = x if x < self.xx[0] else self.xx[0]
        self.xx[1] = x if x > self.xx[1] else self.xx[1]
        self.yy[0] = y if y < self.yy[0] else self.yy[0]
        self.yy[1] = y if y > self.yy[1] else self.yy[1]

    def np(self, pos, dx):
        return (pos[0] + dx[0], pos[1] + dx[1])

    def move(self, d):
        dx = directions[d]
        self.pos = self.np(self.pos, dx)
        door = DOORH if d in 'NS' else DOORV
        self.set(self.pos, door)
        self.pos = self.np(self.pos, dx)
        self.set(self.pos, ROOM)

    def print_grid(self):
        for y in range(self.yy[0] - 1, self.yy[1] + 2):
            print("".join([self.get_print((x, y)) for x in range(self.xx[0] - 1, self.xx[1] + 2)]), y)
        print()

    def set_walls(self):
        for y in range(self.yy[0] - 1, self.yy[1] + 2):
            for x in range(self.xx[0] - 1, self.xx[1] + 2):
                if self.get((x, y)) == UNK:
                    self.grid[(x, y)] = WALL

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def is_reachable(self, pos):
        return False if self.get(pos) in [WALL, UNK] else True

    def get_rooms(self):
        return [(x, y) for y in range(self.yy[0], self.yy[1] + 1) for x in range(self.xx[0], self.xx[1] + 1) if self.get((x, y)) == ROOM]

    def reachable_neighbours(self, pos):
        return [self.np(pos, dx) for dx in directions.values() if self.is_reachable(self.np(pos, dx))]


grid = Grid()


# ^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$
def follow_route(route, pos):
    s = route.popleft()
    while True:
        if s == '^':
            s = route.popleft()
            continue
        elif s in 'NESW':
            grid.move(s)
            s = route.popleft()
        elif s in '(':
            pos_jump = grid.pos  # save our pos before we jump
            route = follow_route(route, pos_jump)
            grid.pos = pos_jump  # restore our pos
            s = route.popleft()
        elif s in '|':
            grid.pos = pos
            s = route.popleft()
        elif s in ')':
            return route
        elif s in '$':
            return route


def find_shortest(grid, start, end):
    # use A* algorithm
    g, h = {}, {}
    g[start] = 0
    h[start] = grid.distance(start, end) * 10
    ol = [(h[start], start)]  # open list of (f, pos) elements
    cl = []  # closed list
    parent = {}
    found = False
    while len(ol) > 0:  # while we still have move options
        # sort the list based on the f-score
        ol.sort(key=itemgetter(0), reverse=True)
        f, pos = ol.pop()
        cl.append(pos)
        if pos == end:
            found = True
            break
        rnbs = grid.reachable_neighbours(pos)
        for neighbour in rnbs:  # calculate f score for each neighbour and add them to the list
            if neighbour in cl:
                continue
            g[neighbour] = g[pos] + 10
            h[neighbour] = grid.distance(neighbour, end) * 10
            f = g[neighbour] + h[neighbour]
            # check if neighbour is already in the open list
            in_list = False
            for i, n in enumerate(ol):
                # if our score is lower then the one in the open list -> replace
                if n[1] == neighbour and n[0] > f:
                    ol[i] = (f, neighbour)
                    parent[neighbour] = pos
                    in_list = True
                    break
            if not in_list:
                ol.append((f, neighbour))
                parent[neighbour] = pos
    doors = {}
    if found:
        path = []
        # path from end to begin
        door_cnt = 0
        while end != start:
            path.append(end)
            end = parent[end]
        path.append(grid.start)
        path.reverse()
        # now we have the path from begin to end
        door_cnt = 0
        for p in path:
            if grid.get(p) in DOORS:
                door_cnt += 1
            if grid.get(p) == ROOM:
                doors[p] = door_cnt
    return doors


def solve(data):
    route = deque()
    for r in data[0]:
        route.append(r)
    follow_route(route, (0, 0))
    grid.set_walls()
    grid.print_grid()
    # now use a A* search for the shortest path to each reachable point
    doors = {}
    rooms = grid.get_rooms()
    for room in rooms:
        # check if we already have the info for this doors
        if room not in doors and room != grid.start:
            print(room)
            d = find_shortest(grid, grid.start, room)
            for k, v in d.items():
                doors[k] = v
    a1 = max(doors.values())
    a2 = sum([1 for v in doors.values() if v > 999])

    return [a1, a2]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    # fh = open('./input_test2.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
