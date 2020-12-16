#!/usr/bin/python3
# import itertools
# import functools
import re
# from collections import Counter
from collections import defaultdict

day = "--- Day 16 - 2020 ---"


def parse_input(d):
    tickets = []
    rules = {}
    for line in d:
        m = re.match(r'^[\d,]+$', line)
        if m is not None:
            tickets.append([int(x) for x in line.split(",")])
            continue
        m = re.match(r'^([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
        if m is not None:
            m = m.groups()
            rules[m[0]] = [int(x) for x in m[1:]]
    return rules, tickets


def solve1(data):
    rate = 0
    rules, tickets = parse_input(data)
    for ticket in tickets:
        for value in ticket:
            match_a_rule = False
            for rule in rules.values():
                valid = (value >= rule[0] and value <= rule[1]) or (value >= rule[2] and value <= rule[3])
                if valid:
                    match_a_rule = True
                    break
            if not match_a_rule:
                rate += value
                break
    return rate


def solve2(data):
    rules, tickets = parse_input(data)
    # find invalid_tickets
    valid_tickets = []
    invalid_tickets = set()
    for i, ticket in enumerate(tickets):
        for value in ticket:
            match_a_rule = False
            for rule in rules.values():
                valid = (value >= rule[0] and value <= rule[1]) or (value >= rule[2] and value <= rule[3])
                if valid:
                    match_a_rule = True
                    break
            if not match_a_rule:
                invalid_tickets.add(i)
                break

    for i, ticket in enumerate(tickets):
        if i not in invalid_tickets:
            valid_tickets.append(ticket)

    # check rules with valid tickets and keep track of which rule is valid for a certain position
    rule_count = len(rules)
    field_pos = defaultdict(list)
    for name, rule in rules.items():
        rule = rules[name]
        # check for each field if it is valid in a certain position
        for i in range(rule_count):
            valid = True
            for j, value in enumerate([ticket[i] for ticket in valid_tickets]):
                valid = (value >= rule[0] and value <= rule[1]) or (value >= rule[2] and value <= rule[3])
                if not valid:
                    break
            if valid:
                field_pos[name].append(i)

    # we could take a shortcut and only find the common positions for rules starting with 'departure'
    # but we will solve the thing completely by finding the exact postion
    # keep looping until all fields only have 1 pos
    names = set(rules.keys())
    while True:
        only_1 = set()
        new_names = set()  # don't delete from a set we are iterarting over
        for name in names:
            if len(field_pos[name]) == 1:
                only_1.add(field_pos[name][0])
            else:
                new_names.add(name)
        if len(only_1) == 0:  # no changes, break
            break
        for i in only_1:
            for name in new_names:
                if i in field_pos[name]:
                    field_pos[name].remove(i)
        names = new_names

    # calcalate product with the exact positions
    my_ticket = tickets[0]
    product = 1
    for k, v in field_pos.items():
        if k.startswith("departure"):
            product *= my_ticket[v[0]]
    return product


def solve(data):
    a1 = solve1(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    a2 = solve2(data.copy())
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
