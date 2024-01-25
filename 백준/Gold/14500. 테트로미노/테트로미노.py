import sys

input = sys.stdin.readline
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

def op1():
    MAX = 0
    for i in range(n):
        for j in range(m-3):
            temp = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]
            MAX = max(MAX,temp)
    for i in range(n-3):
        for j in range(m):
            temp = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]
            MAX = max(MAX,temp)
    return MAX

def op2():
    MAX = 0
    for i in range(n-1):
        for j in range(m - 1):
            temp = graph[i][j] + graph[i][j + 1] + graph[i+1][j] + graph[i+1][j + 1]
            MAX = max(MAX, temp)
    return MAX

def op3():
    MAX = 0
    for i in range(n-2):
        for j in range(m - 1):
            temp1 = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i][j + 1] #7418
            temp2 = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j + 1] #7412
            temp3 = graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1] + graph[i+2][j] #8521
            temp4 = graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1] + graph[i][j]   #8527
            MAX = max(MAX, temp1,temp2,temp3,temp4)

    for i in range(n - 1):
        for j in range(m - 2):
            temp1 = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j + 2]  #7896
            temp2 = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j]      #7894
            temp3 = graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2] + graph[i][j + 2] #4569
            temp4 = graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2] + graph[i][j]     #4567
            MAX = max(MAX, temp1, temp2, temp3, temp4)
    return MAX

def op4():
    MAX = 0
    for i in range(n-2):
        for j in range(m - 1):
            temp1 = graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j + 1] #7452
            temp2 = graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j] + graph[i+2][j]
            MAX = max(MAX, temp1,temp2)

    for i in range(n - 1):
        for j in range(m - 2):
            temp1 = graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j + 2]
            temp2 = graph[i+1][j] + graph[i+1][j+1] + graph[i][j+1] + graph[i][j+2]
            MAX = max(MAX, temp1, temp2)
    return MAX

def op5():
    MAX = 0
    for i in range(n-2):
        for j in range(m - 1):
            temp1 = graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+1][j + 1]
            temp2 = graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j] + graph[i+2][j+1]
            MAX = max(MAX, temp1,temp2)

    for i in range(n - 1):
        for j in range(m - 2):
            temp1 = graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j + 1]
            temp2 = graph[i+1][j] + graph[i+1][j+1] + graph[i][j+1] + graph[i+1][j+2]
            MAX = max(MAX, temp1, temp2)
    return MAX
print(max(op1(),op2(),op3(),op4(),op5()))