import sys

input = sys.stdin.readline
n = int(input())

po = [int(input()) for _ in range(n)]
if n==1:
    print(po[0])
    exit(0)
elif n==2:
    print(po[0]+po[1])
    exit(0)
dp = [po[0],po[0]+po[1],max(po[0]+po[1],po[0]+po[2],po[1]+po[2])]
for i in range(3,n):
    a1 = po[i] + dp[i-2]
    a2 = po[i] + po[i-1] + dp[i-3]
    a3 = dp[i-1]
    dp.append(max(a1,a2,a3))
print(dp[n-1])