#!/usr/bin/python3

# --- Day 19: A Series of Tubes ---

import re

DOWN, UP, LEFT, RIGHT = range(4)
delta = {DOWN: (0, 1), UP: (0, -1), LEFT: (-1, 0), RIGHT: (1, 0)}


def part_1_2(data):
    steps = 0
    # convert to maze
    maze = {}
    for y, r in enumerate(data):
        for x, c in enumerate(r):
            maze[(x, y)] = c
    # find the start coords
    route = ''
    start_pos = (data[0].index('|'), 0)
    going = DOWN
    pos = start_pos
    while going in delta:
        steps += 1
        last_pos = pos
        pos = (pos[0] + delta[going][0], pos[1] + delta[going][1])
        if maze[pos] == '+':
            # turn
            for d in range(4):
                neighbour = (pos[0] + delta[d][0], pos[1] + delta[d][1])
                if neighbour in maze and neighbour != last_pos:
                    if maze[neighbour] != ' ':
                        going = d
            continue

        if maze[pos] in '|-':
            continue

        if re.match(r'[A-Z]', maze[pos]):
            route += maze[pos]
            continue

        going = -1

    return route, steps


def main():
    fh = open('./input', 'r')
    data = [[c for c in line.strip('\n')] for line in fh]
    fh.close()
    # assert part1 = VEBTPXCHLI   part2 = 18702
    print("part1 = %s\npart2 = %d" % part_1_2(data))


if __name__ == '__main__':
    main()
