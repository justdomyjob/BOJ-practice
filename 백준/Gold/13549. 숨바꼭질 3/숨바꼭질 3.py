import heapq
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
INF = 10**9
distance_table = [INF for _ in range(100001)]


def dijkstra(start,end):
    q = []
    heapq.heappush(q,(0,start))
    distance_table[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if distance_table[now] < distance:
            continue
        for dis, neighbor in [(0,2*now),(1,now+1),(1,now-1)]:
            if neighbor > 100000 or neighbor < 0:
                continue
            new_distance = dis + distance_table[now]
            if new_distance < distance_table[neighbor]:
                distance_table[neighbor] = new_distance
                heapq.heappush(q,(new_distance, neighbor))
    print(distance_table[end])
dijkstra(N,K)
