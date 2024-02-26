import heapq
from collections import deque, defaultdict

def solution(n, start, end, roads, traps):
    edges = [[] for _ in range(n+1)]
    for a,b,c in roads:
        edges[a].append((b,c))
        edges[b].append((a,-c))

    return bfs(n,edges,traps,start,end)

def bfs(n,edges,traps,start,end):
    INF = 10**9
    visited = defaultdict(lambda :INF)
    visited[(start,frozenset())] = 0
    q = []
    heapq.heappush(q,(0,start,frozenset()))
    minimum = INF
    while q:
        dis,v,cur_trap = heapq.heappop(q)
        if visited[(v,cur_trap)] < dis:
            continue
        for u, c in edges[v]:
            if (u in cur_trap and v not in cur_trap) or (u not in cur_trap and v in cur_trap):
                cost = -c
            else:
                cost = c
            if cost > 0 :
                next_trap = cur_trap.copy()
                if u in traps:
                    if u in cur_trap:
                        next_trap = set(next_trap)
                        next_trap.remove(u)
                        next_trap = frozenset(next_trap)
                    else:
                        next_trap = set(next_trap)
                        next_trap.add(u)
                        next_trap = frozenset(next_trap)
                else:
                    pass
                if visited[(u,next_trap)] > dis + cost:
                    
                    visited[(u, next_trap)] = dis + cost
                    if u == end:
                        minimum = min(minimum, dis+cost)
                    heapq.heappush(q,(dis+cost,u,next_trap))
    # for v in visited:
    #     print(v)
    # print()
    return minimum

# solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])
# solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])