import sys
sys.setrecursionlimit(10**5)
n = int(input())

edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [0 for i in range(n+1)]
parent = [0 for i in range(n+1)]
def dfs(start):
    visited[start] = 1
    for u in edges[start]:
        if visited[u]==0:
            parent[u] = start
            dfs(u)
dfs(1)
for i in range(2,n+1):
    print(parent[i])
