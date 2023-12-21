import sys

graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(9)]
zero_list = []
for j in range(9):
    for i in range(9):
        if graph[j][i]== 0:
            zero_list.append((i,j))
def dfs(n):
    if n==len(zero_list):
        for i in range(9):
            print(*graph[i])
        exit(0)
    for i in range(1,10):
        x,y = zero_list[n]
        if can(x,y,i):
            graph[y][x] = i
            dfs(n+1)
            graph[y][x] = 0
def can(x,y,i):
    for j in range(9):
        if i == graph [j][x]:
            return False
    for j in range(9):
        if i == graph [y][j]:
            return False
    a, b = (x//3) * 3, (y//3) * 3
    for k in range(b,b+3):
        for j in range(a,a+3):
            if graph[k][j] == i:
                return False
    return True
dfs(0)