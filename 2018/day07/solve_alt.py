#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque


day = "--- Day 7: The Sum of Its Parts ---"


class Step(object):
    TASK_DURATION = 60 + 1 - ord('A')

    def __init__(self, name):
        self.name = name
        self.prereqs = []
        self.org_available = True
        self.reset(wait=False)

    def reset(self, wait):
        self.duration = Step.TASK_DURATION + ord(self.name) if wait else 1
        self.done = False
        self.available = self.org_available
        self.in_progress = False
        self.remaining_prereqs = self.prereqs.copy()

    def start(self):
        self.in_progress = True
        self.available = False

    def do_work(self):
        if self.in_progress:
            self.duration -= 1
            if self.duration == 0:
                self.done = True
                self.in_progress = False
        return self.done

    def add_prereq(self, req):
        self.prereqs.append(req)
        self.remaining_prereqs.append(req)
        self.available = False
        self.org_available = False

    def prereq_completed(self, req):
        if req in self.remaining_prereqs:
            self.remaining_prereqs.remove(req)
            if len(self.remaining_prereqs) == 0:
                self.available = True

    def __str__(self):
        return "%s:%r" % (self.name, self.remaining_prereqs)


def solve(data):
    steps = {}
    all_steps = []
    sec = 0
    workers = []
    max_workers = 5
    # parse data
    for d in data:
        m = re.match(r'Step (.) must be finished before step (.) can begin.', d)
        for s in m.groups():
            if s not in all_steps:
                all_steps.append(s)
                steps[s] = Step(s)
        steps[m.group(2)].add_prereq(m.group(1))
    # start
    for s in steps:
        print(steps[s])
        steps[s].reset(True)
        print(steps[s])
    available = sorted([k for k, v in steps.items() if v.available], reverse=True)
    while len(available) > 0 or len(workers) > 0:
        while len(workers) <= max_workers and available:
            s = available.pop()
            steps[s].start()
            workers.append(s)
        # work
        sec += 1
        notdone = []
        for w in workers:
            if steps[w].do_work():  # returns True if done
                [steps[s].prereq_completed(w) for s in steps]
            else:
                notdone.append(w)
        workers = notdone
        available = sorted([k for k, v in steps.items() if v.available], reverse=True)

    return [['E'], sec]


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
