def solution(board, skill):
    r = len(board)
    c = len(board[0])
    print(r,c)
    dp = [[0 for _ in range(c)] for _ in range(r)]
    for type, r1, c1, r2, c2, degree in skill:
        if type ==2:
            dp[r1][c1] += degree
            try:
                dp[r2+1][c1] -= degree
            except:
                pass
            try:
                dp[r1][c2+1] -= degree
            except:
                pass
            try:
                dp[r2+1][c2+1] += degree
            except:
                pass
        else:
            dp[r1][c1] -= degree
            try:
                dp[r2 + 1][c1] += degree
            except:
                pass
            try:
                dp[r1][c2 + 1] += degree
            except:
                pass
            try:
                dp[r2+1][c2+1] -= degree
            except:
                pass
    for i in range(1,r):
        for j in range(c):
            dp[i][j] = dp[i-1][j] + dp[i][j]

    for i in range(r):
        for j in range(1,c):
            dp[i][j] = dp[i][j-1] + dp[i][j]
    for i in range(r):
        for j in range(c):
            dp[i][j] += board[i][j]

    count = 0
    for i in range(r):
        for j in range(c):
            if dp[i][j] > 0:
                count+=1
    return count

# solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[2,1,0,3,4,3],[2,0,1,3,3,5]])