R,C,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]
CLEAN = -1

dx,dy = [-1,0,1,0], [0,1,0,-1]

find = False
for i in range(R):
    for j in range(C):
        if graph[i][j]==-1:
            cx1=i
            find = True
            break
    if find:
        break
cx2=cx1+1

def defuse():
    temp_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0 :
                for dir in range(4):
                    ni = i + dx[dir]
                    nj = j + dy[dir]
                    if 0<=ni < R and 0<= nj < C and graph[ni][nj] != CLEAN:
                        temp_graph[ni][nj] += graph[i][j]//5
                        temp_graph[i][j] -= graph[i][j]//5
    for i in range(R):
        for j in range(C):
            graph[i][j] += temp_graph[i][j]

def circulate1():
    for i in range(cx1-1,0,-1):
        graph[i][0] = graph[i-1][0]
    for j in range(C-1):
        graph[0][j] = graph[0][j+1]
    for i in range(cx1):
        graph[i][C-1] = graph[i+1][C-1]
    for j in range(C-1,0,-1):
        if j==1:
            graph[cx1][j] = 0
        else:
            graph[cx1][j] = graph[cx1][j-1]

def circulate2():
    for i in range(cx2 + 1, R-1):
        graph[i][0] = graph[i + 1][0]
    for j in range(C - 1):
        graph[R-1][j] = graph[R-1][j + 1]
    for i in range(R-1,cx2,-1):
        graph[i][C - 1] = graph[i - 1][C - 1]
    for j in range(C - 1, 0, -1):
        if j == 1:
            graph[cx2][j] = 0
        else:
            graph[cx2][j] = graph[cx2][j - 1]

for _ in range(T):
    defuse()
    circulate1()
    circulate2()

s = 0
for i in range(R):
    for j in range(C):
        if graph[i][j]!=-1:
            s+=graph[i][j]
print(s)