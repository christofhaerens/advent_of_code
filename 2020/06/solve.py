#!/usr/bin/python3
# import itertools
# import functools
# import re
from collections import defaultdict

day = "--- Day 6 - 2020 ---"


def find_answers(d, unique_answers):
    if d[-1] != "":
        d.append("")  # append empty line to process the last entry
    answers = defaultdict(int)
    a_sum = 0
    for line in d:
        if line == "":
            if unique_answers:
                for a in answers.keys():
                    if a != 'count':
                        if answers[a] == answers['count']:
                            a_sum += 1
            else:
                a_sum += len(answers.keys()) - 1  # substract 1 for 'count' key
            answers = defaultdict(int)
        else:
            answers['count'] += 1
            for a in line:
                answers[a] += 1
    return a_sum


def solve1(data):
    return find_answers(data, False)


def solve2(data):
    return find_answers(data, True)


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
