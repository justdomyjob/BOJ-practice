import heapq
import sys

V, E = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a, c))
INF = 10**9
#distance = [INF for _ in range(V+1)]

def dijkstra(start):
    distance = [INF for _ in range(V + 1)]
    q=[]
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for neighbor, dis in graph[now]:
            new_distance = dis + distance[now]
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(q, (new_distance, neighbor))
    return distance

def min_distance(u,v):
    return dijkstra(u)[v]

Start = 1
Mid1, Mid2 = map(int,sys.stdin.readline().rstrip().split())
End = V
first_course = min_distance(Start,Mid1) + min_distance(Mid1,Mid2) + min_distance(Mid2,End)
second_course = min_distance(Start,Mid2) + min_distance(Mid1,Mid2) + min_distance(Mid1,End)
if first_course >= INF and second_course >=INF:
    print(-1)
else:
    print(min(first_course,second_course))


