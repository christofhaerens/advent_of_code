#!/usr/bin/python3

day = "--- Day 1 - 2019 ---"


def calculate_fuel(mass, all):
    total_mass = 0
    calculate = True
    while calculate:
        mass = int(mass / 3) - 2
        if all is False:
            return mass
        if mass > 0:
            total_mass += mass
        else:
            calculate = False
    return total_mass


def solve1(data):
    return sum([calculate_fuel(d, False) for d in data])


def solve2(data):
    return sum([calculate_fuel(d, True) for d in data])


def solve(data):
    a1 = solve1(data)
    a2 = solve2(data)
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [int(line.strip()) for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
