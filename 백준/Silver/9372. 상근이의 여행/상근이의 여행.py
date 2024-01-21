import sys

input = sys.stdin.readline


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


test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
    print(n-1)

