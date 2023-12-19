try : standard_input = open("input.txt", "r")  
except:pass

import sys
sys.setrecursionlimit(10**6)

N, M, R =map(int,sys.stdin.readline().rstrip().split())
V = [i for i in range(N+1)]
E = [[] for _ in range(N+1)] 

for _ in range(M):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    E[a].append(b)
    E[b].append(a)
for e in E:
    e.sort(reverse=True)

visited = [0 for _ in range(N+1)]
order = 0

def dfs(V,E,R):
    global order
    order+=1
    visited[R] = order
    for each in E[R]:
        if visited[each] ==0:
            dfs(V,E,each)
dfs(V,E,R)
for a in visited[1:]:
    print(a)