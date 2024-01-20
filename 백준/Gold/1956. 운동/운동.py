import sys

N, M = map(int,sys.stdin.readline().rstrip().split())
INF = 10**9
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a][b] = c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

MIN = INF
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            continue
        if graph[i][j]!= INF and graph[j][i]!=INF:
            MIN = min(MIN, graph[i][j]+graph[j][i])
if MIN ==INF:
    print(-1)
else:
    print(MIN)