import sys

input = sys.stdin.readline

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
n, m = map(int,input().split())
parent = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
cost = 0
for edge in edges:
    c,a,b = edge
    if find(parent,a)!=find(parent,b):
        cost+=c
        union(parent,a,b)
print(cost)
