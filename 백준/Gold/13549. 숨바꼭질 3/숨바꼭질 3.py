from collections import deque

n,m = map(int,input().split())

visited = [-1 for _ in range(100001)]
def bfs(start):
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for next in [v-1,v+1]:
            if 0<=next<=100000 and (visited[next]==-1 or visited[next] > visited[v]+1):
                visited[next] = visited[v] +1
                q.append(next)
        if 0<=2*v<=100000 and (visited[2*v]==-1 or visited[2*v] > visited[v]):
            visited[2*v] = visited[v]
            q.append(2*v)
bfs(n)
print(visited[m])