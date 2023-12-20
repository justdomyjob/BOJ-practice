from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

N, M = map(int,input().split())
map1 = [input().rstrip() for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
visited2 = [[-1 for _ in range(M)] for _ in range(N)]
steps = [(1,0),(-1,0),(0,1),(0,-1)]

# 1. visit했냐
# 2. 벽이냐
# 3. 뚫냐

def u(x,y,isBreaked):
    ret = []
    if isBreaked:
        for step in steps:
            x1 = x +step[0]
            y1 = y +step[1]
            if 0<=x1<=M-1 and 0<=y1<=N-1 and map1[y1][x1]=="0":
                ret.append((x1,y1,isBreaked))
    else:
        for step in steps:
            x1 = x +step[0]
            y1 = y +step[1]
            if 0<=x1<=M-1 and 0<=y1<=N-1 and map1[y1][x1]=="0":
                ret.append((x1,y1,isBreaked))
            elif 0<=x1<=M-1 and 0<=y1<=N-1 and map1[y1][x1]=="1":
                ret.append((x1,y1,not isBreaked))
    return ret

def bfs(x,y,isBreaked):
    visited[x][y] = 0
    node =deque()
    node.append((x,y,isBreaked))
    while node:
        x1,y1,isBreaked1 = node.popleft()
        for x2,y2,isBreaked2 in u(x1,y1,isBreaked1):
            if isBreaked1:
                if visited2[y2][x2] == -1:
                    visited2[y2][x2] = visited2[y1][x1] +1
                    node.append((x2,y2,isBreaked2))
            else:
                if isBreaked2:
                    visited2[y2][x2] = visited[y1][x1] +1
                    node.append((x2,y2,isBreaked2))
                else:
                    if visited[y2][x2] == -1:
                        visited[y2][x2] = visited[y1][x1] +1
                        node.append((x2,y2,isBreaked2))
    if visited[N-1][M-1] == -1 and visited2[N-1][M-1] == -1:
        return -1
    elif visited2[N-1][M-1] == -1:
        return  visited[N-1][M-1] +1
    elif visited[N-1][M-1] == -1:
        return  visited2[N-1][M-1] +1
    else :
        return min(visited[N-1][M-1],visited2[N-1][M-1]) +1
print(bfs(0,0,False))
