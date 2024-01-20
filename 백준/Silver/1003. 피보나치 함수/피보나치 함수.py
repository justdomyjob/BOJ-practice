import sys

dp= [0] * 41
dp[0]=0
dp[1]=1

for i in range(2,41):
    dp[i] = dp[i-1]+dp[i-2]

test = int(input())
for _ in range(test):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print("1 0")
    else:
        print(dp[n-1], end =" ")
        print(dp[n])
