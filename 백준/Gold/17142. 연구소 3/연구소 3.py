from collections import deque
from itertools import combinations

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
UNVISITED = -1
BLANK = 0
WALL = 1
VIRUS = 2
viruses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
           viruses.append((i,j))

def bfs(virus_list):
    visited = [[UNVISITED for _ in range(N)] for _ in range(N)]
    q = deque()
    for i,j in virus_list:
        visited[i][j] = 0
        q.append((i,j))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0<=ni <N and 0<=nj<N and visited[ni][nj] == UNVISITED and graph[ni][nj]!=WALL:
                visited[ni][nj] = visited[i][j] +1
                q.append((ni,nj))

    time = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == WALL:
                continue
            else:
                if visited[i][j] == UNVISITED and graph[i][j]== BLANK:
                    return -1
                else:
                    if graph[i][j] == BLANK:
                        time = max(time, visited[i][j])
    return time
time = 10**9
for virus_list in combinations(viruses,M):
    each_time = bfs(virus_list)
    if each_time==-1:
        continue
    else:
        time = min(time,each_time)
if time == 10**9:
    print(-1)
else:
    print(time)