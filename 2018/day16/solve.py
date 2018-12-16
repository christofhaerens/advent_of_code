#!/usr/bin/python3

import re
from collections import defaultdict, Counter


day = "--- Day 16: Chronal Classification ---"


OPCODES = {  # s = sample
    'addr': lambda s: s.before[s.a] + s.before[s.b] == s.after[s.c],
    'addi': lambda s: s.before[s.a] + s.b == s.after[s.c],
    'mulr': lambda s: s.before[s.a] * s.before[s.b] == s.after[s.c],
    'muli': lambda s: s.before[s.a] * s.b == s.after[s.c],
    'banr': lambda s: s.before[s.a] & s.before[s.b] == s.after[s.c],
    'bani': lambda s: s.before[s.a] & s.b == s.after[s.c],
    'borr': lambda s: s.before[s.a] | s.before[s.b] == s.after[s.c],
    'bori': lambda s: s.before[s.a] | s.b == s.after[s.c],
    'setr': lambda s: s.before[s.a] == s.after[s.c],
    'seti': lambda s: s.a == s.after[s.c],
    'gtir': lambda s: (s.a > s.before[s.b] and s.after[s.c] == 1) or (s.a <= s.before[s.b] and s.after[s.c] == 0),
    'gtri': lambda s: (s.before[s.a] > s.b and s.after[s.c] == 1) or (s.before[s.a] <= s.b and s.after[s.c] == 0),
    'gtrr': lambda s: (s.before[s.a] > s.before[s.b] and s.after[s.c] == 1) or (s.before[s.a] <= s.before[s.b] and s.after[s.c] == 0),
    'eqir': lambda s: (s.a == s.before[s.b] and s.after[s.c] == 1) or (s.a != s.before[s.b] and s.after[s.c] == 0),
    'eqri': lambda s: (s.before[s.a] == s.b and s.after[s.c] == 1) or (s.before[s.a] != s.b and s.after[s.c] == 0),
    'eqrr': lambda s: (s.before[s.a] == s.before[s.b] and s.after[s.c] == 1) or (s.before[s.a] != s.before[s.b] and s.after[s.c] == 0),
}

OPERATIONS = {  # r = register, i = instruction
    'addr': lambda r, i: r[i[1]] + r[i[2]],
    'addi': lambda r, i: r[i[1]] + i[2],
    'mulr': lambda r, i: r[i[1]] * r[i[2]],
    'muli': lambda r, i: r[i[1]] * i[2],
    'banr': lambda r, i: r[i[1]] & r[i[2]],
    'bani': lambda r, i: r[i[1]] & i[2],
    'borr': lambda r, i: r[i[1]] | r[i[2]],
    'bori': lambda r, i: r[i[1]] | i[2],
    'setr': lambda r, i: r[i[1]],
    'seti': lambda r, i: i[1],
    'gtir': lambda r, i: 1 if i[1] > r[i[2]] else 0,
    'gtri': lambda r, i: 1 if r[i[1]] > i[2] else 0,
    'gtrr': lambda r, i: 1 if r[i[1]] > r[i[2]] else 0,
    'eqir': lambda r, i: 1 if i[1] == r[i[2]] else 0,
    'eqri': lambda r, i: 1 if r[i[1]] == i[2] else 0,
    'eqrr': lambda r, i: 1 if r[i[1]] == r[i[2]] else 0,
}


class Sample(object):
    def __init__(self, before, instruction, after):
        self.before = [int(x) for x in before[9:-1].split(',')]
        self.instruction = [int(x) for x in instruction.split(' ')]
        self.after = [int(x) for x in after[9:-1].split(',')]
        self.opcode, self.a, self.b, self.c = self.instruction
        self.opcodes = []

    def __str__(self):
        return "before: %r,  after: %r,  instruction: %r" % (self.before, self.after, self.instruction)

    def possible_opcodes(self):
        self.opcodes = [opcode for opcode, f in OPCODES.items() if f(self)]

    def update_opcodes(self, codes):
        self.opcodes = [oc for oc in self.opcodes if oc not in codes]


def solve(data, data2):
    samples = []
    for i in range(0, len(data), 4):
        if data[0].startswith('Before:'):
            s = Sample(data[i], data[i + 1], data[i + 2])
            samples.append(s)
            s.possible_opcodes()

    a1 = len([s for s in samples if len(s.opcodes) > 2])
    # part2
    # first find the opcodes
    opcodes_by_id = {}
    while len(opcodes_by_id) < 16:
        codes_found = {}
        # find opcodes that have 1 match
        for s in samples:
            if len(s.opcodes) == 1:
                codes_found[s.opcodes[0]] = s.opcode
        # some safety
        if len(codes_found) == 0:
            raise RuntimeError("Error: cannot resolve opcodes; infinitive loop")
        # now update the samples with the found info
        for s in samples:
            s.update_opcodes(codes_found)
        for name, id in codes_found.items():
            opcodes_by_id[id] = name
    # now run the program
    operations = {}
    for id, name in opcodes_by_id.items():
        operations[id] = OPERATIONS[name]
    r = [0] * 4
    for d in data2:
        i = [int(x) for x in d.split(' ')]
        r[i[3]] = operations[i[0]](r, i)
    return [a1, r[0]]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    fh = open('./input2.txt', 'r')
    data2 = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data, data2))


if __name__ == '__main__':
    main()
