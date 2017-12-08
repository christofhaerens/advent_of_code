#!/usr/bin/python3


def part_1(k):
    # k = '1111'
    # part 1
    prev = 0
    count = 0
    first = 0
    sum = 0
    a = [int(d) for d in k]
    for d in a:
        count += 1
        if count == 1:
            first = d
        # did we have already a match?
        if prev == d:
            sum += d
        prev = d
    # if last == first and match. add to sum
    if d == first:
        sum += d
    return sum


def part_2(k):
    som = 0
    a = [int(v) for v in k]
    l = len(a)
    i = 0
    # caculate half, because send half is the same
    h = int(l / 2)
    while i < h:
        if a[i] == a[i + h]:
            som += a[i]
        i += 1
    return som * 2


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    fh.close()
    # assert part1 = 995  part2 = 1130
    print("part1 = %s" % part_1(data))
    print("part2 = %s" % part_2(data))


if __name__ == '__main__':
    main()
