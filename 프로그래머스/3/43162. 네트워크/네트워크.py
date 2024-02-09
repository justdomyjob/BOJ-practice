from collections import deque
def solution(n, computers):
    visited = [-1 for _ in range(n)]
    
    def bfs(start):
        visited[start] = 1
        q = deque()
        q.append(start)
        while q:
            v  = q.pop()
            for i in range(n):
                if computers[v][i]==1 and visited[i]==-1:
                    visited[i] = 1
                    q.append(i)
    count = 0
    for i in range(n):
        if visited[i]==-1:
            bfs(i)
            count+=1
    return count