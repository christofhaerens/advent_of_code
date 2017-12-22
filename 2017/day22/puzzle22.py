#!/usr/bin/python3

# --- Day 22: Sporifica Virus ---

UP, RIGHT, DOWN, LEFT = range(4)
MOVE = {UP: (0, -1), RIGHT: (1, 0), DOWN: (0, 1), LEFT: (-1, 0)}
CLEAN, INFECTED, WEAK, FLAGGED = ('.', '#', 'W', 'F')


def part_1(data):
    start = (len(data) // 2, len(data[0]) // 2)
    going = UP
    grid = {}
    for r, d in enumerate(data):
        for c, n in enumerate(d):
            grid[(c, r)] = n
    pos = start
    infected = 0
    for _ in range(10000):
        if pos not in grid:
            grid[pos] = CLEAN
        if grid[pos] == CLEAN:
            going = (going + 3) % 4
            grid[pos] = INFECTED
            infected += 1
        else:
            grid[pos] = CLEAN
            going = (going + 1) % 4
        pos = (pos[0] + MOVE[going][0], pos[1] + MOVE[going][1])
    return infected


def part_2(data):
    start = (len(data) // 2, len(data[0]) // 2)
    going = UP
    grid = {}
    for r, d in enumerate(data):
        for c, n in enumerate(d):
            grid[(c, r)] = n
    pos = start
    infected = 0
    for _ in range(10000000):
        if pos not in grid:
            grid[pos] = CLEAN
        if grid[pos] == CLEAN:
            grid[pos] = WEAK
            going = (going + 3) % 4  # turn left
        elif grid[pos] == INFECTED:
            grid[pos] = FLAGGED
            going = (going + 1) % 4  # turn right
        elif grid[pos] == FLAGGED:
            grid[pos] = CLEAN
            going = (going + 2) % 4  # turn around
        else:
            grid[pos] = INFECTED
            infected += 1
        pos = (pos[0] + MOVE[going][0], pos[1] + MOVE[going][1])
    return infected


def main():
    fh = open('./input', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    # assert part1 = 5460   part2 = 2511702
    print("part1 = %d" % part_1(data[:]))
    print("part2 = %d" % part_2(data[:]))


if __name__ == '__main__':
    main()
