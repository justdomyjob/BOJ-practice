import sys
from collections import deque

n, k =map(int,sys.stdin.readline().rstrip().split())

a=deque([i for i in range(1,n+1)])
print("<", end="")
while a:
    a.rotate(-k)
    if len(a)>1:
        print(a.pop(), end=", ")
    else:
        print(a.pop(), end="")
print(">")