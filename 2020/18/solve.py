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


def calc1(d):
    stack = d[:]
    stack.reverse()
    while len(stack) > 1:
        *stack, y, op, x = stack
        stack.append(OP[op](x, y))
    return stack[0]


def calc2(d):
    stack = d[:]
    while "+" in stack:
        i = stack.index('+')
        stack = stack[:i - 1] + [stack[i - 1] + stack[i + 1]] + stack[i + 2:]
    a = 1
    for x in stack:
        if x != "*":
            a *= x
    return a


def sanitize_line(d):
    line = []
    for x in d.replace("(", " ( ").replace(")", " ) ").split(" "):
        if x != "":
            line.append(x if x in "+*()" else int(x))
    return(line)


def homework(data, f):
    a = 0
    for expression in data:
        level = 0
        stack = defaultdict(list)
        for i, c in enumerate(expression):
            if c == "(":
                level += 1
            elif c == ")":
                stack[level - 1].append(f(stack[level]))
                stack[level] = []
                level -= 1
            else:
                stack[level].append(c)
        a += f(stack[level])
    return a


def solve1(data):
    return homework(data, calc1)


def solve2(data):
    return homework(data, calc2)


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
