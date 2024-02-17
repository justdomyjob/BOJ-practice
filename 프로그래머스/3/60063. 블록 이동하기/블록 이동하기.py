from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
U,R,D,L = 0,1,2,3
UNVISIT = 10**6
def solution(board):
    N = len(board)
    visited = [[[UNVISIT for _ in range(4)] for _ in range(N+1)] for _ in range(N+1)]
    def check(y1,x1):
        if board[y1-1][x1-1] == 1:
            return False
        else:
            return True
    def bfs(y,x,d):
        visited[y][x][d] = 0
        q= deque()
        q.append((y,x,d))
        while q:
            y,x,d = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                nd = d
                ny2 = ny + dy[d]
                nx2 = nx + dx[d]
                if 1<=ny<=N and 1<=nx<=N and  1<=ny2<=N and 1<=nx2<=N and visited[ny][nx][nd]==UNVISIT and check(ny,nx) and check(ny2,nx2):
                    visited[ny][nx][nd] = visited[y][x][d] + 1
                    q.append((ny,nx,nd))
            ny = y + dy[d] + dy[(d+1)%4]
            nx = x + dx[d] + dx[(d+1)%4]
            ny3 = y + dy[(d+1)%4]
            nx3 = x + dx[(d+1)%4]
            nd = (d-1)%4
            if 1 <= ny <= N and 1 <= nx <= N and visited[ny][nx][nd] == UNVISIT and check(ny,nx) and check(ny3,nx3):
                visited[ny][nx][nd] = visited[y][x][d] + 1
                q.append((ny, nx, nd))
            ny = y + dy[d] + dy[(d - 1) % 4]
            nx = x + dx[d] + dx[(d - 1) % 4]
            ny3 = y + dy[(d - 1) % 4]
            nx3 = x + dx[(d - 1) % 4]
            nd = (d + 1) % 4
            if 1 <= ny <= N and 1 <= nx <= N and visited[ny][nx][nd] == UNVISIT and check(ny,nx) and check(ny3,nx3):
                visited[ny][nx][nd] = visited[y][x][d] + 1
                q.append((ny, nx, nd))
            ny = y
            nx = x
            nd = (d + 1) % 4
            ny2 = ny + dy[nd]
            nx2 = nx + dx[nd]
            ny3 = y + dy[d] + dy[(d+1)%4]
            nx3 = x + dx[d] + dx[(d+1)%4]
            if 1 <= ny2 <= N and 1 <= nx2 <= N and visited[ny][nx][nd] == UNVISIT and check(ny,nx) and check(ny2,nx2) and check(ny3,nx3):
                visited[ny][nx][nd] = visited[y][x][d] + 1
                q.append((ny, nx, nd))
            ny = y
            nx = x
            nd = (d - 1) % 4
            ny2 = ny + dy[nd]
            nx2 = nx + dx[nd]
            ny3 = y + dy[d] + dy[(d - 1) % 4]
            nx3 = x + dx[d] + dx[(d - 1) % 4]
            if 1 <= ny2 <= N and 1 <= nx2 <= N and visited[ny][nx][nd] == UNVISIT and check(ny,nx) and check(ny2,nx2) and check(ny3,nx3):
                visited[ny][nx][nd] = visited[y][x][d] + 1
                q.append((ny, nx, nd))
    bfs(1,1,1)
    # for v in visited:
    #     print(v)
    up = visited[N-1][N]
    left = visited[N][N-1]
    center = visited[N][N]
    ret = min(up[2],left[1],min(center))
    return ret