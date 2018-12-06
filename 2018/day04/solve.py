#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 4: Repose Record ---"


def solve(data):
    guard_log = {}
    slept = defaultdict(int)
    slept_on_min = defaultdict(list)
    gid_min = defaultdict(int)
    # build data
    for d in data:
        m = re.match(r'^\[(.+)\]\s+(.+)', d)
        guard_log[m.group(1)] = m.group(2)
    for k in sorted(guard_log):
        action = guard_log[k]
        m = re.match(r'^\S+\s+(\d+):(\d+)', k)
        hour, min = [int(x) for x in m.groups()]
        if action.startswith('Guard #'):
            m = re.match(r'^Guard #(\d+)', action)
            gid = int(m.group(1))
            state = 'awake'
        elif action == 'falls asleep':
            # some vaidation checks
            if state != 'awake':
                raise RuntimeError('Fall asleep order mismatch (%s)' % k)
            if hour == 23:
                raise RuntimeError('Fall asleep hour mismatch (%s)' % k)
            state = 'sleep'
            sleep_start = min
        elif action == 'wakes up':
            # some vaidation checks
            if state != 'sleep':
                raise RuntimeError('Wake up order mismatch (%s)' % k)
            if hour == 23:
                raise RuntimeError('Wake up hour mismatch (%s)' % k)
            state = 'awake'
            slept[gid] += min - sleep_start
            for i in range(sleep_start, min):
                slept_on_min[gid].append(i)
                gid_min["%d_%d" % (gid, i)] += 1

    # part 1
    w = Counter(slept)
    gid1, total_sleep = w.most_common(1)[0]
    w = Counter(slept_on_min[gid])
    min_most_asleep, c = w.most_common(1)[0]
    # part 2
    w = Counter(gid_min)
    gid_min, c = w.most_common(1)[0]
    gid2, min2 = [int(x) for x in gid_min.split('_')]
    return [gid1 * min_most_asleep, gid2 * min2]


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
