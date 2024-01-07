import heapq
import sys

def dijkstra(start,n):
    distance_table = [INF for _ in range(n + 1)]
    q=[]
    heapq.heappush(q, (0,start))
    distance_table[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if distance_table[now] < distance:
            continue
        for neighbor, dis in graph[now]:
            new_distance = dis + distance_table[now]
            if new_distance < distance_table[neighbor]:
                distance_table[neighbor] = new_distance
                heapq.heappush(q,(new_distance, neighbor))
    return distance_table
case = int(input())
for _ in range(case):
    n,m,t = map(int,sys.stdin.readline().rstrip().split())
    s,g,h = map(int,sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(n+1)]
    INF = 10**9
    odor_distance = 0

    for _ in range(m):
        a,b,d = map(int,sys.stdin.readline().rstrip().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a==g and b==h) or (a==h and b==g):
            odor_distance = d

    destination = []
    for _ in range(t):
        destination.append(int(sys.stdin.readline().rstrip()))
    destination.sort()

    for dest in destination:
        if (dijkstra(s,n)[dest] == odor_distance + dijkstra(s,n)[g] + dijkstra(h,n)[dest] or
            dijkstra(s, n)[dest] == odor_distance + dijkstra(s, n)[h] + dijkstra(g, n)[dest]):
            print(dest, end=" ")
    print()
