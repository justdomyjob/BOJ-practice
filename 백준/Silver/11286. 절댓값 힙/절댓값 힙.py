import heapq
import sys

minq = []
n = int(input())
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if minq:
            temp = heapq.heappop(minq)
            if temp % 10 == 1: #양수일경우
                print((temp-1)//10)
            else:
                print(-1*(temp+1)//10)
        else:
            print(0)
    else:
        if num > 0:
            heapq.heappush(minq, 10*num + 1)
        else:
            heapq.heappush(minq, 10 * abs(num) - 1)
