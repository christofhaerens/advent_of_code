#!/usr/bin/python3

# --- Day 20: Particle Swarm ---

import re


def read_data(data):
    particles = []
    for d in data:
        # p=<1748,-6950,-3185>, v=<-38,157,136>, a=<-2,8,-1>
        m = re.match(r'^p=<([^>]+)>, v=<([^>]+)>, a=<([^>]+)>', d)
        particles.append([[int(i) for i in g.split(',')] for g in m.groups()])
    return particles


def part_1(particles):
    equal_sign = False
    while not equal_sign:
        equal_sign = True
        # loop till px, vx and ax have the same sign (same applies to y and z)
        for i, p in enumerate(particles):
            for j in range(3):
                p[1][j] += p[2][j]
                p[0][j] += p[1][j]
            if equal_sign:
                us = sum([abs(a) for a in [p[0][0], p[1][0], p[2][0]]])
                ss = sum([p[0][0], p[1][0], p[2][0]])
                if us != abs(ss):
                    equal_sign = False
    # now find the one with the lowest acceleration
    acc = [sum([abs(a) for a in p[2]]) for p in particles]
    return acc.index(min(acc))


def part_2(particles):
    stop = False
    # loop till slowest is closest to zero
    while not stop:
        stop = True
        pos = {}
        for p in particles:
            for j in range(3):
                p[1][j] += p[2][j]
                p[0][j] += p[1][j]
            s = tuple(p[0])
            if s in pos:
                pos[s] += 1
            else:
                pos[s] = 1
        # check which ones that are the same pos
        np = []
        for p in particles:
            if pos[tuple(p[0])] == 1:
                np.append(p)
        particles = np
        # search for slowest part
        for p in particles:
            if stop:
                us = sum([abs(a) for a in [p[0][0], p[1][0], p[2][0]]])
                ss = sum([p[0][0], p[1][0], p[2][0]])
                if us != abs(ss):
                    stop = False
        # check for closest
        if stop:
            acc = [sum([abs(a) for a in p[2]]) for p in particles]
            i = acc.index(min(acc))
            mhd = [sum([abs(a) for a in p[0]]) for p in particles]
            if i != mhd.index(min(mhd)):
                stop = False
    return len(particles)


def main():
    fh = open('./input', 'r')
    data = [line.strip('\n') for line in fh]
    fh.close()
    # assert part1 = 258   part2 = 841 (too high)
    particles = read_data(data)
    print("part1 = %d" % part_1(particles[:]))
    particles = read_data(data)
    print("part2 = %d" % part_2(particles[:]))
    # print("part2 = %d" % part_2(data))


if __name__ == '__main__':
    main()
