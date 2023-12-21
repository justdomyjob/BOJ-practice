from collections import deque


try : standard_input = open("input.txt", "r")  
except:pass

while True:
    line = input()
    if line==".":
        break

    finished =False
    stack =deque()
    for l in line:
        if l=="(":
            stack.append(")")
        elif l=="[":
            stack.append("]")
        elif l==")" or l=="]":
            try:
                small = stack.pop()
                if small!=l:
                    print("no")
                    finished = True
                    break
            except:
                print("no")
                finished = True
                break
    if finished:
        continue
    else:
        if stack:
            print("no")        
        else:
            print("yes")