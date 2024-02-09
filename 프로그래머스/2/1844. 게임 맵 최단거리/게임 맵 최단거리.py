from collections import deque
dy,dx = [-1,0,1,0] , [0,1,0,-1]
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited= [[-1 for _ in range(M)] for _ in range(N)]
    def bfs(y,x):
        visited[y][x] = 1
        q = deque()
        q.append((y,x,1))
        while q:
            y,x,d = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny< N and 0<=nx<M and maps[ny][nx] == 1:
                    if visited[ny][nx] == -1:
                        visited[ny][nx] = d+1
                        q.append((ny,nx,d+1))
    bfs(0,0)
    return visited[-1][-1]