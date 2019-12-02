#!/usr/bin/python3

# part1
fh = open('f4', 'r')
count = 0
for line in fh:
    a = line.strip().split(' ')
    valid = True
    while len(a) > 0:
        w = a.pop()
        if w in a:
            valid = False
            break
    if valid:
        count += 1
fh.close()
print('count valid = %d' % count)

# part 2
fh = open('f4', 'r')
count = 0
for line in fh:
    a = line.strip().split(' ')
    valid = True
    while len(a) > 0:
        w = list(a.pop())
        w.sort()
        if not valid:
            break
        for v in a:
            w2 = list(v)
            w2.sort()
            if w == w2:
                valid = False
                break
    if valid:
        count += 1
fh.close()
print('count valid = %d' % count)
