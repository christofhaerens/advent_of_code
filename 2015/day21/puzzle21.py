#!/usr/bin/python3

shop = {}
weapons:    Cost  Damage  Armor
'weapon': Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

def part_1(data):
    sum = 0
    return sum


def main():
    boss = {'hp': 104, 'damage': 8, 'armor': 1}
    # assert part1 =    part2 =
    print("part1 = %d" % part_1(boss))
    # print("part2 = %d" % part_2(data))


if __name__ == '__main__':
    main()
