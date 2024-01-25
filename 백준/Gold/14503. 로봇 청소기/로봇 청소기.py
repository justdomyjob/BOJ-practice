import sys

input = sys.stdin.readline

n, m = map(int,input().split())
r,c,d =map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

steps = [(1,0),(-1,0),(0,1),(0,-1)]
count=0
def can(r,c,d):
    next_r, next_c = back(r,c,d)
    if graph[next_r][next_c]==1:
        return False
    return True

def back(r,c,d):
    if d==0:
        next_r = r+1
        next_c = c
    elif d==1:
        next_r = r
        next_c = c-1
    elif d == 2:
        next_r = r-1
        next_c = c
    elif d==3:
        next_r = r
        next_c = c+1
    return (next_r,next_c)

def go(r,c,d):
    if d==0:
        next_r = r-1
        next_c = c
    elif d==1:
        next_r = r
        next_c = c+1
    elif d == 2:
        next_r = r+1
        next_c = c
    elif d==3:
        next_r = r
        next_c = c-1
    return (next_r,next_c)

while True:
    not_clean = False
    if graph[r][c] == 0 :
        count+=1
        graph[r][c] = 2

    for step in steps:
        new_x = r+step[0]
        new_y = c+step[1]
        if graph[new_x][new_y]==0:
            not_clean=True
    if not_clean==True:
        d = (d - 1) % 4
        new_r, new_c = go(r, c, d)
        if graph[new_r][new_c] == 0 :
            r, c = new_r, new_c
    elif not_clean==False:
        if can(r,c,d):
            r,c = back(r,c,d)
        else:
            break
print(count)
