S = input()
T = input()
lenS = len(S)
lenT = len(T)
dp =[[0 for _ in range(lenS)] for _ in range(lenT)]

for j in range(lenS):
    if S[j] == T[0]:
        dp[0][j] = 1

for i in range(lenT):
    if S[0] == T[i]:
        dp[i][0] = 1

for i in range(1,lenT):
    for j in range(1,lenS):
        if T[i] ==S[j]:
            dp[i][j] = dp[i-1][j-1] +1
max_list = [max(i) for i in dp]
print(max(max_list))
