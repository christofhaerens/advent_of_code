#!/usr/bin/python3


def part_1(data):
    checksum = 0
    for a in data:
        checksum += (max(a) - min(a))
    return checksum


def part_2(data):
    checksum = 0
    for a in data:
        while len(a) > 0:
            d = a.pop()
            for i in a:
                if d > i:
                    getal, deler = d, i
                else:
                    getal, deler = i, d
                if getal % deler == 0:
                    checksum += getal // deler
                    break
    return checksum


def main():
    fh = open('./input', 'r')
    data = [list(map(int, line.strip().split())) for line in fh]
    fh.close()
    # assert part1 = 50376  part2 = 267
    print("part1 = %s" % part_1(data))
    print("part2 = %s" % part_2(data))


if __name__ == '__main__':
    main()
