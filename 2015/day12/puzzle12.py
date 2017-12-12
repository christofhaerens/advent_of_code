#!/usr/bin/python3

# --- Day 12: JSAbacusFramework.io ---

import re
import json


def part_1(data):
    sum = 0
    # remove al non digits
    for x in re.sub(r'[^\d-]', ' ', data).split():
        sum += int(x)
    return sum


def sum_in_values(v):
    sum = 0
    if isinstance(v, dict):
        v = list(v.values())
        if 'red' in v:
            return 0
    for el in v:
        if isinstance(el, int):
            sum += el
        elif isinstance(el, list) or isinstance(el, dict):
            sum += sum_in_values(el)
    return sum


def part_2(data):
    v = json.loads(data)
    return sum_in_values(v)


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    # data = 'zx'
    fh.close()
    # assert part1 = 191164   part2 = 87842
    print("part1 = %d" % part_1(data))
    print("part2 = %d" % part_2(data))


if __name__ == '__main__':
    main()
