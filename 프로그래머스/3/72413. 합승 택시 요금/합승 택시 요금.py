def solution(n, s, a, b, fares):
    edges = [[] for _ in range(n+1)]
    INF = 10**9
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i][i] = 0
    for c,d,f in fares:
        graph[c][d] = f
        graph[d][c] = f
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
    # for g in graph:
    #     print(g)
    # print()
    minimum = INF
    for i in range(1,n+1):
        distance = graph[s][i] + graph[i][a] + graph[i][b]
        minimum = min(minimum,distance)
    answer = 0
    return minimum