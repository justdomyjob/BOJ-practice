import sys
from collections import deque

n= int(input())
histogram = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

stack = deque()
currentMax = 0
for i in range(n):
    while stack and histogram[stack[-1]] > histogram[i]:
        height = histogram[stack[-1]]
        stack.pop()
        width = i #스택에 더이상 없을 때는 왼쪽부터 세면
        if stack:
            width = i-1 - stack[-1]
        currentMax = max(currentMax,width * height)
    stack.append(i)
while stack:
    height = histogram[stack[-1]]
    stack.pop()
    width = n #스택에 더이상 없을 때는 왼쪽부터 세면
    if stack:
        width = n - stack[-1] -1
    currentMax = max(currentMax, width * height)
print(currentMax)
