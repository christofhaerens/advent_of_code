#!/usr/bin/python3
import time
import re
# import itertools
# import functools
# from collections import Counter
from collections import defaultdict
# from collections import deque

day = "--- Day 19 - 2020 ---"


def parse_input(data):
    rules = {}
    messages = []
    rules_input = True
    for line in data:
        if line == "":
            rules_input = False
            continue
        if rules_input:
            m = re.match(r"^(\d+): (.*)$", line)
            i, r = m.groups()
            rules[i] = [x.split(" ") for x in r.strip('"').split(" | ")]
        else:
            messages.append(line)
    return [rules, messages]


def expand_rule(rules, rule_idx):
    while True:
        expanded = False
        new_rule = []
        for i, r0 in enumerate(rules[rule_idx]):
            x = [[]]
            for j, el in enumerate(r0):
                if el in rules:
                    expanded = True
                    y = []
                    for r in rules[el]:
                        for v in x:
                            y.append(v + r)
                    x = y
                else:
                    for i, v in enumerate(x):
                        x[i] = v + [el]
            for v in x:
                new_rule.append(v)
        rules[rule_idx] = new_rule
        if not expanded:
            break
    return rules[rule_idx]


def expand_rules(rules):
    # lets search for rules that needs least expanding
    # create a set that holds all the rules, and also find the a,b rule
    ruleset_idx = defaultdict(lambda: set())
    expanded_idxs_set = set()
    for idx, rule in rules.items():
        for r in rule:
            for el in r:
                ruleset_idx[idx].add(el)
        if ruleset_idx[idx].union({'a', 'b'}) == {'a', 'b'}:
            expanded_idxs_set.add(idx)
    # now search rules that only have expanded_rules as set members
    while True:
        found = 0
        for idx, rule_set in ruleset_idx.items():
            if idx in expanded_idxs_set:  # this rule is already expanded, look no further
                continue
            if rule_set.issubset(expanded_idxs_set):  # all these rules have been expanded before
                new_rule = expand_rule(rules, idx)
                # since this rule is expanded, we can join all letters (makeing further expansion go faster)
                rules[idx] = [["".join(x)] for x in new_rule]
                # print(idx, rules[idx])
                expanded_idxs_set.add(idx)
                found += 1
        if found == 0:
            break
    return rules


def solve1(data):
    rules, messages = data
    c = 0
    rules = expand_rules(rules)
    values = set([x[0] for x in rules['0']])
    for message in messages:
        if message in values:
            c += 1
    return c, rules


def solve2(data, rules):
    # 0: 8 11
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    messages = data[1]
    longest_message = max([len(m) for m in messages])
    # we will use the length of the rules to determine the length of the matching message
    # sinc 8 and 11 trigger a llop, we set them to 0
    rule_len = {'8': 0, '11': 0}
    rule_len['42'] = len(rules['42'][0][0])
    rule_len['31'] = len(rules['31'][0][0])
    # create seperate rules to expand the loop
    rules2 = {}
    rules2['0'] = [['8', '11']]
    rules2['8'] = [['42'], ['42', '&8']]
    rules2['11'] = [['42', '31'], ['42', '&11', '31']]
    while True:  # keep expanding until the shortest loop >= longest message
        rules2['0'] = expand_rule(rules2, '0')
        new_rules = []
        for rule in rules2['0']:
            new_rules.append([x[1:] if x[0] == '&' else x for x in rule])
        rules2['0'] = new_rules
        # the shortest rule with 8 or 11 must >= longest_message
        shortest = []
        for rule in rules2['0']:
            s = [rule_len[x] for x in rule]
            if 0 in s:  # rule_len for '8' and '11' is 0
                shortest.append(sum(s))
        shortest = min(shortest)
        if shortest >= longest_message:  # we have looped deep enough
            break
    # remove 8 and 11 from rules2['0']
    new_rules = []
    for rule in rules2['0']:
        add_rule = True
        for r in rule:
            if r in ['8', '11']:
                add_rule = False
                break
        if add_rule:
            new_rules.append(rule)
    # check messages against rules
    values = {}
    values['42'] = set([x[0] for x in rules['42']])
    values['31'] = set([x[0] for x in rules['31']])
    c = 0
    # calculating all the possible values takes too long
    # instead cut the message in parts according to the rules and match those seperately
    for m in messages:
        mlen = len(m)
        for rule in new_rules:
            r_len = sum([rule_len[x] for x in rule])  # calculate the length of the message this rule will generate
            if r_len != mlen:
                # message and rule have different length; don't bother checking this rule
                continue
            i_start, i_end = 0, 0
            match = True
            # cut the message in parts matching with the length of the rules
            for rule_idx in rule:
                i_end = i_start + rule_len[rule_idx]
                m_part = m[i_start:i_end]
                if m_part not in values[rule_idx]:
                    match = False
                    break
                i_start = i_end
            if match:
                c += 1
                break  # dont bother checking the rest of the rules
    return c


def solve(data):
    print(f"\n{day}\n")
    t = time.perf_counter()
    a1, rules = solve1(data.copy())
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part1 = %r\n" % (a1))
    t = time.perf_counter()
    a2 = solve2(data.copy(), rules)
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part2 = %r\n" % (a2))


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    data = parse_input(data)
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
