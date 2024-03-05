from collections import deque


def solution(info, edges):
    edge = [[] for _ in range(len(info))]
    for a,b in edges:
        edge[a].append(b)
        edge[b].append(a)
    def bfs(start):
        yang = frozenset({start})
        wolf = frozenset()
        q = deque()
        q.append((yang,wolf,start))
        visited = set()
        visited.add((yang,wolf,start))
        while q:
            yang,wolf, v = q.popleft()
            for u in edge[v]:
                if info[u] == 1: #늑대인경우
                    if u in wolf:
                        if (yang,wolf,u) not in visited:
                            visited.add((yang,wolf,u))
                            q.append((yang,wolf,u))
                    else:
                        if len(yang) > len(wolf) +1:
                            if (yang, wolf, u) not in visited:
                                temp_wolf = set(wolf)
                                temp_wolf.add(u)
                                temp_wolf = frozenset(temp_wolf)
                                visited.add((yang, temp_wolf, u))
                                q.append((yang, temp_wolf, u))
                else:  #양인경우
                    if u in yang:
                        if (yang,wolf,u) not in visited:
                            visited.add((yang,wolf,u))
                            q.append((yang,wolf,u))
                    else:
                        if (yang, wolf, u) not in visited:
                            temp_yang = set(yang)
                            temp_yang.add(u)
                            temp_yang = frozenset(temp_yang)
                            visited.add((temp_yang, wolf, u))
                            q.append((temp_yang, wolf, u))
        maximum = 0
        for v in visited:
            maximum = max(maximum,len(v[0]))
        return maximum
    answer = bfs(0)
    return answer

solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])