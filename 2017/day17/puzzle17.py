#!/usr/bin/python3

# --- Day 17: Spinlock ---


def part_1(count, offset):
    a = []
    p = 0
    for i in range(count):
        a = a[0:p] + [i] + a[p:]
        p = ((p + offset) % len(a)) + 1
    return a[(a.index(i) + 1) % len(a)]


def part_2(count, offset):
    p = 0
    for i in range(count):
        p = ((p + offset) % (i + 1)) + 1
        if p == 1:
            after = i + 1
    return after


def main():
    # assert part1 = 777   part2 = 39289581
    print("part1 = %d" % part_1(2018, 376))
    print("part2 = %d" % part_2(50000000, 376))


if __name__ == '__main__':
    main()
