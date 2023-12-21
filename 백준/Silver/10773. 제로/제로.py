from collections import deque
import sys

n = int(input())
stack = deque()
for _ in range(n):
    a = int(sys.stdin.readline().rstrip()) 
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
sum = 0
while stack:
    sum += stack.pop()
print(sum)
    

     