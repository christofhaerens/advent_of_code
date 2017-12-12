#!/usr/bin/python3

# --- Day 13: Knights of the Dinner Table ---

import re
import itertools


class Person:
    def __init__(self, name):
        self.name = name
        self.neighbours = {}

    def add_neighbour(self, neighbour, happiness):
        self.neighbours[neighbour] = happiness

    def happiness(self, p1, p2):
        return self.neighbours[p1.name] + self.neighbours[p2.name]

    def __str__(self):
        return "name: %s (%r)" % (self.name, self.neighbours)


class Table:
    def __init__(self):
        self.persons = []
        self.names = {}

    def find_person(self, name):
        if name in self.names:
            return self.names[name]
        else:
            return False

    def add_person(self, p):
        self.persons.append(p)
        self.names[p.name] = p

    def total_happiness(self, table_order):
        # table_order is an ordered (circular) list of persons
        # to make it circular add first person to the end and the last person in front
        l = len(table_order)
        p = table_order[-1:] + table_order[:] + table_order[0:]
        # loop from 1 to len
        return sum([p[i].happiness(p[i - 1], p[i + 1]) for i in range(1, l + 1)])

    def __str__(self):
        return "names: %r" % (self.names)


# def combinations(a, min=0):
#     if min + 1 >= len(a):
#         yield a
#     else:
#         for p in combinations(a, min + 1):
#             yield p
#         for i in range(min + 1, len(a)):
#             a[min], a[i] = a[i], a[min]
#             for p in combinations(a, min + 1):
#                 yield p
#             a[min], a[i] = a[i], a[min]


def part_1_2(data):
    t = Table()
    # fill the table
    for (name, effect, happiness, neighbour) in data:
        happiness = int(happiness) if effect == 'gain' else -int(happiness)
        p = t.find_person(name)
        if not p:
            p = Person(name)
            t.add_person(p)
        p.add_neighbour(neighbour, happiness)
    # try all combinations and find the best one
    part1 = max([t.total_happiness(c) for c in itertools.permutations(t.persons[:])])
    # add myself
    me = Person('me')
    for p in t.persons[:]:
        p.add_neighbour('me', 0)
        me.add_neighbour(p.name, 0)
    t.add_person(me)
    part2 = max([t.total_happiness(c) for c in itertools.permutations(t.persons[:])])
    return part1, part2


def main():
    fh = open('./input', 'r')
    r = re.compile('^(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.')
    data = [list(m.groups()) for m in [re.match(r, line.strip()) for line in fh]]
    fh.close()
    # assert part1 = 664   part2 =
    print("part1 = %d\npart2 = %d\n" % part_1_2(data))


if __name__ == '__main__':
    main()
