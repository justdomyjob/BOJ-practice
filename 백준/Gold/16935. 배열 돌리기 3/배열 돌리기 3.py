import sys

input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
def get_nm(graph):
    n = len(graph)
    m = len(graph[0])
    return (n,m)

def op1(graph):
    n,m = get_nm(graph)
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_graph[n-1-i][j] = graph[i][j]
    return new_graph

def op2(graph):
    n, m = get_nm(graph)
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_graph[i][m-1-j] = graph[i][j]
    return new_graph

def op3(graph):
    n, m = get_nm(graph)
    new_graph = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_graph[i][j] = graph[-(j+1)][i]
    return new_graph

def op4(graph):
    n, m = get_nm(graph)
    new_graph = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_graph[i][j] = graph[j][-(i+1)]
    return new_graph

def op5(graph):
    n , m =get_nm(graph)
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n//2): #1번자리
        for j in range(m//2):
            new_graph[i][j] = graph[i+n//2][j]

    for i in range(n//2): #2번
        for j in range(m//2):
            new_graph[i][j+m//2] = graph[i][j]

    for i in range(n//2): #3
        for j in range(m//2,m):
            new_graph[i+n//2][j] = graph[i][j]

    for i in range(n//2,n): #4
        for j in range(m//2):
            new_graph[i][j] = graph[i][j+m//2]
    return new_graph

def op6(graph):
    n , m =get_nm(graph)
    new_graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n//2): #1번자리
        for j in range(m//2):
            new_graph[i][j] = graph[i][j+m//2]

    for i in range(n//2): #2번
        for j in range(m//2):
            new_graph[i][j+m//2] = graph[i+n//2][j+m//2]

    for i in range(n//2): #3
        for j in range(m//2,m):
            new_graph[i+n//2][j] = graph[i+n//2][j-m//2]

    for i in range(n//2,n): #4
        for j in range(m//2):
            new_graph[i][j] = graph[i-n//2][j]
    return new_graph

operations =list(map(int,input().split()))

for op in operations:
    if op==1:
        graph = op1(graph)
    elif op==2:
        graph = op2(graph)
    elif op==3:
        graph = op3(graph)
    elif op==4:
        graph = op4(graph)
    elif op==5:
        graph = op5(graph)
    elif op==6:
        graph = op6(graph)
for i in graph:
    print(*i)
