import math
import sys

test = int(input())
for _ in range(test):
    x, y = map(int,sys.stdin.readline().rstrip().split())
    d = y-x

    n = math.floor(math.sqrt(d))
    # print("n = ", n)
    if d == n**2:
        print(2*n-1)
    elif d <= n*(n+1):
        print(2*n)
    else:
        print(2*n+1)