from collections import deque

n = int(input())
numbers = list(map(int,input().split()))
zeroToN = [i for i in range(n)]
numberWithOrder = [(a,b) for a,b in zip(numbers,zeroToN)]

count = {}
for number in numbers:
    count[number] = count.get(number, 0) +1

stack = deque()
ans = [-1 for _ in range(n)]
for number, i in numberWithOrder:
    while stack and count.get(stack[-1][0],0) < count.get(number,0):
        ans[stack[-1][1]] = number
        stack.pop()
    stack.append((number,i))
for num in ans:
    print(num,end=" ")