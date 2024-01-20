import math
import sys
test = int(input())
for _ in range(test):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().rstrip().split())
    #1
    d = math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    elif x1==x2 and y1==y2 and r1!=r2:
        print(0)
    elif r1+r2 > d:
        if abs(r1-r2) > d:
            print(0)
        elif abs(r1-r2) < d:
            print(2)
        else:
            print(1)
    elif r1+r2 < d:
        print(0)
    else:
        print(1)