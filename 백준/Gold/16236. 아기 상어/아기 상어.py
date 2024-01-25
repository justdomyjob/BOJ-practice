import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            r, c = i, j
size = 2
eat = 0
count = 0
steps = [(1,0),(-1,0), (0,1), (0,-1)]

def go_next(): #메인
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    bfs(r,c,visited,0)
    next_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] not in [-1,0] and 0<graph[i][j]<size:
                next_list.append((visited[i][j],i,j))
    next_list.sort()
    if next_list:
        distance, next_r, next_c = next_list[0]
        go_and_eat(next_r, next_c, distance)
        return
    print(count)
    exit(0)

def go_and_eat(next_r,next_c,distance):
    global eat,size,r,c,count
    graph[next_r][next_c] = 9
    graph[r][c] = 0
    count += distance
    r,c = next_r,next_c
    eat +=1
    if eat==size:
        eat=0
        size+=1

def e(r1,c1):
    ret = []
    for step in steps:
        r2 = r1+step[0]
        c2 = c1 + step[1]
        if 0<= r2<=n-1 and 0<= c2<=n-1 and (graph[r2][c2] <= size or graph[r2][c2]==9):
            ret.append((r2,c2))
    return ret

def bfs(r1,c1,visited,distance):
    visited[r1][c1]=distance
    q = deque()
    q.append((r1,c1,distance))
    while q:
        r1,c1,distance = q.popleft()
        for r2, c2 in e(r1, c1):
            if visited[r2][c2] == -1:
                visited[r2][c2] = distance +1
                q.append((r2,c2,distance+1))

while True:
    go_next()