try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
RGB = [list(map(int,input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = RGB[0]

for i in range(1,n):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1)%3] + RGB[i][j], dp[i-1][(j+2)%3] + RGB[i][j])
print(min(dp[n-1]))