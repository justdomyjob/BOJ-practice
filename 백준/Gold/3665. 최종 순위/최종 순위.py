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

    for _ in range(int(sys.stdin.readline().rstrip())):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        if graph[a][b]==1:
            graph[a][b] = 0
            graph[b][a] = 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
    edge=[[] for _ in range(n+1)]
    count = [0] * (n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] == 1:
                edge[i].append(j)
                count[j]+=1
            
    q1 = deque()
    q2 = deque()
    for i in range(1,n+1):
        if count[i]==0:
            q1.append(i)
    if len(q1)>=2:
        print("?")
        continue
    if len(q1)==0:
        print("IMPOSSIBLE")
        continue
    can_decide = True
    while q1:
        node = q1.popleft()
        q2.append(node)
        for u in edge[node]:
            count[u]-=1
            if count[u]==0:
                q1.append(u)
        if len(q1)>=2:
            can_decide=False
            break
    if can_decide==False:
        print("?")
        continue
    if len(q2)!=n:
        print("IMPOSSIBLE")
        continue
    while q2:
        print(q2.popleft(), end=" ")
    print()
