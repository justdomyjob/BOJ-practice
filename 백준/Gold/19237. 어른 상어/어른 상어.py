import copy

n,m,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dic = {}
up,down,left,right = 1,2,3,4
dic[up] = (-1,0)
dic[down] = (1,0)
dic[left] = (0,-1)
dic[right] = (0,1)

direction = list(map(int,input().split()))
priority = [[list(map(int,input().split())) for _ in range(4)] for _ in range(m)]

#처음
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = [graph[i][j],0]
        else:
            graph[i][j] = [graph[i][j], k]

def move_all():
    global graph
    temp_graph = copy.deepcopy(graph)
    for shark in range(1,m+1):
        move(shark,temp_graph)
    graph = temp_graph
out =0
def move(shark,temp_graph):
    global out
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] == shark and graph[i][j][1] == k:
                dir = direction[shark-1]
                prior_dir = priority[shark-1][dir-1]
                for move_dir in prior_dir:
                    ni = i + dic[move_dir][0]
                    nj = j + dic[move_dir][1]
                    if 0<=ni<n and 0<=nj<n:
                        if graph[ni][nj][0] == 0: #빈칸
                            if temp_graph[ni][nj][1] == k+1:
                                out += 1
                                return
                            else:
                                temp_graph[ni][nj] = [shark,k+1]
                                direction[shark - 1] = move_dir
                                return
                        else:
                            continue
                for move_dir in prior_dir: #빈칸이 없으면 내 채취로
                    ni = i + dic[move_dir][0]
                    nj = j + dic[move_dir][1]
                    if 0 <= ni < n and 0 <= nj < n:
                        if graph[ni][nj][0] == shark:
                            temp_graph[ni][nj] = [shark, k + 1]
                            direction[shark - 1] = move_dir
                            return
def minus():
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] > 0:
                if graph[i][j][1] ==1 :
                    graph[i][j] = [0,0]
                else:
                    graph[i][j] = [graph[i][j][0], graph[i][j][1]-1]

def pp():
    for g in graph:
        print(g)
    print()

for i in range(1,1001):
    move_all()
    minus()
    if out == m-1:
        print(i)
        exit(0)
print(-1)
