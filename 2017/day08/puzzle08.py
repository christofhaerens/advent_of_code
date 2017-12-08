#!/usr/bin/python3

# --- Day 8: I Heard You Like Registers ---

import re


def part_1_2(data):
    reg = {}
    max_found = []
    for instr in data:
        r, op, v, cr, comp, cv = instr
        # make sure our vars exist in the reg
        if r not in reg:
            reg[r] = 0
        if cr not in reg:
            reg[cr] = 0
        new_r = reg[r] + int(v) if op == "inc" else reg[r] - int(v)
        if comp == '==':
            reg[r] = new_r if reg[cr] == int(cv) else reg[r]
        elif comp == '!=':
            reg[r] = new_r if reg[cr] != int(cv) else reg[r]
        elif comp == '>':
            reg[r] = new_r if reg[cr] > int(cv) else reg[r]
        elif comp == '<':
            reg[r] = new_r if reg[cr] < int(cv) else reg[r]
        elif comp == '<=':
            reg[r] = new_r if reg[cr] <= int(cv) else reg[r]
        elif comp == '>=':
            reg[r] = new_r if reg[cr] >= int(cv) else reg[r]
        max_found.append(max([reg[r] for r in reg]))
    return max([reg[r] for r in reg]), max(max_found)


def main():
    fh = open('./input', 'r')
    data = []
    for line in fh:
        # t inc 245 if xq != 0
        m = re.match(r'^(\w+) (\w+) ([\d-]+) if (\w+) (\S+) ([\d-]+)', line.strip())
        if m:
            data.append(m.groups())
    fh.close()
    # assert part1 = 6343  part2 = 7184
    print("part1 = %s\npart2 = %s" % part_1_2(data))


if __name__ == '__main__':
    main()
