#!/usr/bin/python3

import re


class Ingredient:
    def __init__(self, data):
        self.name = data[0]
        self.capacity = int(data[1])
        self.durability = int(data[2])
        self.flavor = int(data[3])
        self.texture = int(data[4])
        self.calories = int(data[5])

    def score(self, spoons):
        return self.capacity * spoons
    # capacity 4, durability -2, flavor 0, texture 0, calories


class Cake:
    def __init__(self):
        self.ing_dict = {}
        self.ing_names = []

    def add_ingredient(self, i):
        self.ing_dict[i.name] = i
        self.ing_names.append(i.name)

    def get_ingredients(self):
        return list(self.ing_dict.values())

    def find_ingredient(self, name):
        return self.ing_dict[name]

    def score(self, spoons):
        score = 0
        for i in ing_dict.values():
            score += 0



def part_1_2(data):
    cake = Cake()
    for v in data:
        i = Ingredient(v)
        cake.add_ingredient(i)
    return 0, 0


def main():
    fh = open('./input', 'r')
    # Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
    r = re.compile('^(\w+): capacity ([\d-]+), durability ([\d-]+), flavor ([\d-]+), texture ([\d-]+), calories ([\d-]+)')
    data = [list(m.groups()) for m in [re.match(r, line.strip()) for line in fh]]
    fh.close()
    print(data)
    # assert part1 =    part2 =
    print("part1 = %d\npart2 = %d\n" % part_1_2(data))

if __name__ == '__main__':
    main()
