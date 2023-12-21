from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
for _ in range(n):
    aa = input()
    stack =deque()
    finished = False
    for a in aa:
        if a=="(":
            stack.append(1)
        else:
            try:
                stack.pop() 
            except:
                print("NO")
                finished=True
                break
    if finished:
        continue
    else:
        if stack:
            print("NO")
        else:
            print("YES")