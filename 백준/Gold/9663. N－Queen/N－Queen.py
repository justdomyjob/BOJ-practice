import sys

n = int(input())

sys.setrecursionlimit(10**5)

count = 0
chess=[]
def dfs():
    global count
    y = len(chess)
    if y == n:
        count += 1
    for x in range(n):
        if x not in chess and avail(x,y):
            chess.append(x)
            dfs()
            chess.pop()

def avail(x,y):
    if y == 0 :
        return True
    for y1,x1 in enumerate(chess):
        if abs(x1-x) == abs(y1-y):
            return False
    return True

dfs()
print(count)
