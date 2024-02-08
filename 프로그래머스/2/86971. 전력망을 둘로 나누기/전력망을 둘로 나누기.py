from collections import deque
def solution(n, wires):
    graph = [[False] * (n+1) for _ in range(n+1)]
    for a,b in wires:
        graph[a][b] = True
        graph[b][a] = True
    def bfs(a,b):
        count = 1
        graph[a][b]=False
        graph[b][a]=False
        visited = [False] *(n+1)
        
        visited[a] =True
        q = deque()
        q.append(a)
        while q:
            v = q.popleft()
            edges = graph[v]
            for i in range(1,n+1):
                if edges[i] == True and visited[i]==False:
                    visited[i]=True
                    q.append(i)
                    count+=1
    
        graph[a][b]=True
        graph[b][a]=True
        return abs(count-(n-count))
    MIN = n
    for a,b in wires:
        difference = bfs(a,b)
        MIN = min(MIN,difference)
    return MIN


