import sys


def find(parent, x):
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(count,parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
        count[a] += count[b]
        return count[a]
    elif a>b:
        parent[a] = b
        count[b] += count[a]
        return count[b]
    else:
        return count[a]

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline().rstrip())
    parent = {}
    count = {}
    for _ in range(n):
        a, b= sys.stdin.readline().rstrip().split()
        if a not in parent:
            parent[a] = a
            count[a] =1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        new_count = union(count,parent,a,b)
        print(new_count)
