N,M,B = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

depth_set = set()
s = B
for i in range(N):
    for j in range(M):
        depth_set.add(graph[i][j])
        s += graph[i][j]

tallest = min(s//(N*M), max(depth_set))
shortest = min(depth_set)

dic = {}
for tall in range(shortest,tallest+1):
    time = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > tall:
                time += ((graph[i][j]-tall)*2)
            elif graph[i][j] < tall:
                time += abs(graph[i][j]-tall)
    dic[time] = tall

item = list(dic.items())
item.sort(key = lambda x:(x[0],-x[1]))
print(item[0][0],item[0][1])