#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "---  ---"
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


def part1(data, r0=0, ip=0):  # the part1 solution, but if you know the part2 solution we can get part1 faster
    ip_idx = int(data[0][4:])
    program = []
    r = [r0] + [0] * 5
    for line in data[1:]:
        program.append([int(v) if i > 0 else v for i, v in enumerate(line.split(" "))])
    # run program
    failed = False
    cnt = 0
    while ip < len(program):
        # get the instruction
        instr = program[ip]
        # update the ip reg with the ip value
        r[ip_idx] = ip
        a = "%d %r  -->  %r : " % (ip, r, instr)
        # execute instruction
        r[instr[3]] = OPERATIONS[instr[0]](r, instr)
        # copy ip reg to ip and add 1
        ip = r[ip_idx] + 1
        print("%s%r %d" % (a, r, ip))
        cnt += 1
        if cnt > 500:
            failed = True
            break
    return (failed, r0, cnt)


def solve(data):
    for i in range(1):
        failed, ro, cnt = part1(data, i)
        if not failed:
            print(failed, ro, cnt)
    return ['a', 'a']


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
