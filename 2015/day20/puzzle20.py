#!/usr/bin/python3

# --- Day 20: Infinite Elves and Infinite Houses ---

import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def part_1(high):
    house = 0
    while True:
        house += 1
        elves = list(divisorGenerator(house))
        presents = sum([i * 10 for i in elves])
        if presents > high:
            break
        return house


def part_2(high, maxhouse):
    house = 0
    visit_count = [0]
    while True:
        house += 1
        visit_count.append(0)
        elves = list(divisorGenerator(house))
        visiting = []
        for e in elves:
            e = int(e)
            if visit_count[e] < maxhouse:
                visit_count[e] += 1
                visiting.append(e)
        presents = sum([i * 11 for i in visiting])
        if presents > high:
            break
    return house


def main():
    data = 36000000
    # assert part1 = 831600   part2 = 884520
    print("part1 = %d" % part_1(data))
    print("part2 = %d" % part_2(data, 50))


if __name__ == '__main__':
    main()
