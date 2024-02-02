import sys

r, c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]

steps = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0 for _ in range(c)] for _ in range(r)]

minus = [[0 for _ in range(c)] for _ in range(r)]
sys.setrecursionlimit(10**4)
def e(i,j):
    ret = []
    for step in steps:
        i1 = i + step[0]
        j1 = j + step[1]
        if 0<=i1<r and 0<=j1<c and graph[i1][j1]!=0:
            ret.append((i1,j1))
    return ret

def check(i,j):
    s = 0
    for step in steps:
        i1 = i + step[0]
        j1 = j + step[1]
        if 0<=i1<r and 0<=j1<c and graph[i1][j1]==0:
            s+=1
    minus[i][j] = s

def dfs(r,c):
    visited[r][c] = 1
    check(r,c)
    for r1,c1 in e(r,c):
        if visited[r1][c1]==0:
            visited[r1][c1] = 1
            dfs(r1,c1)
def melt():
    for i in range(r):
        for j in range(c):
            graph[i][j] = max(graph[i][j]-minus[i][j],0)
def init():
    global visited,minus
    visited = [[0 for _ in range(c)] for _ in range(r)]
    minus = [[0 for _ in range(c)] for _ in range(r)]


year = 0
while True:
    num_component = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j]!=0 and visited[i][j]==0:
                dfs(i,j)
                num_component +=1
    melt()
    init()
    if num_component==0:
        print(0)
        exit(0)
    if num_component>=2:
        print(year)
        exit(0)
    year += 1
