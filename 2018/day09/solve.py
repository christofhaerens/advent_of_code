#!/usr/bin/python3

import re
from collections import defaultdict, Counter, deque


day = "--- Day 9: Marble Mania ---"


def high_score(players, marbles):
    circle = deque([0])
    score = defaultdict(int)
    player_list = range(1, players + 1)
    marble = 0
    for i in range(0, marbles):
        marble += 1
        player = player_list[i % players]
        # we keep the active marble is always at the end of our queue
        if (marble % 23) == 0:
            # move queue 7 to the right to pop the value
            circle.rotate(7)
            score[player] += marble + circle.pop()
            # move queue 1 to the left for the active marble
            circle.rotate(-1)
        else:
            # move queue 1 to left to add new marble
            circle.rotate(-1)
            circle.append(marble)
    w = Counter(score)
    return w.most_common(1)[0][1]


def solve(data):
    # data = ['10 players; last marble is worth 1618 points']  # -> 8317
    # data = ['9 players; last marble is worth 25 points']  # -> 32
    m = re.match(r'(\d+) players; last marble is worth (\d+) points', data[0])
    players, marbles = list(map(int, m.groups()))
    return [high_score(players, marbles), high_score(players, marbles * 100)]


def print_answers(a):
    print("\n%s" % day)
    print("part1 = %r" % a[0])
    print("part2 = %r" % a[1])
    print()


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    print_answers(solve(data))


if __name__ == '__main__':
    main()
