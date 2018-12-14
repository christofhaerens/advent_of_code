#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque


day = "--- Day 14: Chocolate Charts ---"


def print_recipes(recipes, elf):
    s = ''
    for i, r in enumerate(recipes):
        if i == elf[0]:
            s += '(%d) ' % r
        elif i == elf[1]:
            s += '[%d] ' % r
        else:
            s += ' %s  ' % r
    print(s)


def solve(data):
    input1 = int(data[0])
    input2 = [int(x) for x in data[0]]
    li = len(input2)
    recipes = [3, 7]
    elf = [0, 1]
    a1, a2 = False, False
    while not a1 or not a2:
        r0 = recipes[elf[0]]
        r1 = recipes[elf[1]]
        r2 = r0 + r1
        if r2 > 9:
            recipes += [1, r2 % 10]
        else:
            recipes.append(r2)
        l = len(recipes)
        elf[0] = (elf[0] + r0 + 1) % l
        elf[1] = (elf[1] + r1 + 1) % l
        # part1
        if not a1:
            if len(recipes) > input1 + 10:
                a1 = "".join(map(str, recipes[input1:input1 + 10]))
        # part2
        if not a2:
            # check our input (recipes can grow with 1 or 2, so check both)
            if recipes[-li:] == input or recipes[-li - 1:-1] == input2:
                a2 = len(recipes) - li if r2 < 10 else len(recipes) - li - 1
    return [a1, a2]


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
