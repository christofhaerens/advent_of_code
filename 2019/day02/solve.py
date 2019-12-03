#!/usr/bin/python3

day = "--- Day 2 - 2019 ---"


def intcode(data, noun, verb):
    pos = 0
    data[1] = noun
    data[2] = verb
    run = True
    while run:
        opcode = data[pos]
        # print(data[pos:pos + 4])
        if opcode == 99:
            run = False
        else:
            a1, a2, a3 = data[pos + 1:pos + 4]
            pos += 4
            if opcode == 1:
                data[a3] = data[a1] + data[a2]
            elif opcode == 2:
                data[a3] = data[a1] * data[a2]
    return data[0]


def solve1(data):
    return intcode(data.copy(), 12, 2)


def solve2(data):
    r2 = 19690720
    for noun in range(100):
        for verb in range(100):
            if r2 == intcode(data.copy(), noun, verb):
                return noun * 100 + verb


def solve(data):
    print("\n%s" % day)
    print("part1 = %r" % solve1(data))
    print("part2 = %r" % solve2(data))
    print()


def main():
    fh = open('./input.txt', 'r')
    # fh = open('./input_test.txt', 'r')
    input = [line.strip() for line in fh]
    fh.close()
    data = [int(d) for d in input[0].split(',')]
    solve(data)


if __name__ == '__main__':
    main()
