from collections import deque

N,M,T = map(int,input().split())
graph = [deque(list(map(int,input().split()))) for _ in range(N)]
rotates = [list(map(int,input().split())) for _ in range(T)]

CLOCKWISE = 0
COUNTER_CLOCKWISE = 1

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def have_same(i,j):
    number = graph[i][j]
    if number==0:
        return False
    for k in range(4):
        ni = i + dy[k]
        nj = (j + dx[k])%M
        if 0<=ni<N and graph[ni][nj] == number:
            return True
    return False

def bfs(i,j,visited):
    number = graph[i][j]
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dy[k]
            nj = (j + dx[k]) % M
            if 0 <= ni < N and graph[ni][nj] == number and visited[ni][nj] == False:
                visited[ni][nj] = True
                q.append((ni,nj))
def check():
    visited = [[False for _ in range(M)] for _ in range(N)]
    ret = False
    for i in range(N):
        for j in range(M):
            if have_same(i,j):
                ret = True
                bfs(i,j,visited)
    for i in range(N):
        for j in range(M):
            if visited[i][j] ==True:
                graph[i][j] = 0
    return ret

def process():
    global graph
    s = 0
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                s+=graph[i][j]
                count+=1
    if count == 0:
        return
    average = s/count
    new_graph = []
    for line in graph:
        new_line = deque()
        for a in line:
            if a==0:
                new_line.append(a)
            else:
                if a>average:
                    new_line.append(a-1)
                elif a<average:
                    new_line.append(a+1)
                else:
                    new_line.append(a)
        new_graph.append(new_line)
    graph = new_graph
def pp():
    for g in graph:
        print(g)
    print()

for x,d,k in rotates:
    for index, line in enumerate(graph):
        if (index + 1) % x ==0:
            if d == CLOCKWISE:
                line.rotate(k)
            else:
                line.rotate(-k)
    if check():

        continue
    else:

        process()
ret = 0
for i in range(N):
    for j in range(M):
       ret += graph[i][j]
print(ret)

