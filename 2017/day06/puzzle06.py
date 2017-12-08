#!/usr/bin/python3

# --- Day 6: Memory Reallocation ---


def part_1_2(data):
    mb = data
    a = []
    count = 0
    l = len(mb)
    while mb not in a:
        oldmb = mb.copy()
        a.append(oldmb)
        count += 1
        high = max(mb)
        i = mb.index(high)
        # set our bank to zero and re-distribute
        mb[i] = 0
        while high > 0:
            # move index and rotate if needed
            i += 1
            if i == l:
                i = 0
            # incr that bank
            mb[i] += 1
            high -= 1
    return count, len(a) - a.index(mb)


def main():
    fh = open('./input', 'r')
    data = list(map(int, fh.read().strip().split()))
    fh.close()
    # assert part1 = 14029   part2 = 2765
    print("part1 = %s\npart2 = %s" % part_1_2(data))


if __name__ == '__main__':
    main()
