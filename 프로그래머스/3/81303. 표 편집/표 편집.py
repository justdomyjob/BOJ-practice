import bisect
from collections import deque

def solution(n, k, cmd):
    table = {i:[i-1,i+1] for i in range(n)}
    table[0] = [None,1]
    table[n-1] = [n-2,None]
    answer = ["O"] * n
    q=deque()
    for c in cmd:
        a = c.split()
        if a[0] == "U":
            num = int(a[1])
            for i in range(num):
                k = table[k][0]
        elif a[0] == "D":
            num = int(a[1])
            for i in range(num):
                k = table[k][1]
        elif a[0] == "C": #before k after, None k None, None k after, before k None
            before,after  = table[k]
            q.append((before,k,after))
            answer[k] = "X"
            if before == None:
                table[after][0] = None
                k = after
            else:
                if after==None:
                    table[before][1] = None
                    k = before
                else:
                    table[before][1] = after
                    table[after][0] = before
                    k = after

        elif a[0] == "Z":
            before, index, after = q.pop()
            answer[index] = "O"
            if before == None:
                table[after][0] = index
            elif after == None:
                table[before][1] = index
            else:
                table[after][0] = index
                table[before][1] = index


    return "".join(answer)

# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
