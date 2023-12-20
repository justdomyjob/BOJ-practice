from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

n ,m = map(int,input().split())
snake_and_ladder = [[] for _ in range(101)]
for _ in range(n+m):
    a, b =map(int,input().split())
    snake_and_ladder[a] = b
visited = [-1 for _ in range(101)]

def bfs(x) :
    visited[x] = 0
    node =deque()
    node.append(x)
    while node:
        x1 = node.popleft()
        for x2 in [i+x1 for i in range(1,7) if i+x1< 101]:
            if snake_and_ladder[x2] and visited[snake_and_ladder[x2]]==-1:
                new_place = snake_and_ladder[x2]
                visited[new_place] = visited[x1] +1
                node.append(new_place)
            elif snake_and_ladder[x2] :
                continue
            elif visited[x2] == -1:
                visited[x2] = visited[x1] +1
                node.append(x2)
    return visited[100]
print(bfs(1))