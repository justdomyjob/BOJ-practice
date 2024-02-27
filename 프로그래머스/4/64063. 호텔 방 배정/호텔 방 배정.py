import sys

sys.setrecursionlimit(10**8)
def solution(k, room_number):
    parent = {}
    # parent = [i for i in range(k+1)]
    answer = []   
    for n in room_number:
        p = find(parent,n)
        answer.append(p)
        if p+1<=k:
            parent[p] = p+1
            union(parent,p,p+1)
    return answer

def find(parent,x):
    if x not in parent:
        parent[x] = x
    elif parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a >b:
        parent[b] = a
    else:
        parent[a] = b


# print(solution(10,[1,3,4,1,3,1]))