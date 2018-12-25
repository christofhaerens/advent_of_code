#!/usr/bin/python3

import re
from collections import defaultdict, Counter
from operator import itemgetter


day = "--- Day 24: Immune System Simulator 20XX ---"


class Army(object):
    def __init__(self):
        self.groups = []

    def group_add(self, group):
        self.groups.append(group)

    def opponents(self, me):
        # return all groups from the other army which have not been targeted yet and have units left
        return [g for g in self.groups if g.army != me.army and not g.targeted and g.units > 0]

    def army_alive(self):
        groups = defaultdict(int)
        units = defaultdict(int)
        for g in self.groups:
            if g.units > 0:
                groups[g.army] += 1
                units[g.army] += g.units
        return [(army, groups[army], units[army]) for army in groups]

    def target_selection(self):
        # make a list of groups that are not dead yet and order based on the effective_power an initiative
        groups = [(g.effective_power(), g.initiative, g) for g in self.groups if g.units > 0]
        groups.sort(key=itemgetter(0, 1), reverse=True)
        for ep, i, me in groups:
            # find the group of the other army to which it would deal the most damage
            damages = sorted([(me.damage_to(o), o.effective_power(), o.initiative, o) for o in self.opponents(me)], key=itemgetter(0, 1, 2), reverse=True)
            if len(damages) > 0:
                # still left to attack?
                damage = damages[0][0]
                if damage > 0:
                    # only select a target if we can deal damage
                    o = damages[0][3]
                    me.attack = o
                    o.targeted = me

    def fight(self):
        # fight while alls teams alive
        units_killed = 1
        while units_killed > 0:  # we can have a situation where no units can be killed (damage < hit_points)
            units_killed = 0
            # mark the targets
            self.target_selection()
            # make a list of attackers, based on the initiative
            attackers = [g for g in self.groups if g.attack]
            attackers.sort(key=lambda g: g.initiative, reverse=True)
            for g in attackers:
                units_killed += g.fight()
            for g in self.groups:
                g.next_round()
        return self.army_alive()

    def print_groups(self):
        for g in self.groups:
            print(g)

    def boost(self, army, points):
        for g in self.groups:
            g.reset()
            if g.army == army:
                g.ap += points


class Group(object):
    def __init__(self, army_name, id, units, hp, special, attack_points, attack_type, initiative):
        self.id = id
        self.army = army_name
        self.units = int(units)
        self.hp = int(hp)
        self.ap = int(attack_points)
        self.at = attack_type
        self.weak = []
        self.initiative = int(initiative)
        self.immune = []
        self.targeted = False
        self.attack = False
        self.org_units = self.units
        self.org_ap = self.ap
        special = special.strip()  # strip spaces
        if len(special) > 1:
            m = re.match(r'\s*\((.*)\)', special)
            special = m.group(1)
            for s in special.split(';'):
                s = s.strip()
                if s.startswith('weak'):
                    self.weak = [x.strip() for x in s[7:].split(',')]
                elif s.startswith('immune'):
                    self.immune = [x.strip() for x in s[9:].split(',')]
                else:
                    raise RuntimeError("Unexpected special (%s)" % s)

    def reset(self):
        self.units = self.org_units
        self.ap = self.org_ap
        self.next_round()

    def next_round(self):
        self.attack = False
        self.targeted = False

    def fight(self):
        if self.units <= 0:
            return 0
        if self.attack:
            other = self.attack
            damage = self.damage_to(other)
            kills = damage // other.hp
            other.units -= kills
            return kills
        else:
            raise RuntimeError("Error: can not attack")

    def effective_power(self):
        return self.units * self.ap

    def damage_to(self, other):
        # calculate the damage if the other would attack us
        if self.at in other.immune:
            return 0
        return self.effective_power() * 2 if self.at in other.weak else self.effective_power()

    def __str__(self):
        return "%s_%d ep:%d  initiative:%d  units:%d  hp:%d  ap:%d  at:%s  weak:%r  immune:%r" % (self.army, self.id, self.effective_power(), self.initiative, self.units, self.hp, self.ap, self.at, self.weak, self.immune)


def solve(data):
    a = Army()
    for d in data:
        if ':' in d:
            a_name = d[:-1]
            id = 1
        elif re.match(r'\s*$', d):
            pass
        else:
            m = re.match(r'(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (\S+) damage at initiative (\d+)', d)
            g = Group(a_name, id, *m.groups())
            a.group_add(g)
            id += 1
    a1 = a.fight()
    for i in range(1, 500):
        a.boost('Immune System', i)
        result = a.fight()
        if len(result) == 1 and result[0][0] == 'Immune System':
            a2 = result
            break
    return [a1[0][2], a2[0][2]]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
