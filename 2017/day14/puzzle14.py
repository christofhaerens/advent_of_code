#!/usr/bin/python3

# --- Day 14: Disk Defragmentation ---

LEFT, RIGHT, UP, DOWN = (1, 2, 3, 4)


def knot(input, l=256):
    data = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    index = 0
    skip = 0
    round = 0
    cl = list(range(l))
    for round in range(64):
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
    khash = ''.join(["%0.2x" % i for i in dense])
    return khash, format(int(khash, 16), "0128b")


def part_1(data):
    grid = []
    count = 0
    for i in range(128):
        s = data + '-' + str(i)
        k = [int(c) for c in knot(s)[1]]
        grid.append(k)
        count += sum(k)
    return count, grid


def get_pos(r, c, rpos, gridlen):
    if rpos == LEFT:
        c -= 1
    elif rpos == RIGHT:
        c += 1
    if rpos == UP:
        r -= 1
    elif rpos == DOWN:
        r += 1
    if r < 0 or c < 0 or r == gridlen or c == gridlen:
        return None
    else:
        return (r, c)


def find_neighbours(grid, r, c):
    # starting from our position, try all directions until we only have 0
    neighbours = []
    for d in LEFT, UP, RIGHT, DOWN:
        rpos = get_pos(r, c, d, len(grid))
        if rpos:
            dr, dc = rpos
            if grid[dr][dc] == 1:
                # mark grid as visited
                grid[dr][dc] = 0
                neighbours.append((dr, dc))
                neighbours += find_neighbours(grid, dr, dc)
    return neighbours


def part_2(grid):
    region = {}
    next_reg = 1
    for r in range(128):
        for c in range(128):
            if grid[r][c] == 1:
                # check if our region is not already set
                if not (r, c) in region:
                    region[(r, c)] = next_reg
                    next_reg += 1
                    for n in find_neighbours(grid[:], r, c):
                        region[n] = region[(r, c)]
    return max(region.values())


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    fh.close()
    # assert part1 = 8316   part2 = 1074
    part1, grid = part_1(data)
    print("part1 = %d" % part1)
    print("part2 = %d" % part_2(grid))


if __name__ == '__main__':
    main()
