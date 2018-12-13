#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque
from operator import itemgetter, attrgetter

day = "--- Day 13: Mine Cart Madness ---"

DOWN, UP, LEFT, RIGHT, STRAIGHT = range(5)
delta = {DOWN: (0, 1), UP: (0, -1), LEFT: (-1, 0), RIGHT: (1, 0)}
cart_directions = {'v': DOWN, '^': UP, '<': LEFT, '>': RIGHT}

next_move = {('|', UP): UP, ('|', DOWN): DOWN,
             ('/', UP): RIGHT, ('/', LEFT): DOWN, ('/', RIGHT): UP, ('/', DOWN): LEFT,
             ('-', LEFT): LEFT, ('-', RIGHT): RIGHT,
             ('\\', RIGHT): DOWN, ('\\', UP): LEFT, ('\\', LEFT): UP, ('\\', DOWN): RIGHT
             }
# (cartdirection, last_turn_action_at_cross) -> (newdirection -> last_turn_action_at_cross)
next_move_cross = {(UP, LEFT): (UP, STRAIGHT), (UP, STRAIGHT): (RIGHT, RIGHT), (UP, RIGHT): (LEFT, LEFT),
                   (DOWN, LEFT): (DOWN, STRAIGHT), (DOWN, STRAIGHT): (LEFT, RIGHT), (DOWN, RIGHT): (RIGHT, LEFT),
                   (LEFT, LEFT): (LEFT, STRAIGHT), (LEFT, STRAIGHT): (UP, RIGHT), (LEFT, RIGHT): (DOWN, LEFT),
                   (RIGHT, LEFT): (RIGHT, STRAIGHT), (RIGHT, STRAIGHT): (DOWN, RIGHT), (RIGHT, RIGHT): (UP, LEFT),
                   }


def new_direction(cart, tracks):
    id, x, y, direction, last_cross = cart
    # first move
    step = delta[direction]
    x, y = x + step[0], y + step[1]
    # check that the next is still a track
    track = tracks[(x, y)]
    if track is False:
        raise RuntimeError('Error: cart %s went off track' % str(cart))
    if track == '+':
        direction, last_cross = next_move_cross[(direction, last_cross)]
    else:
        direction = next_move[(track, direction)]
    return (id, x, y, direction, last_cross)


def solve(data):
    tracks = {}
    carts = []
    cart_idx = 0
    cart_pos = {}
    for y, row in enumerate(data):
        for x, track in enumerate(row):
            if track != ' ':
                if track in cart_directions:
                    carts.append((cart_idx, x, y, cart_directions[track], RIGHT))
                    cart_pos[cart_idx] = (x, y)
                    cart_idx += 1
                    # we assume a cart never starts in a turn or on a cross; for my input this is the case
                    track = '|' if track in '^v' else '-'
                tracks[(x, y)] = track
            else:
                tracks[(x, y)] = False
    # normally the carts are sorted at this point, but nevertheless
    carts = sorted(carts, key=itemgetter(2, 1))  # sort on y=row, x=col
    # move carts
    cnt = 0
    a1 = False
    remove_cart_ids = []
    while True:  # repeat
        moved_carts = []
        cnt += 1
        for cart in carts:
            # check forst if our cart is still active
            if cart[0] in cart_pos:
                cart = new_direction(cart, tracks)
                moved_carts.append(cart)
                id, x, y = cart[0], cart[1], cart[2]
                # now check for crash
                if (x, y) in cart_pos.values():
                    # crashed !
                    # save the first crash coord
                    if not a1:
                        a1 = '%d,%d' % (x, y)
                    # remove our cart and the cart we crashed into from the list
                    for c_id, c_pos in cart_pos.items():
                        if c_pos == (x, y):
                            remove_cart_ids = [id, c_id]
                            break
                    # wipe the positions
                    for id in remove_cart_ids:
                        del(cart_pos[id])
                        remove_cart_ids = []
                    if len(cart_pos) == 1:
                        for k, pos in cart_pos.items():
                            return (a1, "%d,%d" % pos)
                else:
                    # not crashed, update the position
                    cart_pos[id] = (x, y)
        carts = sorted(moved_carts, key=itemgetter(2, 1))  # sort on x, y
    # if we arrive here, there is a problem
    raise RuntimeError("ERROR: unexpected state")


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip('\n') for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
