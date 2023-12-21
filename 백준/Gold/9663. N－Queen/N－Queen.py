import sys
n = int(sys.stdin.readline().rstrip())
sys.setrecursionlimit(10**5)
count = 0
queens = []

def dfs():
    global count
    if len(queens)==n:
        count+=1
    i = len(queens)
    for j in range(n):
        if j not in queens and can(i,j):
            queens.append(j)
            dfs()
            queens.pop()
def can(x,y):
    for x1,y1 in enumerate(queens):
        if abs(x1-x) == abs(y1-y):
            return False
    return True 
dfs()
print(count)