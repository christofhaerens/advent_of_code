#!/usr/bin/python3
# import itertools
# import functools
# import re
from collections import defaultdict

day = "--- Day 8 - 2020 ---"


def run(code):
    acc = 0
    pointer = 0
    p_hist = defaultdict(int)
    end_code = False
    while True:
        if (pointer + 1) == len(code):  # if we are at last instruction, end the program
            end_code = True
        p_hist[pointer] += 1  # keep track of pointers already visited
        if p_hist[pointer] > 1:
            return (False, acc)
        op, arg = code[pointer]
        if op == 'acc':
            acc += arg
            pointer += 1
        elif op == 'nop':
            pointer += 1
        elif op == 'jmp':
            pointer += arg
        else:
            print("Unknown instruction")
            raise Exception
        if end_code:
            return (True, acc)


def read_code(d):
    code = []
    for instruction in d:
        op, arg = instruction.split(" ")
        code.append([op, int(arg)])
    return code


def part2(d):
    acc = 0
    code = read_code(d)
    # get the jmp and nop pointers
    pointers = []
    for i, op in enumerate(code):
        if op[0] in ["nop", "jmp"]:
            pointers.append(i)
    # chg every jmp/nop pointer till we find normal exit
    for p in pointers:
        new_code = code.copy()
        op, arg = new_code[p]
        op = "jmp" if op == "nop" else "nop"
        new_code[p] = [op, arg]
        run_status, acc = run(new_code)
        if run_status is True:
            return acc


def part1(d):
    acc = 0
    code = read_code(d)
    run_status, acc = run(code)
    return acc


def solve1(data):
    return part1(data)


def solve2(data):
    return part2(data)


def solve(data):
    a1 = solve1(data.copy())
    a2 = solve2(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
