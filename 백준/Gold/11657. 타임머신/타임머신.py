import sys

N, M = map(int,sys.stdin.readline().rstrip().split())
INF = 10**9
edges = []
dist = [INF] *(N+1)

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    edges.append((a,b,c))

def bf(start):
    dist[start] = 0
    for i in range(N):
        for a,b,c in edges:
            if dist[a]!=INF and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c
                if i==N-1:
                    return False
    return True

if bf(1)==False:
    print(-1)
    exit(0)

for i in range(2,N+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])