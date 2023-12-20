from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

def bfs(x):
    visited[x] = 0
    node = deque()
    node.append(x)
    while node:
        x1 = node.popleft()
        for x2 in [x1-1,x1+1,2*x1]:
            if 0 <= x2 <= OVER_WALK and visited[x2] == -1 :
                visited[x2] = visited[x1] +1
                node.append(x2)

N, K =map(int,input().split())
OVER_WALK = 100000
visited = [-1 for _ in range(OVER_WALK+1)]
bfs(N)
print(visited[K])
