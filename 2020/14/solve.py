#!/usr/bin/python3
# import itertools
# import functools
# import re
# from collections import Counter
# from collections import defaultdict

day = "--- Day 14 - 2020 ---"


def split_mask(mask):
    mask_and = 0
    mask_or = 0
    for b in mask:
        mask_and <<= 1
        mask_or <<= 1
        if b == 'X':
            mask_and += 1
        elif b == '1':
            mask_and += 1
            mask_or += 1
    return mask_and, mask_or


def get_addresses(mask):
    masks = [0]
    for b in mask:
        new_masks = []
        for m in masks:
            m <<= 1
            if b == 'X':
                new_masks.append(m)
                new_masks.append(m + 1)
            elif b == '1':
                new_masks.append(m + 1)
            else:
                new_masks.append(m)
        masks = new_masks
    return masks


def n2bits(n, bitsize):
    b = ""
    for i in range(bitsize):
        x = pow(2, i)
        if x == x & n:
            b = "1" + b
        else:
            b = "0" + b
    return b


def addr_mask(mask, addr):
    addr = n2bits(addr, len(mask))  # transform addr to bitstring
    addr_mask = ""
    for i, b in enumerate(mask):
        if b in "X1":
            addr_mask += b
        else:
            addr_mask += addr[i]
    return addr_mask


def part1(d):
    mem = {}
    mask_and = 0
    mask_or = 0
    for i, v in d:
        if i == "mask":
            mask_and, mask_or = split_mask(v)
        else:
            mem[int(i[4:-1])] = int(v) & mask_and | mask_or
    return sum(mem.values())


def part2(d):
    mem = {}
    mask = ""
    for i, v in d:
        if i == "mask":
            mask = v
        else:
            a_mask = addr_mask(mask, int(i[4:-1]))
            for a in get_addresses(a_mask):
                mem[a] = int(v)
    return sum(mem.values())


def solve1(data):
    return part1(data)


def solve2(data):
    return part2(data)


def solve(data):
    a1 = solve1(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    a2 = solve2(data.copy())
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip().split(" = ") for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
