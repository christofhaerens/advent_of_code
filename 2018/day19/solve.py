#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 19: Go With The Flow ---"
OPERATIONS = {  # r = register, i = instruction
    'addr': lambda r, i: r[i[1]] + r[i[2]],
    'addi': lambda r, i: r[i[1]] + i[2],
    'mulr': lambda r, i: r[i[1]] * r[i[2]],
    'muli': lambda r, i: r[i[1]] * i[2],
    'banr': lambda r, i: r[i[1]] & r[i[2]],
    'bani': lambda r, i: r[i[1]] & i[2],
    'borr': lambda r, i: r[i[1]] | r[i[2]],
    'bori': lambda r, i: r[i[1]] | i[2],
    'setr': lambda r, i: r[i[1]],
    'seti': lambda r, i: i[1],
    'gtir': lambda r, i: 1 if i[1] > r[i[2]] else 0,
    'gtri': lambda r, i: 1 if r[i[1]] > i[2] else 0,
    'gtrr': lambda r, i: 1 if r[i[1]] > r[i[2]] else 0,
    'eqir': lambda r, i: 1 if i[1] == r[i[2]] else 0,
    'eqri': lambda r, i: 1 if r[i[1]] == i[2] else 0,
    'eqrr': lambda r, i: 1 if r[i[1]] == r[i[2]] else 0,
}


# the part1 solution, but if you know the part2 solution we can get part1 faster
def part1(data, ip=0):
    ip_idx = int(data[0][4:])
    program = []
    r = [0] * 6
    for line in data[1:]:
        program.append([int(v) if i > 0 else v for i, v in enumerate(line.split(" "))])
    # run program
    while ip < len(program):
        # get the instruction
        instr = program[ip]
        # update the ip reg with the ip value
        r[ip_idx] = ip
        # execute instruction
        r[instr[3]] = OPERATIONS[instr[0]](r, instr)
        # copy ip reg to ip and add 1
        ip = r[ip_idx] + 1
    return [r[0], 'a']


def part2(data, r0=0, ip=0):
    ip_idx = int(data[0][4:])
    program = []
    r = [r0] + [0] * 5
    for line in data[1:]:
        program.append([int(v) if i > 0 else v for i, v in enumerate(line.split(" "))])
    # run program, we get r1 afterat least 100 loops
    for i in range(100):
        # get the instruction
        instr = program[ip]
        # update the ip reg with the ip value
        r[ip_idx] = ip
        # execute instruction
        r[instr[3]] = OPERATIONS[instr[0]](r, instr)
        # copy ip reg to ip and add 1
        ip = r[ip_idx] + 1
    return divisors_sum(r[1])


def divisors_sum(r1):
    # sum all the divisors of r1
    return sum([i for i in range(1, r1 + 1) if r1 % i == 0])
    # the program does the above. By following the instructions I came to the code below
    # evaluating that code I came to the conclusion of sum divisors
    # while r2 <= r1:
    #     r4 = 0
    #     while r4 <= r1:
    #         if r2 * r4 == r1:
    #             r0 += r2
    #             print(r0)
    #         r4 += 1
    #     r2 += 1
    # print("r0", r0)


def solve(data):
    return [part2(data, r0=0), part2(data, r0=1)]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    # fh = open('./input_test.txt', 'r')
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()

# too low:  10551384
