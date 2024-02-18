import heapq
from collections import deque

n,m,k = map(int,input().split())
year_food = [list(map(int,input().split())) for _ in range(n)]
food = [[5 for _ in range(n)] for _ in range(n)]
trees = [list(map(int,input().split())) for _ in range(m)]
tree_graph = [[[] for _ in range(n) ] for _ in range(n)]

dy = [-1,-1,-1, 0,0, 1,1,1]
dx = [-1, 0, 1,-1,1,-1,0,1]

for tree in trees:
    x,y,old = tree
    tree_graph[x-1][y-1].append(old)
for i in range(n):
    for j in range(n):
        tree_graph[i][j].sort()
        tree_graph[i][j] = deque(tree_graph[i][j])

def spring_summer():
    for i in range(n):
        for j in range(n):
            tree = tree_graph[i][j]
            new_tree = deque()
            dead_tree = 0
            while tree:
                old = tree.popleft()
                if food[i][j]<old:
                    dead_tree += old//2
                    dead_tree += sum([i//2 for i in tree])
                    break
                else:
                    food[i][j]-=old
                    new_tree.append(old+1)
            tree_graph[i][j] = new_tree
            food[i][j] +=dead_tree
def fall():
    for y in range(n):
        for x in range(n):
            for tree in tree_graph[y][x]:
                if tree%5==0:
                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0<=ny<n and 0<=nx<n:
                            tree_graph[ny][nx].appendleft(1)
                            # heapq.heappush(tree_graph[ny][nx],1) #속도가 걸릴 수 있음
def winter():
    for i in range(n):
        for j in range(n):
            food[i][j] += year_food[i][j]

for _ in range(k):
    spring_summer()
    fall()
    winter()
ret = 0
for line in tree_graph:
    for tree in line:
        ret+=len(tree)
print(ret)