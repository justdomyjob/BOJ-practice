N = int(input())
homes = [list(map(int,input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]

INF = 10**9
MIN = INF
#1 처음 R 선택
dp[1] = [INF, homes[0][0] + homes[1][1], homes[0][0] + homes[1][2]]
for i in range(2,N):
    dp[i][0] = homes[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = homes[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = homes[i][2] + min(dp[i - 1][0], dp[i - 1][1])

MIN = min(MIN,dp[N-1][1],dp[N-1][2])
#2
dp[1] = [homes[0][1] + homes[1][0], INF, homes[0][1] + homes[1][2]]
for i in range(2,N):
    dp[i][0] = homes[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = homes[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = homes[i][2] + min(dp[i - 1][0], dp[i - 1][1])
MIN = min(MIN,dp[N-1][0],dp[N-1][2])
#3
dp[1] = [homes[0][2] + homes[1][0], homes[0][2] + homes[1][1], INF]
for i in range(2,N):
    dp[i][0] = homes[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = homes[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = homes[i][2] + min(dp[i - 1][0], dp[i - 1][1])
MIN = min(MIN,dp[N-1][0],dp[N-1][1])
print(MIN)