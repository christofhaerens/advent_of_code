#!/usr/bin/python3
import time
# import re
# import itertools
# import functools
# from collections import Counter
# from collections import defaultdict
# from itertools import permutations
from collections import deque

day = "--- Day 22 - 2020 ---"


def parse_input(data):
    p = 0
    deck = {}
    for line in data:
        if line.startswith("P"):
            p += 1
            deck[p] = deque()
        elif line.isdigit():
            deck[p].append(int(line))
    return deck


def play(deck, part=1, sub=1):
    dlen = {}
    c = {}
    history = {1: set(), 2: set()}
    while True:

        if part == 2:  # recursive test
            seen = True
            for i in (1, 2):
                d = tuple(deck[i])
                if d not in history[i]:
                    seen = False
                    history[i].add(d)
            if seen:
                return 1

        c[1], c[2] = deck[1].popleft(), deck[2].popleft()
        dlen[1], dlen[2] = len(deck[1]), len(deck[2])
        if part == 1:
            round_win = 2 if c[2] > c[1] else 1
        else:
            if dlen[1] < c[1] or dlen[2] < c[2]:
                round_win = 2 if c[2] > c[1] else 1
            else:
                new_deck = {}
                for i in (1, 2):
                    new_deck[i] = deque(list(deck[i])[:c[i]])
                round_win = play(new_deck, part, sub + 1)

        round_lost = [1, 2][2 - round_win]
        deck[round_win].extend([c[round_win], c[round_lost]])
        if dlen[round_lost] == 0:
            if sub == 1:
                break
            else:
                return round_win

    score = 0
    for card_value in range(1, len(deck[round_win]) + 1):
        score += (card_value * deck[round_win].pop())
    return score


def solve1(data):
    deck = parse_input(data)
    return play(deck)


def solve2(data):
    deck = parse_input(data)
    return play(deck, part=2)
    # return 0


def solve(data):
    print(f"\n{day}\n")
    t = time.perf_counter()
    a1 = solve1(data.copy())
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part1 = %r\n" % (a1))
    t = time.perf_counter()
    a2 = solve2(data.copy())
    print("process_time = %.3f" % (time.perf_counter() - t))
    print("part2 = %r\n" % (a2))


def main():
    fh = open('./input.txt', 'r')
    data = [line.strip() for line in fh]
    fh.close()
    solve(data)


if __name__ == '__main__':
    main()
