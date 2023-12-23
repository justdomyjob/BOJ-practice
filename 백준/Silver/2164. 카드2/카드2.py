from collections import deque


n = int(input())
queue = deque([i+1 for i in range(n)])
while len(queue)!=1:
    queue.popleft()
    if len(queue)==1:
        break
    queue.rotate(-1)
print(queue.pop())