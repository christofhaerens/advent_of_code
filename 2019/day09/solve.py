#!/usr/bin/python3

import re
from collections import defaultdict
from itertools import permutations

day = "--- Day 9 - 2019 ---"
POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2


class Intcode(object):
    """docstring for intcode."""

    F = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        7: lambda x, y: 1 if x < y else 0,
        8: lambda x, y: 1 if x == y else 0,
    }

    def __init__(self, code, phase):
        self.code = defaultdict(lambda: 0)
        for idx, c in enumerate(code):
            self.code[idx] = c
        self.phase = phase
        self.pointer = 0
        self.relative_base = 0
        self.inputs = [] if phase is None else [phase]
        self.state = 'start'
        self.output = None
        self.len = len(code)

    def evaluate_param(self, param, mode):
        if mode == POSITION_MODE:
            return self.code[param]
        elif mode == RELATIVE_MODE:
            return self.code[self.relative_base + param]
        return param

    def fetch_params(self, param_count, start=1):
        p = self.pointer + start
        return self.code[p] if param_count == 1 else [self.code[d] for d in range(p, p + param_count)]

    def process(self, test_mode=False):
        opcode = self.code[self.pointer] % 100
        if test_mode:
            if opcode != 99 and self.output is not None:
                # print("Test = %d" % self.output)
                if self.output != 0:
                    raise RuntimeError('ERROR: test failed (%d)' % self.output)
            self.output = None
        mode1 = (self.code[self.pointer] // 100) % 10  # 1 = immediate, 0 = position
        mode2 = (self.code[self.pointer] // 1000) % 10  # 1 = immediate, 0 = position
        mode3 = (self.code[self.pointer] // 10000) % 10  # 1 = immediate, 0 = position
        # print("inputs = %r, pointer = %d, base = %d, opcode = %d, code = %r" % (self.inputs, self.pointer, self.relative_base, opcode, self.fetch_params(4, 0)))
        if opcode in [1, 2, 7, 8]:
            p1, p2, p3 = self.fetch_params(3)
            v1 = self.evaluate_param(p1, mode1)
            v2 = self.evaluate_param(p2, mode2)
            pos = p3 if mode3 == POSITION_MODE else p3 + self.relative_base
            self.code[pos] = Intcode.F[opcode](v1, v2)
            self.pointer += 4
        elif opcode == 3:  # need input
            p1 = self.fetch_params(1)
            pos = p1 if mode1 == POSITION_MODE else p1 + self.relative_base
            self.code[pos] = self.inputs.pop(0)
            self.pointer += 2
        elif opcode == 4:  # output
            p1 = self.fetch_params(1)
            self.output = self.evaluate_param(p1, mode1)
            self.pointer += 2
        elif opcode in [5, 6]:  # 5=jump if true (non-zero), 6=jump if false (zero)
            p1, p2 = self.fetch_params(2)
            v1 = self.evaluate_param(p1, mode1)
            if (opcode == 5 and v1 != 0) or (opcode == 6 and v1 == 0):
                self.pointer = self.evaluate_param(p2, mode2)
            else:
                self.pointer += 3
        elif opcode == 9:
            p1 = self.fetch_params(1)
            v1 = self.evaluate_param(p1, mode1)
            self.relative_base += v1
            self.pointer += 2
        elif opcode == 99:  # halt
            self.state = 'halt'
            self.pointer += 1
        else:
            raise RuntimeError('unexpected')
        return opcode

    def run(self, code_input, test_mode=True):
        # in test_mode the program halts with an error if an output != 0 is produced before the program ends (opcode 99)
        opcode = 0
        last_output = None
        if code_input is not None:
            self.inputs.append(code_input)
        while opcode != 99:
            opcode = self.process(test_mode)
            if opcode == 4:
                last_output = self.output
                self.inputs.append(self.output)
        return last_output

    def feedback_run(self, code_input):
        opcode = 0
        if input is not None:
            self.inputs.append(code_input)
        while opcode not in [4, 99]:
            opcode = self.process()
        return self.output


def solve1(data):
    prog = Intcode(data.copy(), None)
    return prog.run(1)


def solve2(data):
    prog = Intcode(data.copy(), None)
    return prog.run(2)


def solve(data):
    a1, a2 = (0, 0)
    print("\n%s" % day)
    a1 = solve1(data.copy())
    print("part1 = %r" % a1)
    a2 = solve2(data.copy())
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    i = [line.strip().split(',') for line in fh]
    data = [int(d) for d in i[0]]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
