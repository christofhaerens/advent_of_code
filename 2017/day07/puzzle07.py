#!/usr/bin/python3

# --- Day 7: Recursive Circus ---

import re


class member:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.kinderen = []

    def add_child(self, child):
        self.kinderen.append(child)

    def __str__(self):
        kinderen = []
        total_weight = self.get_weight()
        sum_kinderen = 0
        for kind in self.kinderen:
            weight = kind.get_weight()
            sum_kinderen += weight
            kinderen.append('%s[%d]' % (kind.name, weight))
        return("%s (%d + %d = %d) (%d) -> [%s = %d]" % (self.name, self.weight, sum_kinderen, self.weight + sum_kinderen, total_weight, ', '.join(kinderen), sum_kinderen))

    def find_member(self, name):
        if self.name == name:
            return self
        elif self.kinderen:
            for kind in self.kinderen:
                member = kind.find_member(name)
                if member:
                    return member
        return None

    def get_weight_childeren(self):
        sum = 0
        if self.kinderen:
            for kind in self.kinderen:
                # print(kind.name, kind.weight, sum)
                sum += kind.get_weight()
        return sum

    def get_weight(self):
        return (self.weight + self.get_weight_childeren())


def part_1(data):
    weight_of = {}
    kinderen_van = {}
    ouder_van = {}
    is_geen_ouder = []
    is_ouder = []
    alle_kinderen = []
    for line in data:
        m = re.match('^(\S+)\s+\((\d+)\)', line)
        name, weight = m.groups()
        weight_of[name] = int(weight)
        m = re.match('.*\s+->\s+(.+)$', line.strip())
        if m:
            x = m.groups()[0].split(', ')
            alle_kinderen += x
            kinderen_van[name] = x
            is_ouder.append(name)
            for kind in x:
                ouder_van[kind] = name
        else:
            # no childs
            is_geen_ouder.append(name)

    # find the parent that is no childeren
    for p in is_ouder:
        if p not in alle_kinderen:
            bottom = p

    # now we know the bottom, we can add members
    tree = member(bottom, weight_of[bottom])
    lijst = [bottom]
    while len(is_ouder) > 0:
        ouders = lijst
        lijst = []
        # loop over ouders
        for ouder in ouders:
            # voor elke ouder add de kinderen, als ze kinderen hebben
            if ouder not in is_geen_ouder:
                for child in kinderen_van[ouder]:
                    x = member(child, weight_of[child])
                    tree_member = tree.find_member(ouder)
                    tree_member.add_child(x)
                    # new ouderlist = childeren
                lijst += kinderen_van[ouder]
                # verwijder ouder van de list om aan te geven dat we deze hebben gedaan
                is_ouder.remove(ouder)

    # m = tree.find_member('orflty')
    # print(m)
    # print('-----')
    # for kind in m.kinderen:
    #     print(kind)
    return bottom


def main():
    fh = open('./input', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    # assert part1=vmpywg   part2=1674
    print("part1 = %s\n" % part_1(data))
    # print("part1 = %s\npart2 = %s" % part_1_2(data))


if __name__ == '__main__':
    main()
