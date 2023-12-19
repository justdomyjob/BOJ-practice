try : standard_input = open("input.txt", "r")  
except:pass

import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, R =map(int,sys.stdin.readline().rstrip().split())
V = [i for i in range(N+1)]
E = [[] for _ in range(N+1)] 

for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    E[a].append(b)
    E[b].append(a)
for e in E:
    e.sort()


visited = [0 for _ in range(N+1)]
order = 1
node = deque()

def bfs(V,E,R):
    global order
    visited[R] = order
    node.append(R)
    while node:
        u = node.popleft()
        for v in E[u]:
            if visited[v]==0:
                order+=1
                visited[v]=order
                node.append(v)
bfs(V,E,R)
for a in visited[1:]:
    print(a)