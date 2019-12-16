#!/usr/bin/python3

import re
from collections import defaultdict
from itertools import permutations

day = "--- Day 07 - 2019 ---"


class Intcode(object):
    """docstring for intcode."""

    POSITION_MODE = 0
    F = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        7: lambda x, y: 1 if x < y else 0,
        8: lambda x, y: 1 if x == y else 0,
    }

    def __init__(self, code, phase, mode='test'):
        self.code = code
        self.phase = phase
        self.pointer = 0
        self.inputs = [phase]
        self.state = 'start'
        self.output = None
        self.mode = mode
        self.len = len(code)

    def process(self):
        opcode = self.code[self.pointer] % 100
        mode1 = (self.code[self.pointer] // 100) % 10  # 1 = immediate, 0 = position
        mode2 = (self.code[self.pointer] // 1000) % 10  # 1 = immediate, 0 = position
        # print("inputs = %r, pointer = %d, opcode = %d, code = %r" % (self.inputs, self.pointer, opcode, self.code[self.pointer:min([self.len, self.pointer + 4])]))
        if opcode in [1, 2, 7, 8]:
            p1, p2, p3 = self.code[self.pointer + 1:self.pointer + 4]
            v1 = self.code[p1] if mode1 == Intcode.POSITION_MODE else p1
            v2 = self.code[p2] if mode2 == Intcode.POSITION_MODE else p2
            self.code[p3] = Intcode.F[opcode](v1, v2)
            self.pointer += 4
        elif opcode == 3:  # need input
            p1 = self.code[self.pointer + 1]
            self.code[p1] = self.inputs.pop(0)
            self.pointer += 2
        elif opcode == 4:  # output
            p1 = self.code[self.pointer + 1]
            self.output = self.code[p1] if mode1 == Intcode.POSITION_MODE else p1
            self.pointer += 2
        elif opcode in [5, 6]:  # 5=jump if true (non-zero), 6=jump if false (zero)
            p1, p2 = self.code[self.pointer + 1:self.pointer + 3]
            v1 = self.code[p1] if mode1 == Intcode.POSITION_MODE else p1
            if (opcode == 5 and v1 != 0) or (opcode == 6 and v1 == 0):
                self.pointer = self.code[p2] if mode2 == Intcode.POSITION_MODE else p2
            else:
                self.pointer += 3
        elif opcode == 99:  # halt
            self.state = 'halt'
            self.pointer += 1
        elif self.output is not None:
            # test mode
            if self.output == 0:  # ok, test passed
                self.output = None
            else:
                raise RuntimeError('ERROR: test failed (%d)' % self.output)
        else:
            raise RuntimeError('unexpected')
        return opcode

    def run(self, code_input):
        opcode = 0
        if input is not None:
            self.inputs.append(code_input)
        while opcode != 99:
            opcode = self.process()
            if opcode == 4:
                self.inputs.append(self.output)
        return self.output

    def feedback_run(self, code_input):
        opcode = 0
        if input is not None:
            self.inputs.append(code_input)
        while opcode not in [4, 99]:
            opcode = self.process()
        return self.output


def solve1(data):  # with itertools
    thrust = set()
    phases_list = permutations(range(5))
    for phases in phases_list:
        input = 0
        for p in phases:
            amp = Intcode(data.copy(), p)
            input = amp.run(input)
        thrust.add(input)
    return max(thrust)


def solve2(data):  # with itertools
    thrust = set()
    phases_list = permutations(range(5, 10))
    for phases in phases_list:
        # create the amps
        amp = []
        last_output = 0
        idx = 0
        # init the amps
        for phase in phases:
            amp.append(Intcode(data.copy(), phase))
        # run till output or halt
        while amp[4].state != 'halt':
            last_output = amp[idx].feedback_run(last_output)
            idx = idx + 1 if idx < 4 else 0
        thrust.add(last_output)
    return max(thrust)


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
