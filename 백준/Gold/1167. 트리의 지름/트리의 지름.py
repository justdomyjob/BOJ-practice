import sys
sys.setrecursionlimit(10**5)
v = int(input())
edges = [[] for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
distance = [0 for _ in range(v+1)]
MIN = 10 ** 9
for i in range(1,v+1):
    a = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(len(a)//2-1):
        edges[a[0]].append((a[2*j+1],a[2*j+2]))

def dfs(v, root_length): #return end 길이
    visited[v] = 1
    default = 0
    end_length_list = []
    for u,dis in edges[v]:
        if visited[u]==0:
            end_length = dfs(u, root_length + dis)
            end_length_list.append(end_length + dis)
            if end_length + dis > default:
                default = end_length + dis
    end_length_list.sort(reverse=True)
    if len(end_length_list) == 0:
        distance[v] = root_length
    elif len(end_length_list)==1:
        distance[v] = root_length + end_length_list[0]
    else:
        root_end_length = root_length + end_length_list[0]
        end_end_length = end_length_list[0] + end_length_list[1]
        distance[v] = max(end_end_length,root_end_length)
    return default
dfs(1,0)
print(max(distance))
