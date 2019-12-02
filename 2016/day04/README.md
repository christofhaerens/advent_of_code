#!/usr/bin/python3

# --- Day 4: Security Through Obscurity ---
# => description at the end of this file

import re

fh = open('./f4', 'r')
# fh = ['aaaaa-bbb-z-y-x-123[abxyz]', 'a-b-c-d-e-f-g-h-987[abcde]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']
c = 0
# use this to decrypt (part2)
abc = list('abcdefghijklmnopqrstuvwxyz')
for line in fh:
    m = re.match('^([a-z-]+)(\d+)\[([a-z]+)\]', line)
    name, id, checksum = m.groups()
    h = {}
    for char in name.replace('-', ''):
        if char in h:
            h[char] += 1
        else:
            h[char] = 1
    # now put the chars that have the same count into an hash with key=count and value=array of chars
    z = {}
    for k, v in h.items():
        if v in z:
            z[v].append(k)
            z[v].sort()
        else:
            z[v] = [k]
    kl = list(z)
    kl.sort(reverse=True)
    # add the chars to most in order of most occurences
    most = []
    for k in kl:
        most += z[k]
    # if the first 5 are in checksum then we are good
    most = most[:len(checksum)]
    print(z)
    if ''.join(most) == checksum:
        id = int(id)
        c += id
        # decrypt name
        txt = ''
        for char in name:
            if char == '-':
                txt += ' '
            else:
                txt += abc[(abc.index(char) + id) % 26]
        print(txt, id)

print("c = %d" % c)

# --- Day 4: Security Through Obscurity ---
#
# Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.
#
# Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:
#
#     aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
#     a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
#     not-a-real-room-404[oarel] is a real room.
#     totally-real-room-200[decoy] is not.
#
# Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?
#
# Your puzzle answer was 185371.
# --- Part Two ---
#
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?
#
# Your puzzle answer was 984.
