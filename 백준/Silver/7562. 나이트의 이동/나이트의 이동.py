from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

steps = [(2,1),(1,2),(-2,1),(-1,2),(1,-2),(2,-1),(-1,-2),(-2,-1)]

def move(x,y,max_chess):
    ret = []
    for step in steps:
        x1 =x+step[0]
        y1 =y+step[1]
        if 0 <= x1 <= max_chess-1 and 0<= y1 <= max_chess-1:
            ret.append((x1,y1))
    return ret
def bfs(x,y,visited,max_chess,endx,endy):
    visited[y][x] = 0
    node = deque()
    node.append((x,y))
    while node:
        x1,y1 = node.popleft()
        for x2,y2 in move(x1,y1,max_chess):
            if visited[y2][x2] == -1:
                visited[y2][x2] = visited[y1][x1] + 1
                node.append((x2,y2))
    return visited[endy][endx]
N = int(input())
for _ in range(N):
    length = int(input())
    x,y = map(int,input().split())
    endx,endy = map(int,input().split())
    visited = [[-1 for _ in range(length)] for _ in range(length)]
    print(bfs(x,y,visited,length,endx,endy))