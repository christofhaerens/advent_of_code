#!/usr/bin/python3

# part1
fh = open('f5', 'r')
count = 0
a = []
for line in fh:
    a.append(int(line.strip()))
fh.close()
# a = [0, 3, 0, 1, -3]

l = len(a)
i = 0
jumps = 0
while i < l:
    j = a[i]
    a[i] += 1
    i = i + j
    jumps += 1

print("jumps = %d" % jumps)
# print(a)

# part 2
fh = open('f5', 'r')
count = 0
a = []
for line in fh:
    a.append(int(line.strip()))
fh.close()

# test
# a = [0, 3, 0, 1, -3]

l = len(a)
i = 0
jumps = 0
while i < l:
    j = a[i]
    if j > 2:
        a[i] -= 1
    else:
        a[i] += 1
    i = i + j
    jumps += 1

print("jumps = %d" % jumps)
# print(a)
