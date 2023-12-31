from collections import deque

str = input()
explosion = input()
explosionSize = len(explosion)

stack = deque()
buf = deque()

first = explosion[0]
for char in str:
    stack.append(char)
    if char == first:
        buf.append(1)
        if buf[-1] == explosionSize:
            buf.pop()
            for _ in range(explosionSize):
                stack.pop()
        continue
    if buf:
        if char == explosion[buf[-1]]:
            buf[-1]+=1
            if buf[-1] == explosionSize:
                buf.pop()
                for _ in range(explosionSize):
                    stack.pop()
        else:
            buf[-1] = 0
if stack:
    print("".join(list(stack)))
else:
    print("FRULA")