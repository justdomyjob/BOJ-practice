import sys

input = sys.stdin.readline

n,L,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1 for _ in range(n)] for _ in range(n)]
steps = [(1,0),(-1,0),(0,1),(0,-1)]

def u(r,c):
    global L,R
    ret =[]
    for step in steps:
        next_r = step[0] + r
        next_c = step[1] + c
        if 0<=next_r<n and 0<=next_c<n and L<=abs(graph[r][c]-graph[next_r][next_c])<=R:
            ret.append((next_r,next_c))
    return ret

def dfs(r,c, union): #return 연합국수, 연합인구
    union_count = 1
    population = graph[r][c]
    visited[r][c] = union
    for next_r,next_c in u(r,c):
        if visited[next_r][next_c]==-1:
            uc, pop = dfs(next_r,next_c,union)
            union_count+=uc
            population +=pop
    return (union_count,population)


def move():
    global visited
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    union = 0
    populations = {}
    unions = {}
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                un, pop = dfs(i, j, union)
                unions[union], populations[union] = un, pop
                union += 1
    for i in range(n):
        for j in range(n):
            union = visited[i][j]
            graph[i][j] = populations[union] // unions[union]
    return len(unions.keys())

count = 0
while True:
    count+=1
    if move()==n**2:
        print(count-1)
        break
