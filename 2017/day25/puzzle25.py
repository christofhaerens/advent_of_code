#!/usr/bin/python3

# --- Day 25: The Halting Problem ---

A, B, C, D, E, F = range(6)
RIGHT, LEFT = (1, -1)
STATES = {A: [[1, RIGHT, B], [0, LEFT, F]],
          B: [[0, RIGHT, C], [0, RIGHT, D]],
          C: [[1, LEFT, D], [1, RIGHT, E]],
          D: [[0, LEFT, E], [0, LEFT, D]],
          E: [[0, RIGHT, A], [1, RIGHT, C]],
          F: [[1, LEFT, A], [1, RIGHT, A]]
          }
STEPS = 12794428
START_STATE = A


def part_1(state, steps):
    tape = {}
    index = 0
    for _ in range(steps):
        v = 0 if index not in tape else tape[index]
        tape[index], direction, new_state = state[v]
        state = STATES[new_state]
        index += direction
    return sum(tape.values())


def main():
    # assert part1 = 2832   part2 = reboot printer
    print("part1 = %d" % part_1(STATES[START_STATE], STEPS))
    print("part2 = reboot printer")


if __name__ == '__main__':
    main()
