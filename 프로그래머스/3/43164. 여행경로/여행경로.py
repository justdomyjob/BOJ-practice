from collections import deque
def solution(tickets):
    edges = {}
    for start,end in tickets:
        edges[start] = edges.get(start,deque())
        edges[start].append(end)
    
    ret = []
    def dfs(start,n,orders):
        nonlocal ret
        if n == len(tickets):
            ret.append(orders[:])
            return
        else:
            neighbors = edges.get(start,[])
            for _ in range(len(neighbors)):
                u = neighbors.popleft()
                orders.append(u)
                dfs(u,n+1,orders)
                orders.pop()
                neighbors.append(u)
    dfs("ICN",0,["ICN"])
    ret.sort()
    # print(ret[0])
    return ret[0]
