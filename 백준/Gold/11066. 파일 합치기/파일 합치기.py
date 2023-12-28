import sys
try:
    sys.stdin = open("input.txt", "r") 
except:
    pass

T = int(input())
for _ in range(T):
    k = int(input())
    sumdp = [[0 for _ in range(k) ] for _ in range(k)]
    dp = [[0 for _ in range(k) ] for _ in range(k)]
    file = list(map(int, input().split()))
    for i in range(k):
        sumdp[i][i] = file[i]
    for i in range(1,k):
        for j in range(k-i):
            min = 1000000000
            sumdp[j][i+j] = file[j] + sumdp[j+1][i+j]
            for l in range(j,i+j):
                temp = dp[j][l]+dp[l+1][i+j]
                if temp < min:
                    min = temp
            dp[j][i+j] = min + sumdp[j][i+j]
    print(dp[0][k-1])
