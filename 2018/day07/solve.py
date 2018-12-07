#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque


day = "--- Day 7: The Sum of Its Parts ---"


def solve(data):
    steps_1 = defaultdict(list)
    steps_2 = defaultdict(list)
    for d in data:
        m = re.match(r'Step (.) must be finished before step (.) can begin.', d)
        s1, s2 = m.groups()
        steps_1[s1].append(s2)
        steps_2[s2].append(s1)
    # find the step that needs to be first
    steps_available = []
    steps_done = []
    for s in steps_1:
        if s not in steps_2:
            steps_available.append(s)
    while len(steps_available) > 0:
        # do the step
        steps_available.sort(reverse=True)
        step = steps_available.pop()
        steps_done.append(step)
        # check if extra steps are avaiable yet
        steps = steps_2.copy()
        for k in steps:
            if step in steps[k]:
                steps[k].remove(step)
            if len(steps[k]) == 0:
                steps_available.append(k)
                del(steps_2[k])
    return [''.join(steps_done), solve2(data)]


def find_available_steps(steps, before, avail):
    a = avail.copy()
    before2 = before.copy()
    # are there steps where the prereq are empty
    for step, prereqs in before2.items():
        if len(prereqs) == 0:
            a.append(step)
            del(before[step])
    # are there steps that don't have any prereq?
    for step in steps:
        if step not in before:
            a.append(step)
    # cleanup steps to do
    for step in a:
        if step in steps:
            steps.remove(step)
    return [steps, before, a]


def solve2(data):
    steps = []
    before = defaultdict(list)
    for d in data:
        m = re.match(r'Step (.) must be finished before step (.) can begin.', d)
        steps += m.groups()
        before[m.group(2)].append(m.group(1))
    steps = list(set(steps))
    steps_done = []
    steps_available = []
    steps, before, steps_available = find_available_steps(steps, before, steps_available)
    doing = {}
    max_workers = 5
    work_duration = 61 - ord('A')
    sec = 0
    while len(steps_available) > 0 or len(doing) > 0:
        # check for steps as long workers are available
        while len(doing) < max_workers and steps_available:
            steps_available.sort(reverse=True)
            step = steps_available.pop()
            doing[step] = work_duration + ord(step)
        # wait a sec
        sec += 1
        # decrease workers
        for step in doing:
            doing[step] -= 1
        # check if steps are done
        t = {}
        for step in doing:
            if doing[step] == 0:
                steps_done.append(step)
                for k in before.keys():
                    if step in before[k]:
                        before[k].remove(step)
            else:
                t[step] = doing[step]
        doing = t.copy()
        steps, before, steps_available = find_available_steps(steps, before, steps_available)
    return sec


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
