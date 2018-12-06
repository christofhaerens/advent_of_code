#!/usr/bin/python3

import re
from collections import defaultdict

day = "--- Day 3: No Matter How You Slice It ---"


def solve(data):
    fabric = defaultdict(lambda: [])
    dupes = 0
    dup_cids = {}
    cids = []
    for d in data:
        #  #1 @ 35,93: 11x13
        m = re.match(r'^#\s*(\d+)\s*@\s*(\d+)\s*,\s*(\d+)\s*:\s*(\d+)\s*x\s*(\d+)\s*', d)
        cid, left, top, w, h = [int(v) for v in m.groups()]
        cids.append(cid)
        # mark positions
        for x in range(left + 1, left + 1 + w):
            for y in range(top + 1, top + 1 + h):
                pos = '%d:%d' % (x, y)
                fabric[pos].append(cid)
    # check if multiple cids have claimed the fabric pos
    for pos_cids in fabric.values():
        if len(pos_cids) > 1:
            dupes += 1
            for cid in pos_cids:
                dup_cids[cid] = True
    # check if a cid has only claimed singe positions
    for cid in cids:
        if cid not in dup_cids.keys():
            return [dupes, cid]
    raise RuntimeError('No claim ID found that does not overlap wit another')


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
