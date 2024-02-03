import copy
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,0,1,0], [0,1,0,-1]


def bfs_air(i,j):
    visited[i][j] = 1
    graph[i][j] = 2
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.pop()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<=ni<n and 0<=nj<m and graph[ni][nj] in [0,2]:
                if visited[ni][nj]==-1:
                    graph[ni][nj] = 2
                    visited[ni][nj] = 1
                    q.append((ni,nj))

def bfs(i,j):
    num=1
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.pop()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<=ni<n and 0<=nj<m and graph[ni][nj]==1:
                if visited[ni][nj]==-1:
                    num+=1
                    visited[ni][nj] = 1
                    q.append((ni,nj))
    return num

def melt():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            for k in range(4):
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 2:
                        new_graph[i][j] = 2
    graph = new_graph

cheeze_list =[]
while True:
    num_cheeze = 0
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    bfs_air(0,0)
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and visited[i][j]==-1:
                cheeze = bfs(i,j)
                num_cheeze+=cheeze
    melt()
    if num_cheeze ==0:
        break
    cheeze_list.append(num_cheeze)
print(len(cheeze_list))
print(cheeze_list[-1])