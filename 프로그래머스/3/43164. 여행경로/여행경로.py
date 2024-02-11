import heapq
def solution(tickets):
    edges = {}
    for start,end in tickets:
        edges[start] = edges.get(start,[])
        heapq.heappush(edges[start],end)
    ret = []
    def dfs(start):
        nonlocal ret
        ret.append(start)
        neigh = edges.get(start,[])
        if neigh:
            u = heapq.heappop(neigh)
            dfs(u)
        return ret
    ret = dfs("ICN")
    print(ret)
    
    return ret
