#!/usr/bin/python3

import re
from collections import Counter

day = "--- Day 2: Inventory Management System ---"


def solve(data):
    box = {2: 0, 3: 0}
    for box_id in data:
        char_count = Counter(box_id)
        counts = char_count.values()
        for i in [2, 3]:
            if i in counts:
                box[i] += 1
    return [str(box[2] * box[3]), solve2(data)]


def difference(w1, w2):
    """
    Given 2 words, compare them and return an array with the index of the chars that differ
    """
    chars = []
    for idx, val in enumerate(w1):
        if w2[idx] != val:
            chars.append(idx)
    return chars


def solve2(data):
    l = len(data)
    # loop until we have found 2 box ids that have 1 char different
    for idx, val in enumerate(data):
        for i in range(idx + 1, l):
            different_chars = difference(val, data[i])
            if len(different_chars) == 1:
                # return the box_id without the different char
                pos = different_chars[0]
                return val[0:pos] + val[(pos + 1):]
    raise RuntimeError('Error: no boxids found with 1 char different')


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %s" % a[0])
    print("part2 = %s" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
