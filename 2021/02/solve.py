#!/usr/bin/python3

day = "--- Day 2 - 2021 ---"


def solve1(data):
    hor = 0
    depth = 0
    for d in data:
        step = int(d[1])
        if d[0] == 'forward':
            hor += step
        elif d[0] == 'down':
            depth += step
        elif d[0] == 'up':
            depth -= step
    return hor * depth


def solve2(data):
    hor = 0
    depth = 0
    aim = 0
    for d in data:
        step = int(d[1])
        if d[0] == 'forward':
            hor += step
            depth += step * aim
        elif d[0] == 'down':
            aim += step
        elif d[0] == 'up':
            aim -= step
    return hor * depth


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip().split() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
