from collections import deque

N, Q = map(int,input().split())
usado = [list(map(int,input().split())) for _ in range(N-1)]
questions = [list(map(int,input().split())) for _ in range(Q)]

edges = [[] for _ in range(N+1)]
for a,b,c in usado:
    edges[a].append((b,c))
    edges[b].append((a,c))

def bfs(k,start):
    visited = [False for _ in range(N+1)]
    visited[start] = True
    q = deque()
    q.append(start)
    ret = 0
    while q:
        v = q.popleft()
        for u,cost in edges[v]:
            if visited[u]== False and cost >= k:
                ret+=1
                visited[u] = True
                q.append(u)
    return ret #자기 자신 제외

for k, v in questions:
    a = bfs(k,v)
    print(a)