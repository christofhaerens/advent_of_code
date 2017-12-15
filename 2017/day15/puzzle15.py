#!/usr/bin/python3

# --- Day 15: Dueling Generators ---

DIV = 2147483647


def part_1(data):
    judge = 0
    b = 2**16 - 1
    va, fa = data[0]
    vb, fb = data[1]
    for x in range(40000000):
        va = (va * fa) % DIV
        vb = (vb * fb) % DIV
        if va & b == vb & b:
            judge += 1
    return judge


def part_2(data):
    judge = 0
    b = 2**16 - 1
    va, fa = data[0]
    vb, fb = data[1]
    for x in range(5000000):
        search = True
        while search:
            va = (va * fa) % DIV
            if va % 4 == 0:
                search = False
        search = True
        while search:
            vb = (vb * fb) % DIV
            if vb % 8 == 0:
                search = False
        if va & b == vb & b:
            judge += 1
    return judge


def main():
    # Generator A starts with 116
    # Generator B starts with 299
    # generator A uses 16807; generator B uses 48271
    # and then keep the remainder of dividing that resulting product by 2147483647
    # assert part1 = 569    part2 = 298
    print("part1 = %d" % part_1([[116, 16807], [299, 48271]]))
    print("part2 = %d" % part_2([[116, 16807], [299, 48271]]))


if __name__ == '__main__':
    main()
