import copy
import sys

N, Mbytes = map(int, sys.stdin.readline().rstrip().split())
appBytes = list(map(int,sys.stdin.readline().rstrip().split()))
appCosts = list(map(int,sys.stdin.readline().rstrip().split()))
MAX = 10000
dp = [0 for _ in range(MAX+1)] #dp[cost] = cost로 최대 M바이트 확보가능

for appByte,appCost in zip(appBytes,appCosts):
    dp_copy = copy.deepcopy(dp)
    for c in range(MAX+1):
        if c >= appCost:
            dp[c] = max(dp_copy[c - appCost] + appByte, dp_copy[c])
for c in range(MAX+1):
    if dp[c] >= Mbytes:
        print(c)
        break
