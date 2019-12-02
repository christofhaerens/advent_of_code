#!/usr/bin/python3

# --- Day 3: Squares With Three Sides ---

fh = open('./f3', 'r')
# fh = ['5 25 10']
c = 0
for line in fh:
    a = list(map(int, line.strip().split()))
    a.sort()
    if (a[0] + a[1]) > a[2]:
        c += 1
        print(a)

print("c = %d" % c)


# part2
fh = open('./f3', 'r')
b = []
i = 0
a1, a2, a3 = [], [], []
for line in fh:
    i += 1
    a = list(map(int, line.strip().split()))
    a1.append(a[0])
    a2.append(a[1])
    a3.append(a[2])
    if i == 3:
        b.append(a1)
        b.append(a2)
        b.append(a3)
        i = 0
        a1, a2, a3 = [], [], []
        print(b)

c = 0
for a in b:
    a.sort()
    if (a[0] + a[1]) > a[2]:
        c += 1
        print(a)

print("c = %d" % c)
