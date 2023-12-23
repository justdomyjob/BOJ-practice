from collections import deque

try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())

node = deque(map(int,input().split()))
order = 1
stack =deque()
while node:
    front = node.popleft()
    if front == order:
        order+=1
        continue
    else:
        if stack:
            front2 = stack.pop()
            if front2==order:
                order+=1
                node.appendleft(front)
                continue
            else:
                stack.append(front2)
                stack.append(front)
        else:
            stack.append(front)
while stack:
    front = stack.pop()
    if front!=order:
        print("Sad")
        exit(0)
    else:
        order+=1
print("Nice")