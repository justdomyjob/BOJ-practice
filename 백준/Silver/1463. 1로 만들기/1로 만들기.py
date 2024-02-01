import sys

n = int(input())
dp ={1:0}
def recur(n):
    if not n in dp:
        if n%3==0 and n%2==0:
            dp[n] = min(recur(n//3), recur(n//2)) + 1
        elif n%3==0:
            dp[n] = min(recur(n//3), recur(n - 1)) +1
        elif n%2==0:
            dp[n] =  min(recur(n//2) + 1, recur(n - 1) + 1)
        else:
            dp[n] = recur(n-1)+1
    return dp[n]
print(recur(n))