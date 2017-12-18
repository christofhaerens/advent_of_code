#!/usr/bin/python3

# --- Day 16: Permutation Promenade ---

import re


def read_moves(data):
    moves = []
    re_s = re.compile('^s(\d+)')
    re_e = re.compile('^[xp](\w+)/(\w+)')
    for move in data:
        if move.startswith('s'):
            m = re.match(re_s, move)
            moves.append(('s', int(m.group(1))))
        else:
            m = re.match(re_e, move)
            if move.startswith('x'):
                moves.append(('x', int(m.group(1)), int(m.group(2))))
            else:
                moves.append(('p', m.group(1), m.group(2)))
    return moves


def dance(dancers, moves):
    d = dancers.copy()
    for m in moves:
        if m[0] == 's':
            d = d[-m[1]:] + d[:len(d) - m[1]]
            # d = spin(d, int(m.group(1)))
        else:
            if m[0] == 'x':
                x, y = m[1], m[2]
                d[x], d[y] = d[y], d[x]
                # d = exchange(d, int(m.group(1)), int(m.group(2)))
            else:
                x, y = d.index(m[1]), d.index(m[2])
                d[x], d[y] = d[y], d[x]
                # d = partner(d, m.group(1), m.group(2))
    return d[:]


def part_1(moves):
    dancers = [d for d in 'abcdefghijklmnop']
    return ''.join(dance(dancers, moves))


def part_2(moves):
    dancers = [d for d in 'abcdefghijklmnop']
    d = dancers.copy()
    # search till we find our start position
    for r in range(1000000000):
        d = dance(d, moves)
        if d == dancers:
            break
    for r in range(1000000000 % (r + 1)):
        d = dance(d, moves)
    return ''.join(d)


def main():
    fh = open('./input', 'r')
    data = fh.read().strip().split(',')
    fh.close()
    # assert part1 = iabmedjhclofgknp   part2 = oildcmfeajhbpngk
    moves = read_moves(data)
    print("part1 = %s" % part_1(moves))
    print("part2 = %s" % part_2(moves))


if __name__ == '__main__':
    main()
