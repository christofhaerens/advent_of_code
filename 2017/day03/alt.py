#!/usr/bin/python3

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

# -1, 1   0, 1   1, 1
# -1, 0   0, 0   1, 0
# -1,-1   0,-1   1,-1   2,-1

RIGHT, UP, LEFT, DOWN = range(4)
go = {RIGHT: (1, 0),
      UP: (0, 1),
      LEFT: (-1, 0),
      DOWN: (0, -1)
      }


def next_position(x, y, direction):
    dx, dy = go[direction]
    return (x + dx, y + dy)


def next_direction(direction, x, y, width):
    if x == width or y == width:
        direction = (direction + 1) % 4
    if x == y == -width:
        width += 1
    return direction, width


# part 2 functions
def get_value(h, v):
    if h in values:
        if v in values[h]:
            return values[h][v]
    return 0


def set_value(value, h, v):
    if h not in values:
        values[h] = {}
    values[h][v] = value


def calculate_value(h, v):
    adj_cells = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)]
    s = get_value(h, v)
    for c in adj_cells:
        s += get_value(h + c[0], v + c[1])
    set_value(s, h, v)


# part 1
i = 1
end = 23
end = 361527
x, y = (0, 0)
width = 0
direction = RIGHT

# for part2
values = {}
values[0] = {}
values[0][0] = 1
value = 0

while i <= end:
    # calculate value of our field part2 field until we have found the value
    if value < end:
        calculate_value(x, y)
        value = get_value(x, y)
    # get our next position
    print("before = ", x,y,direction,width)
    x, y = next_position(x, y, direction)
    direction, width = next_direction(direction, x, y, width)
    print("after = ", x,y,direction,width)
    print()
    i += 1

print("part1 = %d" % (abs(x) + abs(x)))
print("part2 = %d" % value)
