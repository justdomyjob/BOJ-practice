import copy
from collections import deque

N,M,F = map(int,input().split())
passenger_graph = [list(map(int,input().split())) for _ in range(N)]
end_graph = [[set() for _ in range(N)] for _ in range(N)]
y,x = map(int,input().split())
y,x = y-1, x-1
dy= [-1,0,1,0]
dx = [0,1,0,-1]
for i in range(2,M+2):
    y1,x1,y2,x2 = map(int,input().split())
    passenger_graph[y1-1][x1-1] = i
    end_graph[y2 - 1][x2 - 1].add(i)

def p():
    for g in passenger_graph:
        print(g)
    print()
def pp():
    for g in end_graph:
        print(g)
    print()

UNVISITED = -1
WALL = 1
def bfs_1(i,j):
    visited = [[UNVISITED for _ in range(N)] for _ in range(N)]
    visited[i][j] = 0
    q = deque()
    q.append((i,j))
    ret = []
    if passenger_graph[i][j] > 0:
        ret.append((0,i,j,passenger_graph[i][j]))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0<=ni < N and 0<=nj<N and visited[ni][nj] == UNVISITED and passenger_graph[ni][nj]!=WALL:
                visited[ni][nj] = visited[i][j] +1
                q.append((ni,nj))
                if passenger_graph[ni][nj] > 0 :
                    ret.append((visited[ni][nj],ni,nj,passenger_graph[ni][nj]))
    ret.sort()
    return ret

def bfs_2(i,j,who):
    visited = [[UNVISITED for _ in range(N)] for _ in range(N)]
    visited[i][j] = 0
    q = deque()
    q.append((i,j))

    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0<=ni < N and 0<=nj<N and visited[ni][nj] == UNVISITED and passenger_graph[ni][nj]!=WALL:
                visited[ni][nj] = visited[i][j] +1
                q.append((ni,nj))
                if who in end_graph[ni][nj]:
                    return visited[ni][nj],ni,nj


for _ in range(M):
    try:
        distance,y,x,who = bfs_1(y,x)[0]
    except:
        print(-1)
        exit(0)
    if F-distance < 0:
        print(-1)
        exit(0)
    F-=distance
    passenger_graph[y][x] = 0
    try:
        distance,y,x = bfs_2(y,x,who)
    except:
        print(-1)
        exit(0)
    if F-distance <0:
        print(-1)
        exit(0)
    F+=distance
print(F)