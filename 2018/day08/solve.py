#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 8: Memory Maneuver ---"


def find_nodes(n, metadata, pos):
    children, meta = n[pos:pos + 2]
    if children == 0:
        metadata += n[pos + 2:pos + 2 + meta]
        return (metadata, pos + meta)
    for c in range(0, children):
        metadata, pos = find_nodes(n, metadata, pos + 2)
    metadata += n[pos + 2:pos + 2 + meta]
    return (metadata, pos + meta)


def find_nodes2(n, metadata, pos):
    children, meta = n[pos:pos + 2]
    if children == 0:
        metadata = n[pos + 2:pos + 2 + meta]
        value = sum(metadata)
        return (value, metadata, pos + meta)
    values_children = {}
    for c in range(1, children + 1):
        values_children[c], metadata, pos = find_nodes2(n, metadata, pos + 2)
    value = 0
    metadata = n[pos + 2:pos + 2 + meta]
    for m in metadata:
        if m in values_children:
            value += values_children[m]
    return (value, metadata, pos + meta)


def solve(data):
    # data = ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2']
    nodes = list(map(int, data[0].split(' ')))
    # part1
    metadata, pos = find_nodes(nodes, [], 0)
    a1 = sum(metadata)
    # part2
    a2, metadata, pos = find_nodes2(nodes, [], 0)
    return [a1, a2]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
