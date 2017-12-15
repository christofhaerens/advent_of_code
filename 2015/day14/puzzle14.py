#!/usr/bin/python3

# --- Day 14: Reindeer Olympics ---

import re


class Reindeer:
    def __init__(self, name, speed, endurance, pause):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.pause = pause
        self.reset()

    def ready(self):
        self.endurance_left = self.endurance
        self.pause_left = self.pause

    def reset(self):
        self.distance = 0
        self.score = 0
        self.ready()

    def distance_step(self):
        if self.endurance_left > 0:
            self.distance += self.speed
            self.endurance_left -= 1
        else:
            self.pause_left -= 1
            if self.pause_left == 0:
                self.ready()
        return self.distance


def part_1_2(data, duration):
    farest = 0
    reindeers = []
    for (name, speed, endurance, pause) in (data):
        reindeers.append(Reindeer(name, int(speed), int(endurance), int(pause)))
    for i in range(duration):
        for r in reindeers:
            d = r.distance_step()
            farest = d if d > farest else farest
        for r in reindeers:
            if r.distance == farest:
                r.score += 1
    winner = reindeers[0]
    for r in reindeers:
        winner = r if r.score > winner.score else winner
    return farest, winner.score


def main():
    fh = open('./input', 'r')
    # Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
    r = re.compile('^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.')
    data = [list(m.groups()) for m in [re.match(r, line.strip()) for line in fh]]
    fh.close()
    print()
    # assert part1 = 2640   part2 = 1102
    print("part1 = %d\npart2 = %d\n" % part_1_2(data, 2503))

if __name__ == '__main__':
    main()
