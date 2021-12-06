#!/usr/bin/python3
from collections import Counter, defaultdict

day = "--- Day 6 - 2021 ---"


def lanterfish(fish, afterdays):
    for _ in range(afterdays):
        newfish = defaultdict(lambda: 0)
        for days in fish.keys():
            if days == 0:
                newfish[8] += fish[days]
                newfish[6] += fish[days]
            else:
                newfish[days - 1] += fish[days]
        fish = newfish
    return sum(fish.values())


def solve1(data):
    fish = Counter([int(f) for f in data[0].split(",")])
    return lanterfish(fish, 80)


def solve2(data):
    fish = Counter([int(f) for f in data[0].split(",")])
    return lanterfish(fish, 256)


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
