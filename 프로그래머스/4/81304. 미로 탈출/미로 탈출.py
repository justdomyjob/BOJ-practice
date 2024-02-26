import heapq
from collections import defaultdict

def solution(n, start, end, roads, traps):
    edges = [[] for _ in range(n+1)]
    for a,b,c in roads:
        edges[a].append((b,c))
        edges[b].append((a,-c))

    return bfs(edges,traps,start,end)
INF = 10**9

def bfs(edges,traps,start,end):
    traps.sort()
    trap_bit = defaultdict(int)
    for i,data in enumerate(traps):
        trap_bit[data] = i+1
    visited = defaultdict(lambda :INF)
    visited[(start,0)] = 0
    q = []
    heapq.heappush(q,(0,start,0))
    minimum = INF
    while q:
        dis,v,cur_trap = heapq.heappop(q)
        if visited[(v,cur_trap)] <dis :
            continue
        for u, c in edges[v]:
            # u나 v가 cur_trap에 하나만 있을때
            if (1<<trap_bit[u] & cur_trap and not(1<<trap_bit[v] & cur_trap)) or ( not (1<<trap_bit[u] & cur_trap) and 1<<trap_bit[v] & cur_trap):
                cost = -c
            else:
                cost = c
            if cost > 0 :
                next_trap = cur_trap
                if u in traps:
                    next_trap ^= 1 << trap_bit[u]
                if visited[(u,next_trap)] > dis + cost:
                    visited[(u, next_trap)] = dis + cost
                    if u == end:
                        minimum = min(minimum, dis+cost)
                    heapq.heappush(q,(dis+cost,u,next_trap))
    return minimum

# solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])