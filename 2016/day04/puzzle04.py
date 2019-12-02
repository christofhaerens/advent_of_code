#!/usr/bin/python3

# --- Day 4: Security Through Obscurity ---

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
