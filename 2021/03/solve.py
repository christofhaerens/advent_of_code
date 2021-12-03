#!/usr/bin/python3
from collections import defaultdict

day = "--- Day 3 - 2021 ---"


def solve1(data):
    zerobits = defaultdict(lambda: 0)
    bitcount = len(data[0])
    for byte in data:
        for idx in range(bitcount):
            # we only count zero bits
            if byte[idx] == "0":
                zerobits[idx] += 1
    # if we have more zeros then half of total
    max_occurences = len(data)
    gamma = ""
    epsilon = ""
    for i in range(bitcount):
        # if zero count is bigger then half of max, dominant is a "0" otherwise a "1"
        if zerobits[i] * 2 > max_occurences:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)


def solve2(data):
    bitcount = len(data[0])
    life_support_rating = 1
    for rating in range(2):  # 0 for CO2 en 1 for O2
        bytes = data.copy()
        for idx in range(bitcount):
            bytes_with = [[], []]
            for byte in bytes:
                if byte[idx] == '0':
                    bytes_with[0].append(byte)
                else:
                    bytes_with[1].append(byte)
            c0 = len(bytes_with[0])
            c1 = len(bytes_with[1])
            if c0 == c1:
                bytes = bytes_with[rating]
            elif c0 > c1:
                bytes = bytes_with[abs(rating - 1)]
            else:
                bytes = bytes_with[rating]
            if len(bytes) == 1:
                life_support_rating *= int(bytes[0], 2)
                continue
    return life_support_rating


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    data = []
    with open('./input.txt', 'r') as fh:
        data = [line.strip() for line in fh]
    solve(data)


if __name__ == '__main__':
    main()
