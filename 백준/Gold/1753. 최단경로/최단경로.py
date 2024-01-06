import heapq
import sys

V ,E = map(int,sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(V+1)]
INF = 10**9
distance = [INF for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append((b,c)) # a->b c거리

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #해당 노드는 이미 처리한 적이 있다.
            continue
        for neighbor, dis in graph[now]:
            new_distance = distance[now] + dis
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(q, (new_distance, neighbor))
dijkstra(start)
for dis in distance[1:]:
    if dis!=INF:
        print(dis)
    else:
        print("INF")
