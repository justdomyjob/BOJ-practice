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

def melt():
    global graph
    temp_graph = [array[:] for array in graph]
    for i in range(n):
        for j in range(m):
            count_air = 0
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == AIR:
                    count_air += 1
            if count_air >= 2:
                temp_graph[i][j] = AIR
    graph = temp_graph

def all_melt():
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                return False
    return True

time = 0
while True:
    visited = [[-1] * m for _ in range(n)]
    dfs_air(0, 0)
    melt()
    time += 1
    if all_melt():
        break
print(time)