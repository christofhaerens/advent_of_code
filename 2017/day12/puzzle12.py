#!/usr/bin/python3

# --- Day 12: Digital Plumber ---

import re


def part_1_2(data):
    program = {}
    groups = []
    processed = []
    for p in data:
        m = re.match(r'^(\d+) <-> ([\d\s,]+)', p)
        program[int(m.group(1))] = list(map(int, m.group(2).split(', ')))
    for p in program.keys():
        if p in processed:
            continue
        members = [p]
        found = 1
        while found > 0:
            found = 0
            for i, plist in program.items():
                if i in members:
                    processed.append(i)
                    for x in plist:
                        if x not in members:
                            members.append(x)
                            found += 1
        groups.append(members)
    # find group that conatins 0
    for g in groups:
        if 0 in g:
            part1 = len(g)
            break
    return part1, len(groups)


def main():
    fh = open('./input', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    # assert part1 = 283   part2 = 195
    print("part1 = %d\npart2 = %d" % part_1_2(data))


if __name__ == '__main__':
    main()
