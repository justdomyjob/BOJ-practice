try : standard_input = open("input.txt", "r")  
except:pass
from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if line == "front":
        try: print(queue[0])
        except: print(-1)
    elif line[:4]=="push":
        queue.append(int(line[5:]))
    elif line == "pop" :
        try: print(queue.popleft())
        except: print(-1)
    elif line == "size" : 
        print(len(queue))
    elif line == "empty":
        if queue: print(0)
        else: print(1)
    elif line == "back":
        try: print(queue[-1])
        except : print(-1)
    else:
        print("error")