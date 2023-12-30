import heapq
import sys

maxq = []
n = int(input())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if maxq:
            print(-1 * heapq.heappop(maxq))
        else:
            print(0)
    else:
        heapq.heappush(maxq,-1 * num)
