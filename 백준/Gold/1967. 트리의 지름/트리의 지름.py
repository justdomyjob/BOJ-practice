import heapq
import sys
sys.setrecursionlimit(10**5)
v = int(input())
edges = [[] for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
distance = [0 for _ in range(v+1)]

for i in range(v-1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    edges[a].append((b,c))
    edges[b].append((a,c))
ret = 0

def dfs(v, root_length): #return 가장 긴 end
    visited[v] = 1
    length_list = [0]
    for u,dis in edges[v]:
        if visited[u]==0:
            u_to_end_length= dfs(u, root_length + dis)
            v_to_end_length = u_to_end_length + dis
            heapq.heappush(length_list,-v_to_end_length)
    longest_end = -heapq.heappop(length_list)
    if length_list:
        distance[v] = longest_end + max(root_length, -heapq.heappop(length_list))
    else:
        distance[v] = longest_end + root_length
    return longest_end #end_len
dfs(1,0)
print(max(distance))
