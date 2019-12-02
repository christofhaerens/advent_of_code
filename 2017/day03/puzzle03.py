#!/usr/bin/python3

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

# -1, 1   0, 1   1, 1
# -1, 0   0, 0   1, 0
# -1,-1   0,-1   1,-1   2,-1

RIGHT = 1
UP = 2
LEFT = 3
DOWN = 4
dname = ['NONE', 'RIGHT', 'UP', 'LEFT', 'DOWN']


def next_position(lh, lv, ldirection):
    if ldirection == RIGHT:
        return (lh + 1, lv)
    elif ldirection == UP:
        return (lh, lv + 1)
    elif ldirection == LEFT:
        return (lh - 1, lv)
    elif ldirection == DOWN:
        return (lh, lv - 1)


def next_direction(ldirection, lh, lhmax, lv, lvmax):
    if ldirection == RIGHT:
        if lh > lhmax and lv <= lvmax:
            return (UP, lhmax + 1, lvmax)
        else:
            return (ldirection, lhmax, lvmax)
    if ldirection == UP:
        if lh <= lhmax and lv > lvmax:
            return (LEFT, lhmax, lvmax + 1)
        else:
            return (ldirection, lhmax, lvmax)
    if ldirection == LEFT:
        if abs(lh) == lhmax:
            return (DOWN, lhmax, lvmax)
        else:
            return (ldirection, lhmax, lvmax)
    if ldirection == DOWN:
        if abs(lv) == lvmax:
            return (RIGHT, lhmax, lvmax)
        else:
            return (ldirection, lhmax, lvmax)


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
hmax = 0
vmax = 0
# horizontal and vertical position
hp = 0
vp = 0
# which direction we next go (1 = go right; 2 = go up, 3 go left, 4 go down)
direction = RIGHT

# for part2
values = {}
values[0] = {}
values[0][0] = 1
value = 0

while i <= end:
    # calculate value of our field part2 field until we have found the value
    if value < end:
        calculate_value(hp, vp)
        value = get_value(hp, vp)
    # get our next position
    hp, vp = next_position(hp, vp, direction)
    direction, hmax, vmax = next_direction(direction, hp, hmax, vp, vmax)
    i += 1

# assert part1 = 327  part2 = 363010

print("part1 = %d" % (abs(hp) + abs(vp)))
print("part2 = %d" % value)
