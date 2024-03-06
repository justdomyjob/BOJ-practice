maximum = 0
def solution(info, edges):
    edge = [[] for _ in range(len(info))]
    for a,b in edges:
        edge[a].append(b)
        # edge[b].append(a)
    def dfs(cur,sheep,wolf,next_node):
        global maximum
        sheep += info[cur] ^ 1
        wolf += info[cur]
        if sheep <= wolf :
            return
        maximum = max(maximum,sheep)
        for u in edge[cur]:
            next_node.add(u)
        for n in next_node:
            temp_next = next_node.copy()
            temp_next.remove(n)
            dfs(n,sheep,wolf,temp_next)

    dfs(0,0,0,set())

    return maximum