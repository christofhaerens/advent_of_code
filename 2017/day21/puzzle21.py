#!/usr/bin/python3

# --- Day 21: Fractal Art ---


def print_square(square):
    print()
    for i in square.split('/'):
        print(i)


def rotate(square):
    sq = square.split('/')
    sqy = sq.copy()
    for i in range(len(sq)):
        sqy[i] = ''
        for j in range(len(sq[i])):
            sqy[i] += sq[-(j + 1)][i]
    return '/'.join(sqy)


def flip_hor(square):
    sq = square.split('/')
    for i in range(len(sq)):
        a = [x for x in sq[i]]
        a.reverse()
        sq[i] = ''.join(a)
    return '/'.join(sq)


def flip_ver(square):
    sq = square.split('/')
    sqy = []
    for i in range(len(sq)):
        sqy.append(sq[-(i + 1)])
    return '/'.join(sqy)


def split_square(square):
    sq = square.split('/')
    l = len(sq)
    squares = {}
    if l > 3:
        for split in (2, 3):
            if l % split == 0:
                for r in range(l):
                    x = r % split
                    xcount = r // split
                    for c in range(l):
                        y = c % split
                        ycount = c // split
                        sq_count = xcount * (l // split) + ycount
                        count = x * split + y
                        if sq_count in squares:
                            squares[sq_count] += sq[r][c]
                            if y == (split - 1) and count + 1 != split**2:
                                squares[sq_count] += '/'
                        else:
                            squares[sq_count] = sq[r][c]
                return [squares[i] for i in range(len(squares))]
    else:
        return [square]


def part_1(square, rules, iterations):
    for _ in range(iterations):
        squares = split_square(square)
        new_sq = []
        # find the new squares
        for s in squares:
            x = s
            mutations = 0
            while x not in rules:
                mutations += 1
                if mutations == 5:
                    x = flip_ver(x)
                else:
                    x = rotate(x)
                if mutations > 100:
                    exit(2)
            rule = rules[x]
            new_sq.append(rule)
        # reassemble square
        l = len(new_sq)
        if l == 1:
            square = new_sq[0]
        else:
            square = []
            h = int(l**0.5)
            index = 0
            for i, s in enumerate(new_sq):
                if i % h == 0:
                    indexes = []
                for j, p in enumerate(s.split('/')):
                    if i % h == 0:
                        square.append(p)
                        indexes.append(index)
                        index += 1
                    else:
                        v = indexes[j]
                        square[v] += p
            square = '/'.join(square)
    return square.count('#')


def main():
    fh = open('./input', 'r')
    data = [line.strip().split(' => ') for line in fh]
    fh.close()
    rules = {}
    for r in data:
        rules[r[0]] = r[1]
    square = '.#./..#/###'
    # assert part1 = 190   part2 = 2335049
    print("part1 = %d" % part_1(square, rules, 5))
    print("part2 = %d" % part_1(square, rules, 18))


if __name__ == '__main__':
    main()
