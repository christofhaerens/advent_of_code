#!/usr/bin/python3

# --- Day 8: I Heard You Like Registers ---

import re


def part_1_2(data):
    # strp !
    m = re.sub(r'!.', '', data)
    level = 0
    sum = 0
    g_sum = 0
    garbage = False
    for c in m:
        if garbage and c != '>':
            g_sum += 1
        elif c == '>':
            garbage = False
        elif c == '<':
            garbage = True
        elif c == '{':
            level += 1
        elif c == '}':
            sum += level
            level = level - 1 if level > 0 else 0
    return sum, g_sum


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    fh.close()
    # assert part1 = 11938  part2 = 6285
    # print("part1 = %s" % part_1(data))
    print("part1 = %s\npart2 = %s" % part_1_2(data))


if __name__ == '__main__':
    main()
