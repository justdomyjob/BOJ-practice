import math
import sys

def find(parent,x):
    if parent[x]!=x:
        parent[x]= find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,sys.stdin.readline().rstrip().split())

god = []
for _ in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    god.append((x,y))

already_edge=[]
edges = []
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    already_edge.append((a-1,b-1))

def cost(god1,god2):
    x1,y1 = god1
    x2,y2 = god2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

for i in range(n):
    for j in range(i+1,n):
        edges.append( (cost(god[i],god[j]), i,j) )
edges.sort()

parent = [i for i in range(n+1)]


for edge in already_edge:
    a,b = edge
    union(parent,a,b)

ret = 0
for edge in edges:
    c ,a, b = edge
    if find(parent,a)!= find(parent,b):
        ret+=c
        union(parent,a,b)
print(f'{ret:.2f}')
