#!/usr/bin/python3

# --- Day 1: No Time for a Taxicab ---
# => description at the end of this file

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

# --- Day 1: No Time for a Taxicab ---
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
#
# For example:
#
#     Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
#     R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
#     R5, L5, R5, R3 leaves you 12 blocks away.
#
# How many blocks away is Easter Bunny HQ?
# Your puzzle answer was 271.
# --- Part Two ---
#
# Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?
#
# Your puzzle answer was 153.
