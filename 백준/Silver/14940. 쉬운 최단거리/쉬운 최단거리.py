import sys
from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

GOAL = 2
CAN = 1
CANT = 0

UNVISITED = -1

visited = [[UNVISITED for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            goal_r,goal_c = i,j
            break

steps = [(1,0),(-1,0),(0,1),(0,-1)]
def e(i,j):
    ret = []
    for step in steps:
        new_i = i+step[0]
        new_j = j+step[1]
        if 0<=new_i<n and 0<=new_j<m:
            if graph[new_i][new_j]==CAN:
                ret.append((new_i,new_j))
    return ret

def bfs(i,j):
    visited[i][j]=0
    q = deque()
    q.append((i,j,0))
    while q:
        i,j,n = q.popleft()
        for i2,j2 in e(i,j):
            if visited[i2][j2]==UNVISITED:
                visited[i2][j2] = n+1
                q.append((i2,j2,n+1))

bfs(goal_r,goal_c)

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            visited[i][j]=0
for v in visited:
    print(*v)
