#!/usr/bin/python3

import re
from collections import defaultdict

day = "--- Day 5 - 2019 ---"


def intcode(data, user_input, debug=False):
    f = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        7: lambda x, y: 1 if x < y else 0,
        8: lambda x, y: 1 if x == y else 0,
    }
    pos = 0
    run = True
    last_output = 0
    while run:
        instruction = str(data[pos])
        for i in range(5 - len(instruction)):
            instruction = '0' + instruction
        opcode = int(''.join(instruction[-2:]))
        mode1 = instruction[2]
        mode2 = instruction[1]
        # mode3 = instruction[0]
        if debug:
            print(pos, opcode, data[pos:pos + 8])
        if opcode == 99:
            run = False
        elif last_output != 0:
            print("Test failed")
            run = False
        elif opcode in [1, 2, 7, 8]:
            p1, p2, p3 = data[pos + 1:pos + 4]
            v1 = data[p1] if mode1 == '0' else p1
            v2 = data[p2] if mode2 == '0' else p2
            data[p3] = f[opcode](v1, v2)
            if debug:
                print("   ", v1, v2, data[p3])
            pos += 4
        elif opcode == 3:  # input
            p1 = data[pos + 1]
            # data[p1] = int(input('Input: '))
            data[p1] = user_input
            pos += 2
        elif opcode == 4:  # output
            p1 = data[pos + 1]
            v1 = data[p1] if mode1 == '0' else p1
            if debug:
                print("out ", mode1, p1, v1)
                print('Output: %d' % v1)
            last_output = v1
            pos += 2
        elif opcode == 5:  # jump if true (non-zero)
            p1, p2 = data[pos + 1:pos + 3]
            v1 = data[p1] if mode1 == '0' else p1
            if v1 != 0:
                pos = data[p2] if mode2 == '0' else p2
            else:
                pos += 3
            if debug:
                print("   p1 p2 v1 pos ", p1, p2, v1, pos)
        elif opcode == 6:  # jump if false (zero)
            p1, p2 = data[pos + 1:pos + 3]
            v1 = data[p1] if mode1 == '0' else p1
            if v1 == 0:
                pos = data[p2] if mode2 == '0' else p2
            else:
                pos += 3
            if debug:
                print("   ", v1, p2, pos)
        else:
            print('Error')
            run = False
    return last_output


def solve1(data):
    return intcode(data.copy(), 1)


def solve2(data):
    return intcode(data.copy(), 5)


def solve(data):
    a1, a2 = (0, 0)
    print("\n%s" % day)
    a1 = solve1(data)
    print("part1 = %r" % a1)
    a2 = solve2(data)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    i = [line.strip().split(',') for line in fh]
    data = [int(d) for d in i[0]]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
