try : standard_input = open("input.txt", "r")  
except:pass

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

n = int(input())
def recur(n):
    if dp[n]!=0:
        return dp[n]
    else:
        for i in range(7,n+1):
            dp[i] = dp[i-1] + dp[i-5]
        return dp[n]
for _ in range(n):
    print(recur(int(input())))
