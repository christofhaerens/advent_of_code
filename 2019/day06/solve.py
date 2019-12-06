#!/usr/bin/python3

import re
from collections import defaultdict

day = "--- Day 6 - 2019 ---"


def do(data, part=1):
    orbiting_planets = defaultdict(lambda: [])
    parent_planet = {}
    for p, op in data:  # p = planet, op = orbiting planet
        orbiting_planets[p].append(op)
        parent_planet[op] = p
    planets = orbiting_planets.keys()
    orbiters = parent_planet.keys()
    com = list(set(planets)-set(orbiters))[0]  # com is not orbiting
    if part == 1:
        count = 0
        for planet in orbiters:
            while planet != com:  # count until com
                planet = parent_planet[planet]
                count += 1
        return count
    # part 2
    you, san = 'YOU', 'SAN'
    # find shortest path from you to san
    routes = []  # keep track of our routes
    planets_passed = defaultdict(int)
    routes.append([parent_planet[you]])  # start with our parent planet
    while True:
        newroutes = []
        for route in routes:
            # get the last planet from the route
            p = route[-1]
            if p == san:  # did we found san?
                return len(route) - 2  # don't count start and end
            else:  # neighbour planets = orbiting + parent
                neighbour_planets = orbiting_planets[p]
                if p != com:  # com has no parent
                    neighbour_planets.append(parent_planet[p])
                for ap in neighbour_planets:  # ap = adjecedant planets
                    if planets_passed[ap] == 0:
                        newroute = route[:] + [ap]
                        newroutes.append(newroute)
                        planets_passed[ap] = 1
        routes = newroutes.copy()
        if len(routes) == 0:
            return "Error: no route found"


def solve1(data):
    return do(data, part=1)


def solve2(data):
    return do(data, part=2)


def solve(data):
    a1, a2 = (0, 0)
    a1 = solve1(data)
    a2 = solve2(data)
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    input = [line.strip() for line in fh]
    fh.close()
    data = [d.split(')') for d in input]
    solve(data)


if __name__ == '__main__':
    main()
