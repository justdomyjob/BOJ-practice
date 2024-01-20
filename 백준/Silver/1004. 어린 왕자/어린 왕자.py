import math
import sys


def enter(x1,y1,x2,y2,cx,cy,r):
    if inPlanet(x1,y1,cx,cy,r) == inPlanet(x2,y2,cx,cy,r):
        return 0
    else:
        return 1

def inPlanet(x,y,cx,cy,r):
    if math.sqrt((cx-x) ** 2 + (cy-y) ** 2)< r:
        return True
    elif math.sqrt((cx-x) ** 2 + (cy-y) ** 2) > r:
        return False
    else:
        print("error")
        return False


test = int(input())
for _ in range(test):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    n = int(sys.stdin.readline().rstrip())
    cxcyr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
    sum = 0
    for cx, cy, r in cxcyr:
        sum +=enter(x1,y1,x2,y2,cx,cy,r)
    print(sum)
