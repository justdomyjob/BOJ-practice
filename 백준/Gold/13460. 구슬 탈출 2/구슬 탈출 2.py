import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int,input().split())
graph = [list(input().rstrip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j]=="R":
            rr,rc=i,j
        elif graph[i][j]=="B":
            br,bc = i,j
visited = []

steps = [(1,0),(-1,0),(0,1),(0,-1)]
def move(r,c,i,j):
    cnt = 0
    while graph[r][c]!="O" and graph[r+i][c+j]!="#":
        r+=i
        c+=j
        cnt +=1
    return r,c,cnt

def bfs(rr,rc,br,bc):
    visited.append((rr,rc,br,bc))
    q = deque()
    q.append((rr,rc,br,bc,0))
    while q:
        rr,rc,br,bc, cnt = q.popleft()
        if cnt >= 10:
            continue
        for step in steps:
            nrr,nrc, cr = move(rr,rc,step[0],step[1])
            nbr,nbc, cb = move(br,bc,step[0],step[1])
            if graph[nbr][nbc] == "O":
                continue
            if graph[nrr][nrc] == "O":
                return cnt+1
            if nrr==nbr and nrc==nbc:
                if cr > cb:
                    nrr-=step[0]
                    nrc-=step[1]
                elif cr < cb:
                    nbr -= step[0]
                    nbc -= step[1]
            if (nrr,nrc,nbr,nbc) not in visited:
                visited.append((nrr,nrc,nbr,nbc))
                q.append((nrr,nrc,nbr,nbc,cnt+1))
    return -1
print(bfs(rr,rc,br,bc))