import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deq =deque()
for _ in range(n):
    num = sys.stdin.readline().rstrip()
    n = num[0]
    if n == "1":
        deq.appendleft(int(num[2:]))
    elif n == "2":
        deq.append(int(num[2:]))
    elif n == "3":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif n == "4":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif n == "5":
        print(len(deq))
    elif n == "6":
        if deq:
            print(0)
        else:
            print(1)
    elif n == "7":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif n == "8":
        if deq:
            print(deq[-1])
        else:
            print(-1)