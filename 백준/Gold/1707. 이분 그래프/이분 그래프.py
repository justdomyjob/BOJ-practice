import sys
sys.setrecursionlimit(10**6)
def dfs(x):
    if visited[x]==-1:
        visited[x] = 0
    for x1 in edge[x]:
        if visited[x1]==-1:
            visited[x1] = visited[x] + 1   
            if dfs(x1)=="NO": #dfs값이 YES면 return하지말고 계속 해야됨
                return "NO"
        elif visited[x1]!=-1 and (visited[x1]-visited[x])%2==0:
            return "NO"
    return "YES"
K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    V, E = map(int,sys.stdin.readline().rstrip().split())
    edge = [[] for _ in range(V+1)]
    visited = [-1 for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int,sys.stdin.readline().rstrip().split())
        edge[u].append(v)
        edge[v].append(u)
    ans = "YES"
    for i in range(1,V+1):
        if visited[i]==-1:
            ans = dfs(i)
            if ans=="NO":
                print("NO")
                break
    if ans!="NO":    
        print("YES")