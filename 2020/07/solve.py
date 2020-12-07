#!/usr/bin/python3
# import itertools
# import functools
import re
from collections import defaultdict

day = "--- Day 8 - 2020 ---"


def read_rules(d):
    bags = defaultdict(lambda: [])
    for rule in d:
        b = rule.split(", ")
        m1 = re.match(r'(.+) bags? contain (\S+) (.+) bag', b[0])
        name, count, other = m1.groups()
        if count == "no":
            bags[name] = []
        else:
            bags[name].append([int(count), other])

        for x in b[1:]:
            m1 = re.match(r'(\d+) (.+) bag', x)
            count, other = m1.groups()
            bags[name].append([int(count), other])
    return bags


def part1(d):
    bags = read_rules(d)
    # lookup bag that hold our bag directly
    can_hold = defaultdict(int)
    expand_bags = ['shiny gold']
    while len(expand_bags) > 0:
        new_expand_bags = []
        for name in expand_bags:
            for bag_name in bags.keys():
                if bag_name in expand_bags:
                    continue
                if name in [other[1] for other in bags[bag_name]]:
                    can_hold[bag_name] += 1
                    new_expand_bags.append(bag_name)
        expand_bags = new_expand_bags
    return len(can_hold.keys())


def find_bags(bags, name):
    count = 0
    if len(bags[name]) == 0:
        return count
    else:
        for content in bags[name]:
            count = count + content[0] + (content[0] * find_bags(bags, content[1]))
        return count


def part2(d):
    bags = read_rules(d)
    return find_bags(bags, 'shiny gold')


def solve1(data):
    return part1(data)


def solve2(data):
    return part2(data)


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
