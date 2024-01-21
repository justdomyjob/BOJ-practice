import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = 10 ** 6

def neigh(i, j):
    ret = []
    for step in steps:
        next_i = i + step[0]
        next_j = j + step[1]
        if 0 <= next_i <= n - 1 and 0 <= next_j <= m - 1 and maps[next_i][next_j] == 1:
            ret.append((next_i, next_j))
    return ret

def dfs(land, i, j):
    visited[i][j] = 1
    land.append((i, j))
    for next_i, next_j in neigh(i, j):
        if visited[next_i][next_j] == 0:
            visited[next_i][next_j] = 1
            dfs(land, next_i, next_j)

def get_land(i, j):
    land = []
    dfs(land, i, j)
    return land

land_list = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            land = get_land(i, j)
            land_list.append(land)
    
def distance(land1, land2):  # 2이상
    MIN = INF
    for i in range(n):
        limeMIN = INF
        for i1, j1 in land1:
            for i2, j2 in land2:
                if i1 == i and i2 == i:
                    jmin = min(j1,j2)
                    jmax = max(j1,j2)
                    between_country = False
                    for j3 in range(jmin+1,jmax):
                        if maps[i1][j3]==1:
                            between_country = True
                            break
                    if between_country:
                        continue
                    length = abs(j1 - j2) - 1
                    if limeMIN > length and length >=2:
                        limeMIN = length
        if limeMIN < MIN:
            MIN = limeMIN
    for j in range(m):
        limeMIN = INF
        for i1, j1 in land1:
            for i2, j2 in land2:
                if j1 == j and j2 == j:
                    imin = min(i1, i2)
                    imax = max(i1, i2)
                    between_country = False
                    for i3 in range(imin + 1, imax):
                        if maps[i3][j1] == 1:
                            between_country = True
                            break
                    if between_country:
                        continue
                    length = abs(i1 - i2) - 1
                    if limeMIN > length and length >=2:
                        limeMIN = length
        if limeMIN < MIN:
            MIN = limeMIN
    return MIN

edges = []
for i in range(len(land_list)):
    for j in range(i + 1, len(land_list)):
        cost = distance(land_list[i], land_list[j])
        if cost != INF:
            edges.append((cost, i, j))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges.sort()
parent = [i for i in range(len(land_list))]
cost_sum = 0
edge_count = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        cost_sum += cost
        union(parent, a, b)
        edge_count += 1
if edge_count != len(land_list) - 1:
    print(-1)
else:
    print(cost_sum)
