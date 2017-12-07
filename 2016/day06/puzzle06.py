#!/usr/bin/python3

# --- Day 6: Signals and Noise ---


def part_1_2():
    fh = open('./input', 'r')
    d = [[0 for i in range(26)] for i in range(8)]
    offset = ord('a')
    for line in fh:
        for i in range(8):
            x = ord(line[i]) - offset
            d[i][x] += 1
    fh.close()
    part1 = ''.join([chr(i.index(max(i)) + offset) for i in d])
    part2 = ''.join([chr(i.index(min(i)) + offset) for i in d])
    return part1, part2


def main():
    # assert part1 = zcreqgiv  part2 = pljvorrk
    print("part1 = %s\npart2 = %s" % part_1_2())


if __name__ == '__main__':
    main()
