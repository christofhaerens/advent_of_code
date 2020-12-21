#!/usr/bin/python3
import time
import re
# import itertools
# import functools
# from collections import Counter
# from collections import defaultdict
# from itertools import permutations
# from collections import deque

day = "--- Day 21 - 2020 ---"


def solve1(data):
    ingredients_idx = {}
    allergens_idx = {}
    ingredients = set()
    allergens = set()
    for idx, line in enumerate(data):
        m = re.match(r"^(.+) \(contains (.*)\)", line)
        i, a = m.groups()
        ingredients_idx[idx] = set(i.split(" "))
        allergens_idx[idx] = set(a.split(", "))
        allergens.update(allergens_idx[idx])
        ingredients.update(ingredients_idx[idx])

    map = {}
    mapped_ingredients = set()
    while True:
        found = 0
        # check for each allergen all ingredients and see if we get a single intersection
        for a in allergens:
            if a not in map:  # only search if this isnt mapped yet
                intersect = None
                for idx, a_list in allergens_idx.items():  # check each food
                    if a in a_list:  # and see if allergen is in it
                        # make an intersection of all ingredients that have this allergen
                        if intersect is None:
                            # to initialize the intersect, add ingredients from first match without the ingredients we already mapped
                            intersect = ingredients_idx[idx].difference(mapped_ingredients)
                        else:
                            intersect = intersect.intersection(ingredients_idx[idx])
                        # when we have narrowed down the interset to 1 ingredient, we have a match
                        if len(intersect) == 1:
                            mapped_ingredients.update(intersect)
                            map[a] = intersect.pop()
                            found += 1

        if found == 0:
            break
    c = 0
    # for each food, count how many ingredients are allergen free
    for i in ingredients_idx.values():
        c += len(i.difference(mapped_ingredients))
    # create list of ingredients that have an allergen
    dangerous = [map[a] for a in sorted(map.keys())]
    return c, ",".join(dangerous)


def solve2(data):
    return 0


def solve(data):
    print(f"\n{day}\n")
    t = time.perf_counter()
    a1, a2 = solve1(data.copy())
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part1 = %r\n" % (a1))
    t = time.perf_counter()
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part2 = %r\n" % (a2))


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
