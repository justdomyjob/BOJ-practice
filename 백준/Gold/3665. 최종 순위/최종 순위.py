import sys
from collections import deque

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline().rstrip())
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    rank = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(n):
        for t in rank[i+1:]:
            graph[rank[i]][t] = 1

    change_count = int(sys.stdin.readline().rstrip())
    change_edge= []
    for _ in range(change_count):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        if graph[a][b]==1:
            graph[a][b] = 0
            graph[b][a] = 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0

    indegree = [[graph[x][i] for x in range(1,n+1)] for i in range(1,n+1)]

    q = deque()
    for i in range(n):
        if sum(indegree[i])==0:
            q.append(i)
    if len(q)>=2:
        print("?")
        continue
    if len(q)==0:
        print("IMPOSSIBLE")
        continue
    result = deque()
    can_decide = True
    while q:
        node = q.pop()
        result.append(node)
        for i in range(n):
            indegree[i][node] = 0
            if sum(indegree[i]) == 0 and i not in result:
                q.append(i)
        if len(q)>=2:
            can_decide = False
            break
    if can_decide==False:
        print("?")
        continue
    if len(result)!=n:
        print("IMPOSSIBLE")
        continue
    while result:
        print(result.popleft()+1,end=" ")
    print()

        