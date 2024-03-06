from collections import defaultdict, deque


def solution(edges):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    edge = defaultdict(list)
    v_set = set()

    def detect(v):
        visited = set()
        visited.add(v)
        q= deque()
        q.append(v)
        if out_degree[v] == 0:
            return 2
        elif in_degree[v] == 2 and out_degree[v] == 2:
            return 3
        while q:
            v = q.popleft()
            for u in edge[v]:
                if u not in visited:
                    visited.add(u)
                    q.append(u)
                    if out_degree[u] == 0:
                        return 2
                    elif in_degree[u] == 2 and out_degree[u] == 2:
                        return 3
        return 1
    for a,b in edges:
        v_set.add(a)
        v_set.add(b)
        in_degree[b] +=1
        out_degree[a] +=1
        edge[a].append(b)
    for v in v_set:
        if in_degree[v] == 0 and out_degree[v] >=2:
            center = v
    ret = [center,0,0,0]
    for u in edge[center]:
        in_degree[u]-=1
        what = detect(u)
        ret[what] +=1

    return ret