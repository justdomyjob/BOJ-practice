import heapq
import sys

n = int(input())
m = int(input())

INF = 10 **9
edge = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    edge[a].append((b,c))

start, end = map(int,sys.stdin.readline().rstrip().split())

def dijkstra(start):
    dist[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next, cost in edge[now]:
            if cost + dist[now] < dist[next]:
                dist[next] = cost + dist[now]
                heapq.heappush(q,(dist[next],next))
dijkstra(start)
print(dist[end])
