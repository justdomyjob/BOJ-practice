from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

m,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
EMPTY = -1
UNVISTED = -100
visited = [[UNVISTED for _ in range(m)] for _ in range(n)]
start_list = []
steps = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            start_list.append((j,i))
 
def bfs(start_list):
    node = deque()
    for x,y in start_list:
        node.append((x,y))
        visited[y][x] = 0
    while node:
        x,y = node.popleft()
        for step in steps:
            x1 = x + step[0]
            y1 = y + step[1]
            if 0<=x1<=m-1 and 0<=y1<=n-1 and box[y1][x1] != EMPTY and visited[y1][x1]==UNVISTED:
                node.append((x1,y1))
                visited[y1][x1] = visited[y][x] + 1
    for i in range(n):
        for j in range(m):
            if visited[i][j] == UNVISTED and box[i][j] != EMPTY:
                return -1 
    return max(map(max,visited))
print(bfs(start_list))
