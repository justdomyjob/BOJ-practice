from collections import deque

N,Q = map(int,input().split())
R = 2**N
graph = [list(map(int,input().split())) for _ in range(R)]
L = list(map(int,input().split()))

dy = [-1,0,1,0]
dx = [0,1,0,-1]
for l in L:
    length = 2**l  #length*length
    count = R//length #가 한 줄에 count개

    for i in range(count):
        for j in range(count):
            small_graph = graph[i*length:(i+1)*length]
            small_graph = [i[j*length:(j+1)*length] for i in small_graph]
            # for s in small_graph:
            #     print(s)
            # print()
            # temp_graph = [[0 for _ in range(length)] for _ in range(length)]
            for y in range(length):
                for x in range(length):
                    # temp_graph[y][x] = small_graph[length-1-x][y]
                    graph[y+i*length][x+j*length] = small_graph[length-1-x][y]
    new_graph = [[0 for _ in range(R)] for _ in range(R)]
    for i in range(R):
        for j in range(R):
            if graph[i][j]==0:
                continue
            count = 0
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0<=ni<R and 0<=nj<R and graph[ni][nj] > 0: #얼음인지 체크
                    count+=1
            if count < 3:
                new_graph[i][j] = graph[i][j]-1
            else:
                new_graph[i][j] = graph[i][j]
    graph = new_graph



count = 0
for i in range(R):
    for j in range(R):
        count += graph[i][j]
print(count)

def bfs(i,j,visited):
    visited[i][j] = True
    ret = 1
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i+ dy[k]
            nj = j+ dx[k]
            if 0<=ni<R and 0<=nj<R and visited[ni][nj]==False and graph[ni][nj] >0:
                visited[ni][nj] = True
                ret+=1
                q.append((ni,nj))
    return ret
visited = [[False for _ in range(R)] for _ in range(R)]
maximum = 0

for i in range(R):
    for j in range(R):
        if graph[i][j]> 0 and visited[i][j] == False:
            maximum = max(maximum,bfs(i,j,visited))
print(maximum)