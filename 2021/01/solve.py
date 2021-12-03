#!/usr/bin/python3

day = "--- Day 1 - 2021 ---"


def solve1(data):
    depth = data[0]
    increased = 0
    for d in data[1:]:
        if d > depth:
            increased += 1
        depth = d
    return increased


def solve2(data):
    wsize = 3
    p = 1
    previous_sum = sum(data[:wsize])
    increased = 0
    while p + wsize <= len(data):
        current_sum = sum(data[p:p + wsize])
        if current_sum > previous_sum:
            increased += 1
        p += 1
        previous_sum = current_sum
    return increased


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [int(line.strip()) for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
