#!/usr/bin/python3

# --- Day 11: Corporate Policy ---

letters = [x for x in 'abcdefghijklmnopqrstuvwxyz']
invalid_letters = [x for x in 'ilo']


def next_string(data):
    s = [x for x in data]
    i = letters.index(s[-1])
    next_letter = letters[0] if i == 25 else letters[i + 1]
    if i == 25:
        # we need to wrap
        if len(s) == 1:
            s[0] = next_letter
        else:
            s = next_string(s[:len(s) - 1]) + next_letter
    else:
        s[-1] = next_letter
    return ''.join(s)


def valid_pw(pw):
    for c in invalid_letters:
        if c in pw:
            return False
    # check for 3 increasing letters
    valid = False
    l = len(pw)
    for i in range(l - 2):
        if l - i < 3:
            # stop if we have less then 3 chars
            break
        if ord(pw[i]) + 2 == ord(pw[i + 1]) + 1 == ord(pw[i + 2]):
            valid = True
            break
    # was 1st test valid?
    if valid:
        valid = False
    else:
        return False
    # 2nd test ; we need twice same char
    found = []
    for i in range(l - 1):
        if pw[i] == pw[i + 1] and pw[i] not in found:
            found.append(pw[i])
    return len(found) > 1


def find_next_pw(old):
    pw = next_string(old)
    while not valid_pw(pw):
        pw = next_string(pw)
    return pw


def part_1_2(data):
    part1 = find_next_pw(data)
    part2 = find_next_pw(part1)
    return part1, part2


def main():
    fh = open('./input', 'r')
    data = fh.read().strip()
    # data = 'zx'
    fh.close()
    # assert part1 = 675   part2 = 1424
    print("part1 = %s\npart2 = %s" % part_1_2(data))


if __name__ == '__main__':
    main()
