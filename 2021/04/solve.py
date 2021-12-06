#!/usr/bin/python3
from collections import defaultdict

day = "--- Day 4 - 2021 ---"


def play_bingo(data):
    card_numbers = defaultdict(lambda: [])  # for indexing the cards (cardno, row_idx, col_idx)
    card_rows = []
    card_cols = []

    drawn = [int(f) for f in data[0].split(",")]
    # read the rows
    card_idx = 0
    rows = []
    for r in data[1:]:
        if r == "":
            continue
        rows.append(r.split())
        if len(rows) == 5:
            card_rows.append(rows)
            # transform rows in cols and create index
            cols = []
            for col_idx in range(len(rows[0])):
                col = []
                for row_idx in range(len(rows)):
                    col.append(rows[row_idx][col_idx])
                    card_numbers[int(rows[row_idx][col_idx])].append((card_idx, row_idx, col_idx))  # make an index where we cand find a number
                cols.append(col)
            card_cols.append(cols)
            # reset rows
            rows = []
            card_idx += 1

    # draw the numbers
    winning_cards = []
    winning_draw = {}
    for n in drawn:
        for card in card_numbers[n]:
            card_idx, row_idx, col_idx = card
            if card_idx not in winning_cards:  # only check if this card hasn't won yet
                card_rows[card_idx][row_idx][col_idx] = 'x'
                card_cols[card_idx][col_idx][row_idx] = 'x'
                # did we win?
                if "".join(card_rows[card_idx][row_idx]) == 'xxxxx' or "".join(card_cols[card_idx][col_idx]) == 'xxxxx':
                    winning_cards.append(card_idx)
                    winning_draw[card_idx] = n

    first_sum = sum([int(n) if n != 'x' else 0 for row in card_rows[winning_cards[0]] for n in row])
    last_sum = sum([int(n) if n != 'x' else 0 for row in card_rows[winning_cards[-1]] for n in row])
    return winning_draw[winning_cards[0]] * first_sum, winning_draw[winning_cards[-1]] * last_sum


def solve1(data):
    return play_bingo(data)


def solve2(data):
    return 0


def solve(data):
    a1, a2 = solve1(data.copy())
    print("\n%s" % day)
    print("part1 = %r" % a1)
    print("part2 = %r" % a2)
    print()


def main():
    data = []
    with open('./input.txt', 'r') as fh:
        data = [line.strip() for line in fh]
    solve(data)


if __name__ == '__main__':
    main()
