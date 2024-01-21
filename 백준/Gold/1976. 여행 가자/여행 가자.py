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

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
for i in range(1,n+1):
    connect = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(1,n+1):
        if connect[j-1]==1:
            union(parent,i,j)

plan_city = list(map(int,sys.stdin.readline().rstrip().split()))
root = [find(parent,i) for i in plan_city]
for i in range(1,len(root)):
    if root[i-1]!=root[i]:
        print("NO")
        exit(0)
print("YES")
