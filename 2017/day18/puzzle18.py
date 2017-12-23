#!/usr/bin/python3

# --- Day 18: Duet ---

import re


class Program:
    def __init__(self, pid, instructions):
        self.instructions = instructions
        self.pid = pid
        self.register = {'p': pid}
        self.queue = []
        self.q_link = None
        self.index = 0  # instruction index
        self.wait = False
        self.snd_count = 0

    def link_queue(self, p):
        self.q_link = p

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
        if i == 'set':
            self.register[x] = y
        elif i == 'mul':
            self.register[x] = value_x * y
        elif i == 'jgz' and value_x > 0:
                self.index += y
                jump = True
        elif i == 'mod':
            self.register[x] = value_x % y
        elif i == 'add':
            self.register[x] = value_x + y
        elif i == 'snd':
            self.q_link.queue.append(value_x)
            self.snd_count += 1
        elif i == 'rcv':
            if len(self.queue) > 0:
                self.register[x] = self.queue.pop(0)
                self.wait = False
            else:
                self.wait = True
        if not self.wait and not jump:
            self.index += 1
        return not self.wait

    def run(self):
        while self.step():
            pass


def part_1(data):
    reg = {}
    index = 0
    freq = 0
    while freq == 0:
        code = data[index]
        i = code[0]
        x = code[1]
        jump = False
        value_x = 0 if x not in reg else reg[x]
        if (len(code)) == 3:
            if re.match(r'[-]*\d+', code[2]):
                y = int(code[2])
            else:
                y = 0 if code[2] not in reg else reg[code[2]]
        if i == 'set':
            reg[x] = y
        elif i == 'mul':
            reg[x] = value_x * y
        elif i == 'jgz' and value_x != 0:
            index += y
            jump = True
        elif i == 'mod':
            reg[x] = value_x % y
        elif i == 'add':
            reg[x] = value_x + y
        elif i == 'snd':
            snd = value_x
        elif i == 'rcv' and value_x != 0:
            freq = snd
        if not jump:
            index += 1
        # print(0, index, code, reg, x, value_x, y)
    return freq


def part_2(data):
    p0 = Program(0, data)
    p1 = Program(1, data)
    p0.q_link = p1
    p1.q_link = p0
    while True:
        p0.run()
        p1.run()
        if len(p0.queue) == 0 and len(p1.queue) == 0:
            break
    return p1.snd_count


def main():
    fh = open('./input', 'r')
    data = [line.strip().split() for line in fh]
    fh.close()
    # assert part1 = 1187   part2 = 5969
    print("part1 = %d" % part_1(data))
    print("part2 = %d" % part_2(data))


if __name__ == '__main__':
    main()
