#!/usr/bin/python3

# --- Day 13: Packet Scanners ---


class Scanner:
    def __init__(self, layer, depth):
        self.layer = layer
        self.depth = depth
        self.move_direction = 1
        self.depth_pos = 0

    def move(self, moves=1):
        move_count = 0
        while move_count < moves:
            move_count += 1
            self.depth_pos += self.move_direction
            if self.depth_pos == self.depth - 1 or self.depth_pos == 0:
                self.move_direction = -self.move_direction

    def reset(self):
        self.depth_pos = 0
        self.move_direction = 1

    def get_state(self):
        return (self.layer, self.depth_pos, self.move_direction)

    def set_state(self, p, m):
        self.depth_pos = p
        self.move_direction = m


class Fw:
    def __init__(self):
        self.scanners = {}
        self.layers = []
        self.penalty = 0

    def add_scanner(self, s):
        self.scanners[s.layer] = s
        self.layers.append(s.layer)

    def move_scanners(self, moves=1):
        for s in self.scanners.values():
            s.move(moves)

    def reset_scanners(self):
        for s in self.scanners.values():
            s.reset()

    def get_penalty(self, pd, return_on_caught=False, reset_scanners=True):
        if reset_scanners:
            self.reset_scanners()
        # pd = packet depth the packet is travelling
        penalty = 0
        for i in range(max(self.layers) + 1):
            # print('\n', self.get_state()[:10])
            if i in self.scanners:
                s = self.scanners[i]
                if pd == s.depth_pos:
                    if return_on_caught:
                        # print("caught on layer = ", i)
                        return 1
                    penalty += (i * s.depth)
            self.move_scanners()
        return penalty

    def get_state(self):
        return [s.get_state() for s in self.scanners.values()]

    def set_state(self, states):
        for l, p, m in states:
            self.scanners[l].set_state(p, m)

    def find_delay(self, pd, delay=0):
        penalty = 1
        self.reset_scanners()
        if delay > 0:
            self.move_scanners(delay)
        while penalty > 0:
            delay += 1
            self.move_scanners()
            state = self.get_state()
            penalty = self.get_penalty(pd, return_on_caught=True, reset_scanners=False)
            self.set_state(state)
        return delay


def part_1_2(data):
    fw = Fw()
    for layer, depth in data:
        s = Scanner(layer, depth)
        fw.add_scanner(s)
    return fw.get_penalty(0), fw.find_delay(0, delay=3933121)
    # return 0, fw.find_delay(0, delay=3933121)


def main():
    fh = open('./input', 'r')
    data = [list(map(int, line.strip().split(': '))) for line in fh]
    fh.close()
    # assert part1 = 648   part2 = 3933124
    print("part1 = %d\npart2 = %d" % part_1_2(data))


if __name__ == '__main__':
    main()


# # shorter version stolen from https://github.com/danthelion/advent-of-code-2017

# d = {}
# with open("input") as maf:
#     for line in maf:
#         l = line.strip().split(": ")
#         d[int(l[0])] = int(l[1])
#
# j = len(d)
#
# s = 0
# for i in d.keys():
#     k = d[i]
#     if (i + 0) % (2 * k - 2) == 0:
#         s += i * k
#
# print(s)
#
# de = 0
# ok = False
# layers = list(d.keys())
# layers.sort()
# while not ok:
#     ok = True
#     for i in layers:
#         k = d[i]
#         if (i + de) % (2 * k - 2) == 0:
#             print(de, " caught on layer = ", i)
#             ok = False
#             de += 1
#             break
#
# print(de)
