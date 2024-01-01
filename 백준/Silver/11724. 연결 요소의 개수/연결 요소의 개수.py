import sys
from collections import deque

N, M = map(int,sys.stdin.readline().rstrip().split())
E = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
visited[0] = 1
for _ in range(M):
    u, v = map(int,sys.stdin.readline().rstrip().split())
    E[u].append(v)
    E[v].append(u)

def bfs(R):
    node = deque()
    visited[R] = 1
    node.append(R)
    while node:
        v = node.pop()
        for u in E[v]:
            if visited[u]==0:
                visited[u]=1
                node.append(u)
                
ans = 0
for i in range(1,N+1):
    if visited[i]==0:
        bfs(i)
        ans += 1
print(ans)
