from collections import deque

try : standard_input = open("input.txt", "r")  
except:pass

N = int(input())
M = int(input())
E = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    E[a].append(b)
    E[b].append(a)

visited = [0 for _ in range(N+1)]


node = deque()
def bfs(E,R):
    virus = 0
    visited[R] = 1
    node.append(R)
    while node:
        v = node.popleft()
        for u in E[v]:
            if visited[u]==0:
                visited[u]=1
                node.append(u)
                virus+=1
    return virus
print(bfs(E,1))


