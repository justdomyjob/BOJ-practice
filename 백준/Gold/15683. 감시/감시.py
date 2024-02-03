import copy

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cctv = []

for i in range(n):
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append((i,j,graph[i][j]))
num_cctv = len(cctv)

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

MIN = 10**6
for case in range(4**num_cctv):
    copy_graph = [arr[:] for arr in graph]
    for i,j,type in cctv:
        d = case % 4  # 방향
        case //= 4
        if type == 1:
            color(copy_graph, i, j, d)
        if type == 2:
            color(copy_graph, i, j, d)
            color(copy_graph, i, j, (d + 2)%4)
        if type == 3:
            color(copy_graph, i, j, d)
            color(copy_graph, i, j, (d + 1) % 4)
        if type == 4:
            color(copy_graph, i, j, d)
            color(copy_graph, i, j, (d + 1) % 4)
            color(copy_graph, i, j, (d + 2) % 4)
        if type == 5:
            color(copy_graph, i, j, d)
            color(copy_graph, i, j, (d + 1) % 4)
            color(copy_graph, i, j, (d + 2) % 4)
            color(copy_graph, i, j, (d + 3) % 4)
    c = count(copy_graph)
    MIN = min(c,MIN)
print(MIN)