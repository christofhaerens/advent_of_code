#!/usr/bin/python3


# --- Day 10: Knot Hash ---

def part_1(data, l):
    index = 0
    skip = 0
    cl = list(range(l))
    for jump in data:
        if jump + index > l:
            j1, j2 = l - index, (index + jump) - l
            sub_cl = cl[index:index + j1] + cl[0:j2]
        else:
            sub_cl = cl[index:index + jump]
        sub_cl.reverse()
        for i in range(jump):
            cl[(index + i) % l] = sub_cl[i]
        index = (index + jump + skip) % l
        skip += 1
    return cl[0] * cl[1]



def part_2(data, l):
    index = 0
    skip = 0
    round = 0
    cl = list(range(l))
    while round < 64:
        round += 1
        for jump in data:
            if jump + index > l:
                j1, j2 = l - index, (index + jump) - l
                sub_cl = cl[index:index + j1] + cl[0:j2]
            else:
                sub_cl = cl[index:index + jump]
            sub_cl.reverse()
            for i in range(jump):
                cl[(index + i) % l] = sub_cl[i]
            index = (index + jump + skip) % l
            skip += 1
    dense = []
    for i in range(l):
        h = cl[i] if i % 16 == 0 else h ^ cl[i]
        if i % 16 == 15:
            dense.append(h)
    part2 = ["%0.2x" % i for i in dense]
    return ''.join(part2)


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    fh.close()
    data1 = list(map(int, data.split(',')))
    data2 = list(map(ord, data)) + [17, 31, 73, 47, 23]
    # assert part1 = 1935   part2 = dc7e7dee710d4c7201ce42713e6b8359
    print("part1 = %d" % part_1(data1, 256))
    print("part2 = %s" % part_2(data2, 256))


if __name__ == '__main__':
    main()
