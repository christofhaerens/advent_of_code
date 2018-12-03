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
    chars = []
    for idx, val in enumerate(w1):
        if w2[idx] != val:
            chars.append(idx)
    return len(chars), chars[0]


def solve2(data):
    data2 = data.copy()
    l = len(data)
    for idx, val in enumerate(data):
        i = idx + 1
        while i < l:
            d, char_idx = difference(val, data2[i])
            if d == 1:
                break
            i += 1
        if d == 1:
            break
    return data[i][0:char_idx] + data[i][(char_idx + 1):]


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
