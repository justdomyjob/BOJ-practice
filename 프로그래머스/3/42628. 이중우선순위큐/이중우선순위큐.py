import re
from bisect import bisect_left, bisect_right
def solution(operations):
    q =[]
    pattern = re.compile("([ID]) ([-]?\d+)")
    for op in operations:
        o = pattern.findall(op)
        if o[0][0] =="I":
            num = int(o[0][1])
            index = bisect_left(q,num)
            q.insert(index,num)
        elif o[0][1]=="1":
            if q:
                q.pop()
        elif o[0][1]=="-1":
            if q:
                del q[0]
    if not q:
        return [0,0]
    if q:
        return [q[-1],q[0]]
