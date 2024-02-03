import copy

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


cctv = []

for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append((i,j,graph[i][j]))
num_cctv = len(cctv)

MAX = 0

def count(graph):
    ret = 0
    for i in range(n):
        for j in range(m):
           if graph[i][j]==0:
                ret+=1
    return ret



dx,dy = [-1,0,1,0],[0,1,0,-1]

def color(graph,i,j,k):
    i = i+dx[k]
    j = j+dy[k]
    while 0<=i<n and 0<=j<m and graph[i][j] != 6:
        if graph[i][j]==0:
            graph[i][j] = "#"
        i = i + dx[k]
        j = j + dy[k]


def cc(cctv,graph):
    ret = []
    i,j,n = cctv
    if n==1:
        for k in range(4):
            graph2 = copy.deepcopy(graph)
            color(graph2,i,j,k)
            ret.append(graph2)
    if n==2:
        for k in range(2):
            graph2 = copy.deepcopy(graph)
            color(graph2, i, j, k)
            color(graph2, i, j, k+2)
            ret.append(graph2)
    if n==3:
        for k in range(4):
            graph2 = copy.deepcopy(graph)
            color(graph2, i, j, k)
            color(graph2, i, j, (k+1)%4)
            ret.append(graph2)
    if n==4:
        for k in range(4):
            graph2 = copy.deepcopy(graph)
            color(graph2, i, j, k)
            color(graph2, i, j, (k+1)%4)
            color(graph2, i, j, (k + 2) % 4)
            ret.append(graph2)
    if n == 5:
        graph2 = copy.deepcopy(graph)
        color(graph2, i, j, 0)
        color(graph2, i, j, 1)
        color(graph2, i, j, 2)
        color(graph2, i, j, 3)
        ret.append(graph2)
    return ret

MIN = 10**6
def do(n,graph):
    global MIN
    if n==num_cctv:
        c = count(graph)
        MIN = min(c,MIN)
        return
    copy_graph = copy.deepcopy(graph)
    for graph2 in cc(cctv[n],copy_graph):
        do(n+1,graph2)

do(0,graph)
print(MIN)