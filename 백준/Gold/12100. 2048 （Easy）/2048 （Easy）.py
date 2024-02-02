import copy


def left():
    for i in range(n):
        left_row(i)
    return

def left_row(r):
    global graph
    insert = 0
    temp =0
    for i in range(n):
        if graph[r][i] != 0 and graph[r][i] == temp:
            graph[r][insert - 1] = 2 * graph[r][i]
            temp = 0
        elif graph[r][i] != 0 and graph[r][i] != temp:
            temp = graph[r][i]
            graph[r][insert] = graph[r][i]
            insert += 1
        elif graph[r][i] == 0:
            continue
    for i in range(insert, n):
        graph[r][i] = 0

def right():
    for i in range(n):
        right_row(i)
    return

def right_row(r):
    global graph
    insert = n-1
    temp =0
    for i in range(n-1,-1,-1):
        if graph[r][i] != 0 and graph[r][i] == temp:
            graph[r][insert + 1] = 2 * graph[r][i]
            temp = 0
        elif graph[r][i] != 0 and graph[r][i] != temp:
            temp = graph[r][i]
            graph[r][insert] = graph[r][i]
            insert -= 1
        elif graph[r][i] == 0:
            continue
    for i in range(insert, -1,-1):
        graph[r][i] = 0

def up():
    for i in range(n):
        up_column(i)
    return

def up_column(c):
    global graph
    insert = 0
    temp =0
    for i in range(n):
        if graph[i][c] != 0 and graph[i][c] == temp:
            graph[insert - 1][c] = 2 * graph[i][c]
            temp = 0
        elif graph[i][c] != 0 and graph[i][c] != temp:
            temp = graph[i][c]
            graph[insert][c] = graph[i][c]
            insert += 1
        elif graph[i][c] == 0:
            continue
    for i in range(insert, n):
        graph[i][c] = 0

def down(): #graph row r줄 이거나 row c줄에서 i,j 이동
    for i in range(n):
        down_colum(i)
    return

def down_colum(c):
    global graph
    insert = n-1
    temp =0
    for i in range(n-1,-1,-1):
        if graph[i][c] != 0 and graph[i][c] == temp:
            graph[insert + 1][c] = 2 * graph[i][c]
            temp = 0
        elif graph[i][c] != 0 and graph[i][c] != temp:
            temp = graph[i][c]
            graph[insert][c] = graph[i][c]
            insert -= 1
        elif graph[i][c] == 0:
            continue
    for i in range(insert, -1,-1):
        graph[i][c] = 0

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

MAX = 0
directions = [left,right,up,down]

def dfs(n):
    global MAX,graph
    if n == 5:
        a = [max(i) for i in graph]
        real_max = max(a)
        if real_max > MAX:
            MAX = real_max
        return
    for direction in directions:
        temp = copy.deepcopy(graph)
        direction()
        dfs(n+1)
        graph = temp

dfs(0)
print(MAX)