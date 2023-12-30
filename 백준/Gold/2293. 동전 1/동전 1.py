import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
coins.sort()
MAX_VALUE = 100, 000
dp = [[-1 for _ in range(k + 1)] for _ in range(n)]  # dp[n-1][k]

coin = coins[0]
for i in range(k + 1):
    if i % coin == 0:
        dp[0][i] = 1
    else:
        dp[0][i] = 0
def count(n, k):
    if dp[n][k] != -1:
        return dp[n][k]
    else:
        start = k
        temp = 0
        while True:
            if start < 0:
                break
            temp += count(n-1,start)
            start -= coins[n]
        dp[n][k] = temp
        return temp
print(count(n-1,k))