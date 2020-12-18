#!/usr/bin/python3
import time
# import itertools
# import functools
# import re
# from collections import Counter
from collections import defaultdict
# from collections import deque

day = "--- Day 18 - 2020 ---"

OP = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}


def calc(d):
    stack = d[:]
    stack.reverse()
    while len(stack) > 1:
        *stack, y, op, x = stack
        stack.append(OP[op](int(x), int(y)))
    return stack[0]


def calc2(d):
    stack_len = len(d)
    stack = d[:] + [""]  # append extra element for the i+1 to work
    new_stack = []
    i = 0
    # do all sums first
    while i < stack_len:
        if stack[i + 1] == "+":
            new_stack.append(int(stack[i]) + int(stack[i + 2]))
            i += 2
        else:
            if stack[i] == "+":
                x = new_stack.pop()
                new_stack.append(x + int(stack[i + 1]))
                i += 1
            elif stack[i] != '*':
                new_stack.append(int(stack[i]))
        i += 1
    a = 1
    # only products left in new_stack
    for x in new_stack:
        a *= x
    return a


def sanitize_line(d):
    line = []
    for x in d.replace("(", " ( ").replace(")", " ) ").split(" "):
        if x != "":
            line.append(x)
    return(line)


def solve1(data):
    a = 0
    for expression in data:
        level = 0
        stack = defaultdict(list)
        for i, c in enumerate(expression):
            if c == "(":
                level += 1
            elif c == ")":
                stack[level - 1].append(calc(stack[level]))
                stack[level] = []
                level -= 1
            else:
                stack[level].append(c)
        a += calc(stack[level])
    return a


def solve2(data):
    a = 0
    for expression in data:
        level = 0
        stack = defaultdict(list)
        for i, c in enumerate(expression):
            if c == "(":
                level += 1
            elif c == ")":
                stack[level - 1].append(calc2(stack[level]))
                stack[level] = []
                level -= 1
            else:
                stack[level].append(c)
        a += calc2(stack[level])
    return a


def solve(data):
    print(f"\n{day}\n")
    t = time.perf_counter()
    a1 = solve1(data.copy())
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part1 = %r\n" % (a1))
    t = time.perf_counter()
    a2 = solve2(data.copy())
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part2 = %r\n" % (a2))


def main():
    fh = open('./input.txt', 'r')
    data = [sanitize_line(line.strip()) for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
