#!/usr/bin/python3

from collections import defaultdict

day = "--- Day 3 - 2019 ---"


def map_wires(data):
    wires = ['A', 'B']
    grid = defaultdict(lambda: '.')
    pos_steps = {}
    crossings = []
    crossing_steps = []
    for id, wire in enumerate(wires):
        pos = (0, 0)
        pos_steps[id] = defaultdict(int)
        stepstaken = 0
        for path in data[id]:
            positions = []
            direction, steps = path[0], int(path[1:])
            if direction == 'R':
                for i in range(pos[0] + 1, pos[0] + steps + 1):
                    positions.append((i, pos[1]))
            elif direction == 'L':
                for i in range(pos[0] - 1, pos[0] - steps - 1, -1):
                    positions.append((i, pos[1]))
            elif direction == 'U':
                for i in range(pos[1] + 1, pos[1] + steps + 1):
                    positions.append((pos[0], i))
            elif direction == 'D':
                for i in range(pos[1] - 1, pos[1] - steps - 1, -1):
                    positions.append((pos[0], i))
            for pos in positions:
                stepstaken += 1
                if grid[pos] == '.':  # no wire passed by
                    grid[pos] = wire
                    pos_steps[id][pos] = stepstaken
                elif grid[pos] != 'x' and grid[pos] != wire:  # not already crossed and not ourself
                    grid[pos] = 'x'
                    crossings.append(abs(pos[0]) + abs(pos[1]))
                    crossing_steps.append(stepstaken + pos_steps[0][pos])
    return (min(crossings), min(crossing_steps))


def solve1(data):
    return map_wires(data)


def solve2(data):
    return 1


def solve(data):
    print("\n%s" % day)
    a = solve1(data)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test2.txt', 'r')
    data = [line.strip().split(',') for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
