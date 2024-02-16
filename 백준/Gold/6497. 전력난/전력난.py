def find(x,parent):
    if x!=parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
while True:
    m,n = map(int,input().split())
    if m==n==0:
        break
    edges = []

    s = 0
    for _ in range(n):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))
        s+=z
    edges.sort()

    parent = [i for i in range(m)]

    ret = 0
    for z,x,y in edges:
        if find(x,parent)!=find(y,parent):
            ret+=z
            union(x,y,parent)
    print(s-ret)