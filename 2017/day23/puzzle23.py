#!/usr/bin/python3

# --- Day 23: Coprocessor Conflagration ---

import re


class Program:
    def __init__(self, pid, instructions, reg={}):
        self.instructions = instructions
        self.max_index = len(instructions)
        self.pid = pid
        self.register = reg
        self.index = 0  # instruction index
        self.count = 0
        self.inside_loop = False

    def reg(self, x):
        return 0 if x not in self.register else self.register[x]

    def step(self):
        iset = self.instructions[self.index]
        jump = False
        i = iset[0]
        x = iset[1]
        value_x = int(x) if re.match(r'[-]*\d+', x) else self.reg(x)
        if i not in ['snd', 'rcv']:
            y = int(iset[2]) if re.match(r'[-]*\d+', iset[2]) else self.reg(iset[2])
        if self.index == -2:
            pass
        elif i == 'set':
            self.register[x] = y
        elif i == 'mul':
            self.register[x] = value_x * y
            self.count += 1
        elif i == 'jnz' and value_x != 0:
                self.index += y
                jump = True
        elif i == 'sub':
            b, d, e = (self.reg('b'), self.reg('d'), self.reg('e'))
            if self.index == 16 and b >= 109300 and e > 1 and e < b and b % e != 0:
                # increment e till b is divisable by e
                while e < b and b != d * e:
                    e += 1
                self.register[x] = e
                # self.register[x] = value_x - y
            elif self.index == 20 and b >= 109300 and d > 1 and d < b and b % d != 0:
                # increment d till b is divisable by d
                while d < b and b % d != 0:
                    d += 1
                self.register[x] = d
            else:
                self.register[x] = value_x - y
        elif i == 'add':
            self.register[x] = value_x + y
        if not jump:
            self.index += 1
        return self.index < self.max_index

    def run(self):
        while self.step():
            pass


def part_1(data):
    p0 = Program(0, data)
    p0.run()
    return p0.count


def part_2a(data):
    # solve via the Program
    p0 = Program(0, data, reg={'a': 1})
    p0.run()
    return p0.register['h']


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(n**0.5 + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def part_2():
    # solve if you know that h increments by 1 for each non prime number between 109300 and 126300 and with step=17
    h = 0
    for x in range(109300, 126300 + 1, 17):
        l = len(list(divisorGenerator(x)))
        if l > 2:
            h += 1
    return h


def main():
    fh = open('./input', 'r')
    data = [line.strip().split() for line in fh]
    fh.close()
    # assert part1 = 8281   part2 = 911
    print("part1 = %d" % part_1(data))
    # via the Progran
    # print("part2 = %d" % part_2a(data))
    # faster way
    print("part2 = %d" % part_2())


if __name__ == '__main__':
    main()
