import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int,sys.stdin.readline().rstrip().split())
E = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
visited[0] = 1

for _ in range(M):
    u, v = map(int,sys.stdin.readline().rstrip().split())
    E[u].append(v)
    E[v].append(u)

def dfs(R):
    visited[R] = 1
    for u in E[R]:
        if visited[u]==0:
            dfs(u)
ans = 0
for i in range(1,N+1):
    if visited[i]==0:
        dfs(i)
        ans += 1
print(ans)
