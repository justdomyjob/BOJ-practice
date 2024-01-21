import sys


def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline().rstrip())
    parent = {}
    count = {}
    for _ in range(n):
        a, b= sys.stdin.readline().rstrip().split()
        parent[a] = parent.get(a,a)
        parent[b] = parent.get(b,b)
        
        root_a = find(parent,a)
        root_b = find(parent,b)
        
        if root_a == root_b:
            print(count[root_a])
            continue
        count[root_a] = count.get(root_a,1)
        count[root_b] = count.get(root_b,1)
        
        union(parent,a,b)

        new_root = find(parent,a)
        count[new_root] = count[root_a] + count[root_b]
        print(count[new_root])
