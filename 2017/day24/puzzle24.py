#!/usr/bin/python3

# --- Day 24: Electromagnetic Moat ---


class Bridge():
    def __init__(self):
        self.parts = {}
        self.free = {}
        self.index = 0
        self.chains = []
        self.max_chain = 0
        self.longest_chain = 0
        self.max_longest_chain = 0

    def add_part(self, a, b):
        self.parts[self.index] = (int(a), int(b))
        self.free[self.index] = True
        self.index += 1

    def free_parts(self):
        for index in range(self.index):
            self.free[index] = True

    def used_parts(self, parts):
        for index in parts:
            self.free[index] = False

    def part_value(self, index):
        return sum(self.parts[index])

    def chain_value(self, chain):
        return sum([self.part_value(x) for x in chain])

    def find_parts(self, n):
        parts = []
        for x in range(self.index):
            for j in (0, 1):
                if self.parts[x][j] == n and self.free[x]:
                    parts.append((x, j))
        return parts

    def build_bridge(self, n, chain=[], level=0):
        if level == 0:
            self.chains = []
            self.max_chain = 0
        parts = self.find_parts(n)
        if len(parts) > 0:
            for p in parts:
                self.free_parts()
                n_chain = chain.copy()
                part, node = p
                n_chain.append(part)
                self.used_parts(n_chain)
                next_node = self.parts[part][node - 1]
                self.build_bridge(next_node, n_chain, level + 1)
        else:
            # self.chains.append(chain)
            cv = self.chain_value(chain)
            if self.max_chain < cv:
                self.max_chain = cv
            l = len(chain)
            if l > self.longest_chain:
                self.max_longest_chain = cv
                self.longest_chain = l
            elif l == self.longest_chain:
                self.max_longest_chain = max((cv, self.max_longest_chain))
        return self.max_chain, self.max_longest_chain

    def __str__(self):
        return "%r" % self.parts


def part_1_2(data):
    b = Bridge()
    for p in data:
        b.add_part(p[0], p[1])
    return b.build_bridge(0)


def main():
    fh = open('./input', 'r')
    data = [line.strip().split('/') for line in fh]
    fh.close()
    # assert part1 = 1511   part2 = 1471
    print("part1 = %d\npart2 = %d" % part_1_2(data))


if __name__ == '__main__':
    main()
