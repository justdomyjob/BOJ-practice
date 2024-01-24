import sys

def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] =a
    else:
        parent[a] =b

test_case = 1

while True:
    n,m = map(int,sys.stdin.readline().rstrip().split())
    parent = [i for i in range(n+1)]
    if n==m==0:
        break
        
    edges = []
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        union(parent,a,b)
        edges.append((a,b))
        
    root = [find(parent,i) for i in range(n+1)]

    edge_count = {}
    for i in root[1:]:
        edge_count[i] = edge_count.get(i,0)+1

    for a, b in edges:
        edge_count[find(parent,a)] = edge_count[find(parent,a)] -1

    tree_count = 0
    for count in edge_count:
        if edge_count[count]==1:
            tree_count+=1

    if tree_count==0:
        print(f'Case {test_case}: No trees.')
    elif tree_count==1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {tree_count} trees.')
    test_case+=1
