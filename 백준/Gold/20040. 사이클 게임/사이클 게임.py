import sys

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,sys.stdin.readline().rstrip().split())
parent = [i for i in range(n)]
for i in range(1,m+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    if find(parent,a)==find(parent,b):
        print(i)
        exit(0)
    union(parent,a,b)
print(0)
