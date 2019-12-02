#!/usr/bin/python3

import re


def part_1(molecule, replacements):
    count = 0
    possible = {}
    s = molecule
    for r in replacements:
        pos = 0
        while True:
            pos = molecule.find(molecule, pos)
            if pos >= 0
            
    return count


def parse_data(data):
    replacements = {}
    for d in data:
        if '=' in d:
            el, r = d.split(' => ')
            if el in replacements:
                replacements[el].append(r)
            else:
                replacements[el] = [r]
        elif d:
            molecule = d
    print(replacements, molecule)
    return molecule, replacements


def main():
    fh = open('./input', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    molecule, replacements = parse_data(data)
    # assert part1 =    part2 =
    print("part1 = %d" % part_1(molecule, replacements))
    # print("part2 = %d" % part_2(data))


if __name__ == '__main__':
    main()
