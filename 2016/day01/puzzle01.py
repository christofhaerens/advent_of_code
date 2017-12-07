#!/usr/bin/python3

# --- Day 1: No Time for a Taxicab ---

import re


def part_1_2(data):
    N, E, S, W = 0, 1, 2, 3
    x, y = 0, 0
    visited = [[x, y]]
    visited_distance = None
    d = N
    for step in data:
        m = re.match('^([LR])(\d+)', step)
        direction = m.group(1)
        distance = int(m.group(2))
        d = (d + 1) % 4 if direction == 'R' else (d - 1 + 4) % 4
        # go step by step so we can record all visited locations
        for s in range(distance):
            if d == N:
                y += 1
            elif d == S:
                y -= 1
            elif d == E:
                x += 1
            elif d == W:
                x -= 1
            if not visited_distance and [x, y] in visited:
                visited_distance = abs(x) + abs(y)
            else:
                visited.append([x, y])
    # traveled distance from start (0,0)
    return abs(x) + abs(y), visited_distance


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    fh.close()
    # testdata = 'R5, L5, R5, R3'
    # assert part1 = 271, part2 = 153
    print("part1 = %s\npart2 = %s" % part_1_2(data.split(', ')))


if __name__ == '__main__':
    main()
