from collections import deque

try : standard_input = open("input.txt", "r")  
except:pass

m,n,h = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
EMPTY = -1
UNVISTED = -100
visited = [[[UNVISTED for _ in range(m)] for _ in range(n)] for _ in range(h)]
start_list = []
steps = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0), (0,0,1), (0,0,-1)]
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                start_list.append((j,i,k))
    
def bfs(start_list):
    node = deque()
    for x,y,z in start_list:
        node.append((x,y,z))
        visited[z][y][x] = 0
    while node:
        x,y,z = node.popleft()
        for step in steps:
            x1 = x + step[0]
            y1 = y + step[1]
            z1 = z + step[2]
            if 0<=x1<=m-1 and 0<=y1<=n-1 and 0<=z1<=h-1 and box[z1][y1][x1] != EMPTY and visited[z1][y1][x1]==UNVISTED:
                node.append((x1,y1,z1))
                visited[z1][y1][x1] = visited[z][y][x] + 1
    max_visited = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if visited[k][i][j] >= max_visited :
                    max_visited = visited[k][i][j]
                if visited[k][i][j] == UNVISTED and box[k][i][j] != EMPTY:
                    return -1                   
    return max_visited
print(bfs(start_list))
