import sys
n, m = map(int,input().split())
BLANK,CHEEZE,AIR = 0,1,2
graph = [list(map(int, input().split())) for _ in range(n)]

dy,dx = [-1,0,1,0],[0,1,0,-1]
sys.setrecursionlimit(10**5)
def dfs_air(i,j):
    visited[i][j] = 1
    graph[i][j] = AIR
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0<=ni<n and 0<=nj<m and graph[ni][nj] in [BLANK,AIR]:
            if visited[ni][nj] == -1:
                dfs_air(ni,nj)

def melt(i,j):
    global graph
    temp_graph = [array[:] for array in graph]
    dfs_melt(i, j,temp_graph)
    graph = temp_graph

def dfs_melt(i,j,temp_graph):
    visited[i][j] = 1
    count_air = 0
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if 0<=ni<n and 0<=nj<m and graph[ni][nj] == CHEEZE:
            if visited[ni][nj] == -1:
                dfs_melt(ni,nj,temp_graph)
        if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == AIR:
            count_air+=1
    if count_air>=2:
        temp_graph[i][j] = BLANK

time = 0
while True:
    count = 0
    visited = [[-1] * m for _ in range(n)]
    dfs_air(0, 0)
    for i in range(n):
        for j in range(m):
            if graph[i][j]==CHEEZE and visited[i][j]==-1:
                melt(i,j)
                count+=1
    if count==0:
        break
    time += 1
print(time)