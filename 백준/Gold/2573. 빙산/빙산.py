from collections import deque

r, c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0 for _ in range(c)] for _ in range(r)]
minus = [[0 for _ in range(c)] for _ in range(r)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< r and 0<=ny < c:
                if graph[nx][ny]!=0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                elif graph[nx][ny]==0:
                    minus[x][y] +=1
def melt():
    for i in range(r):
        for j in range(c):
            graph[i][j] = max(graph[i][j]-minus[i][j],0)
def init():
    global visited,minus
    visited = [[0 for _ in range(c)] for _ in range(r)]
    minus = [[0 for _ in range(c)] for _ in range(r)]

year = 0
while True:
    num_component = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j]!=0 and visited[i][j]==0:
                bfs(i,j)
                num_component +=1
    melt()
    init()
    if num_component==0:
        print(0)
        exit(0)
    if num_component>=2:
        print(year)
        exit(0)
    year += 1