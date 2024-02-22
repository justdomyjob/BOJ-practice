from collections import deque

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]
RAINBOW = 0
BLOCK = -1
BLANK = -2
def pp():
    for g in graph:
        print(g)
    print()


def bfs(i,j,visited):

    color = graph[i][j]
    num_rainbow = 0
    num_count = 1
    visited[i][j].add(color)
    q = deque()
    q.append((i,j))

    while q:
        y,x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<N and graph[ny][nx] == color and color not in visited[ny][nx]:
                visited[ny][nx].add(color)
                q.append((ny,nx))
                num_count+=1
            elif 0 <= ny < N and 0 <= nx < N and graph[ny][nx] == RAINBOW and color not in visited[ny][nx]:
                visited[ny][nx].add(color)
                q.append((ny,nx))
                num_count+=1
                num_rainbow+=1
    return num_count,num_rainbow

def bfs_delete(i,j):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[i][j] = True
    color = graph[i][j]
    q = deque()
    q.append((i,j))
    while q:
        y, x = q.popleft()
        graph[y][x] = BLANK
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] in [color,RAINBOW] and visited[ny][nx] == False:
                visited[ny][nx] =True
                q.append((ny, nx))

def gravity():
    for i in range(N-2,-1,-1):
        for j in range(N):
            if graph[i][j] >=0:
                if graph[i+1][j] !=BLANK:
                    continue
                for k in range(i+1,N):
                    if k==N-1 or graph[k+1][j] != BLANK:
                        graph[k][j] = graph[i][j]
                        graph[i][j] = BLANK
                        break
def rotate():
    global graph
    new_graph = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_graph[i][j] = graph[j][N-1-i]
    graph = new_graph

score = 0
while True:
    group = []
    visited = [[set() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and graph[i][j] not in visited:
                count,rainbow = bfs(i,j,visited)
                if count >1:
                    group.append((count,rainbow,i,j,graph[i][j]))
    group.sort(key = lambda x:(-x[0],-x[1],-x[2],-x[3]))
    if len(group) == 0:
        break
    else:
        count,rainbow,i,j,color = group[0]
        score += count**2

        bfs_delete(i,j)

        gravity()

        rotate()

        gravity()
print(score)





