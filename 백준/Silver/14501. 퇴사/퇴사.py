n = int(input())
consult = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for _ in range(100)] #dp[i] : i일 까지 일을하는 방법중 가장 큰 값
for i in range(n):
    ti, pi = consult[i]
    dp[i] = max(dp[:i + 1])
    dp[i+ti] = max(dp[i+ti], dp[i] + pi)
print(max(dp[:n+1]))