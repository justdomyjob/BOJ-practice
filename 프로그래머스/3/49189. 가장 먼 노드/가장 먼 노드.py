import heapq
def solution(n, edge):
    INF = 10**5
    distance = [INF for _ in range(n+1)]
    edges = [[] for _ in range(n+1)]
    for a,b in edge:
        edges[a].append(b)
        edges[b].append(a)
    distance[1] = 0
    q=[]
    heapq.heappush(q,(0,1))
    while q:
        dist,v = heapq.heappop(q)
        for u in edges[v]:
            cost = dist + 1
            if cost < distance[u]:
                distance[u] = cost
                heapq.heappush(q,(cost,u))
    m = max(distance[1:])
    count = 0
    for dis in distance[1:]:
        if dis==m:
            count+=1
            
    return count