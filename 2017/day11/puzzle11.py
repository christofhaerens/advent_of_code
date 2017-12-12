#!/usr/bin/python3

# --- Day 11: Hex Ed ---

location = {"n": (0, 2),
            "ne": (1, 1),
            "se": (1, -1),
            "s": (0, -2),
            "sw": (-1, -1),
            "nw": (-1, 1),
            }


def part_1_2(data):
    x, y = (0, 0)
    max_distance = 0
    for step in data:
        (rx, ry) = location[step]
        x, y = x + rx, y + ry
        distance = abs(x) + ((abs(y) - abs(x)) // 2)
        max_distance = distance if distance > max_distance else max_distance
    return distance, max_distance


def main():
    fh = open('./input', 'r')
    data = fh.read().strip().split(',')
    fh.close()
    # assert part1 = 675   part2 = 1424
    print("part1 = %d\npart2 = %d" % part_1_2(data))


if __name__ == '__main__':
    main()
