from collections import deque

n = int(input())
sequence = list(map(int,input().split()))
zeroToN = [i for i in range(n)]

sequenceWithNumber = [(a,b) for a,b in zip(sequence,zeroToN)]

ans = [-1 for _ in range(n)]
stack = deque()
for number,i in sequenceWithNumber:
    while stack and stack[-1][0] < number:
        ans[stack[-1][1]] = number
        stack.pop()
    stack.append((number,i))
for num in ans:
    print(num,end=" ")