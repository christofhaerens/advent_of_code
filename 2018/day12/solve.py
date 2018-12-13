#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque


day = "--- Day 12: Subterranean Sustainability ---"
PLANT = '#'
GENERATIONS = 50000000000


def generation(pots, patterns):
    pmin = min(pots)
    pmax = max(pots)
    new_pots = []
    # loop over all pots
    for pot in range(pmin - 2, pmax + 3):
        # make a list of pots around us that have a plant
        pots_around = [x for x in range(-2, 3) if pot + x in pots]
        if pots_around in patterns:
            new_pots.append(pot)
    return(new_pots)


def solve(data):
    m = re.match(r'initial state:\s+(\S+)', data[0])
    # keep a list of pot indexes where the a plant is
    pots = [idx for idx, p in enumerate(m.group(1)) if p == PLANT]
    # we are only interested in patterns that produce a plant
    patterns = []
    for d in data[2:]:
        m = re.match(r'(\S+)\s+=>\s+(\S)', d)
        if m.group(2) == PLANT:
            patterns.append([idx - 2 for idx, p in enumerate(m.group(1)) if p == PLANT])
    previous_sum = sum(pots)
    increases = []
    for x in range(1, GENERATIONS + 1):
        pots = generation(pots, patterns)
        pots_sum = sum(pots)
        # part1
        if x == 20:
            a1 = pots_sum
        # part2
        # keep track of differences
        increases.append(pots_sum - previous_sum)
        # check every 500 generations if all increases are the same
        if x % 500 == 0:
            equal = True
            for increase in increases:
                if increases[0] != increase:
                    equal = False
                    break
            if equal:
                # all increases are the same, we assume the rest will also be
                remaining = (GENERATIONS - x) * increases[0]
                return (a1, sum(pots) + remaining)
            increases = []
        previous_sum = pots_sum
        if x > 100000:
            return (a1, 'Unable to detect a pattern')


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
