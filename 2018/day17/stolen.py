from collections import deque
#  '.' = 0, '#' = 1, '|' = 2, '~' = 3
def ch(i):
    return ".#|~"[i]

def print_grid_sub(grid,x1,y1,x2,y2): # Utility
    for y in xrange(y1,y2+1):
        print "".join(ch(grid[y][x]) for x in xrange(x1,x2+1))

W = H = 2100
grid = [[0]*(W+2) for _ in xrange(H+2)]
pmax = [0,0] # max coords
pmin = [W,H] # min coords

for line in open('input.txt').read().splitlines():
    a,b = line.split(", ")
    j = a[0]=='x'
    t = int(a[2:])
    if t > pmax[1-j]:
        pmax[1-j] = t
    elif t < pmin[1-j]:
        pmin[1-j] = t
    tt = map(int,b[2:].split('..'))
    if pmax[j] < tt[1]:
        pmax[j] = tt[1]
    if pmin[j] > tt[0]:
        pmin[j] = tt[0]
    if j:
        for _t in xrange(tt[0],tt[1]+1):
            grid[_t][t] = 1
    else:
        for _t in xrange(tt[0],tt[1]+1):
            grid[t][_t] = 1

spring = [500,0]
xmin,ymin = pmin
xmax,ymax = pmax

belows = deque([spring])
while belows:
    x,y = curr = belows.popleft()
    orig_x, orig_y = x,y
    while y <= ymax and not grid[y][x]: # go down
        grid[y][x] = 2
        y+=1
    if y>ymax: # fall off the edge
        continue
    if grid[y][x]==2: # unstable water: fall already counted
        continue
    else: # clay bottom or stable water bottom
        y-=1
    fall = 0
    while not fall:
        # go left
        while grid[y+1][x-1] and grid[y][x-1]!=1: # haven't reached a fall/wall
            x-=1
            grid[y][x] = 2
        if grid[y][x-1]!=1 and grid[y+1][x-1]!=1: # fall and no wall
            belows.append([x-1,y])
            fall = 1
        # go right
        x = orig_x
        while grid[y+1][x+1] and grid[y][x+1]!=1: # nothing supporting, no blocking wall
            x+=1
            grid[y][x] = 2
        if grid[y][x+1]!=1 and grid[y+1][x+1]!=1: # fall and no wall
            belows.append([x+1,y])
            fall = 1
        x = orig_x
        if fall==0:
            while grid[y][x] in [2,3]: # set this row as stable
                grid[y][x]=3
                x-=1
            x = orig_x
            while grid[y][x] in [2,3]:
                grid[y][x]=3
                x+=1
            x,y = orig_x, y-1 # move up one row
            if grid[y][x]!=2: # make sure to fill it with water
                grid[y][x] = 2

tt = grid[ymax].index(2)
print_grid_sub(grid,tt-10,ymax-100,tt+30,ymax)

tot1=0
tot2=0
for i,row in enumerate(grid):
    if ymin<=i<=ymax:
        tot1+=row.count(2)
        tot2+=row.count(3)
print "part 1:", tot1+tot2
print "part 2:", tot2
